from sqlalchemy.orm import Session
from sqlalchemy import or_
from typing import List, Optional
from app import models, schemas

# ========== Request CRUD ==========
def get_request(db: Session, request_id: int) -> models.Request | None:
    """获取单个请求"""
    return db.query(models.Request).filter(
        models.Request.id == request_id,
        models.Request.status == "active"
    ).first()

def get_requests(
    db: Session, 
    skip: int = 0, 
    limit: int = 100,
    search: Optional[str] = None
) -> List[models.Request]:
    """获取所有活跃请求，支持搜索"""
    query = db.query(models.Request).filter(models.Request.status == "active")
    
    if search:
        query = query.filter(
            or_(
                models.Request.product_name.contains(search),
                models.Request.description.contains(search)
            )
        )
    
    # 按优先级降序（特急优先），再按创建时间降序
    query = query.order_by(
        models.Request.priority.desc(),
        models.Request.created_at.desc()
    )
    
    return query.offset(skip).limit(limit).all()

def create_request(db: Session, request: schemas.RequestCreate) -> models.Request:
    """创建新请求"""
    db_request = models.Request(
        product_name=request.product_name,
        product_url=request.product_url,
        max_people=request.max_people,
        current_people=1,  # 发布者自己算一个
        phone=request.phone,
        qq=request.qq,
        priority=request.priority,
        description=request.description,
        publisher_name=request.publisher_name,
        publisher_id=request.publisher_id,
        status="active"
    )
    db.add(db_request)
    db.commit()
    db.refresh(db_request)
    return db_request

def update_request(
    db: Session, 
    request_id: int, 
    request_update: schemas.RequestUpdate
) -> models.Request | None:
    """更新请求"""
    db_request = get_request(db, request_id)
    if not db_request:
        return None
    
    update_data = request_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_request, key, value)
    
    db.commit()
    db.refresh(db_request)
    return db_request

def complete_request(db: Session, request_id: int) -> bool:
    """完成请求（满员时自动调用）"""
    db_request = db.query(models.Request).filter(models.Request.id == request_id).first()
    if not db_request:
        return False
    
    db_request.status = "completed" # type: ignore
    db.commit()
    return True

# ========== Pickup CRUD ==========
def create_pickup(db: Session, pickup: schemas.PickupCreate) -> models.Pickup | None:
    """创建接取记录"""
    # 检查请求是否存在且活跃
    db_request = get_request(db, pickup.request_id)
    if not db_request:
        return None
    
    # 检查是否已满员
    if db_request.current_people >= db_request.max_people: # type: ignore
        return None
    
    # 检查是否已接取过
    existing = db.query(models.Pickup).filter(
        models.Pickup.request_id == pickup.request_id,
        models.Pickup.user_id == pickup.user_id
    ).first()
    if existing:
        return None
    
    # 创建接取记录
    db_pickup = models.Pickup(
        request_id=pickup.request_id,
        user_id=pickup.user_id,
        user_name=pickup.user_name,
        user_phone=pickup.user_phone
    )
    db.add(db_pickup)
    
    # 增加请求的当前人数
    db_request.current_people += 1 # type: ignore
    db.commit()
    db.refresh(db_pickup)
    
    # 如果满员，自动完成请求
    if db_request.current_people >= db_request.max_people: # type: ignore
        complete_request(db, db_request.id) # type: ignore
    
    return db_pickup

def get_user_pickups(
    db: Session, 
    user_id: str,
    skip: int = 0,
    limit: int = 100
) -> List[models.Pickup]:
    """获取用户的接取记录"""
    return db.query(models.Pickup).filter(
        models.Pickup.user_id == user_id
    ).order_by(models.Pickup.picked_at.desc()).offset(skip).limit(limit).all()

def get_user_pickups_with_requests(
    db: Session, 
    user_id: str
) -> List[dict]:
    """获取用户的接取记录（包含请求详情）"""
    results = db.query(
        models.Pickup,
        models.Request
    ).join(
        models.Request,
        models.Pickup.request_id == models.Request.id
    ).filter(
        models.Pickup.user_id == user_id
    ).order_by(
        models.Pickup.picked_at.desc()
    ).all()
    
    return [
        {
            "id": pickup.id,
            "request_id": pickup.request_id,
            "user_id": pickup.user_id,
            "user_name": pickup.user_name,
            "user_phone": pickup.user_phone,
            "picked_at": pickup.picked_at,
            "product_name": request.product_name,
            "product_url": request.product_url,
            "publisher_phone": request.phone,
            "publisher_qq": request.qq,
            "publisher_name": request.publisher_name,
        }
        for pickup, request in results
    ]

def check_user_picked(db: Session, request_id: int, user_id: str) -> bool:
    """检查用户是否已接取某请求"""
    return db.query(models.Pickup).filter(
        models.Pickup.request_id == request_id,
        models.Pickup.user_id == user_id
    ).first() is not None

def get_pickup_count_by_request(db: Session, request_id: int) -> int:
    """获取某请求的接取人数"""
    return db.query(models.Pickup).filter(
        models.Pickup.request_id == request_id
    ).count()