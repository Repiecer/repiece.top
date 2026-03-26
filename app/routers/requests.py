from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional, List
from app import crud, schemas
from app.database import get_db

router = APIRouter(prefix="/api", tags=["requests"])

# ========== 请求相关接口 ==========
@router.get("/requests", response_model=List[schemas.RequestResponse])
def get_requests(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=200),
    search: Optional[str] = Query(None, max_length=100),
    db: Session = Depends(get_db)
):
    """获取所有活跃的拼单请求，支持搜索"""
    return crud.get_requests(db, skip=skip, limit=limit, search=search)

@router.get("/requests/{request_id}", response_model=schemas.RequestResponse)
def get_request(request_id: int, db: Session = Depends(get_db)):
    """获取单个请求详情"""
    request = crud.get_request(db, request_id)
    if not request:
        raise HTTPException(status_code=404, detail="请求不存在或已过期")
    return request

@router.post("/requests", response_model=schemas.RequestResponse, status_code=201)
def create_request(
    request: schemas.RequestCreate,
    db: Session = Depends(get_db)
):
    """发布新的拼单请求"""
    return crud.create_request(db, request)

@router.put("/requests/{request_id}", response_model=schemas.RequestResponse)
def update_request(
    request_id: int,
    request_update: schemas.RequestUpdate,
    db: Session = Depends(get_db)
):
    """更新请求信息"""
    updated = crud.update_request(db, request_id, request_update)
    if not updated:
        raise HTTPException(status_code=404, detail="请求不存在")
    return updated

# ========== 接取相关接口 ==========
@router.post("/pickups", response_model=schemas.PickupResponse, status_code=201)
def create_pickup(
    pickup: schemas.PickupCreate,
    db: Session = Depends(get_db)
):
    """接取一个拼单请求"""
    # 检查是否已接取
    if crud.check_user_picked(db, pickup.request_id, pickup.user_id):
        raise HTTPException(status_code=400, detail="您已接取过此请求")
    
    result = crud.create_pickup(db, pickup)
    if not result:
        raise HTTPException(status_code=400, detail="接取失败，请求可能已满员或不存在")
    return result

@router.get("/pickups/{user_id}")
def get_user_pickups(
    user_id: str,
    db: Session = Depends(get_db)
):
    """获取用户接取的请求列表"""
    return crud.get_user_pickups_with_requests(db, user_id)

@router.get("/pickups/check/{request_id}/{user_id}")
def check_pickup(
    request_id: int,
    user_id: str,
    db: Session = Depends(get_db)
):
    """检查用户是否已接取某请求"""
    picked = crud.check_user_picked(db, request_id, user_id)
    return {"picked": picked}

# ========== 健康检查 ==========
@router.get("/health")
def health_check():
    """健康检查接口"""
    return {"status": "ok", "message": "Shipping Helper API is running"}