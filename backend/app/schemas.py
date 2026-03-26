from pydantic import BaseModel, Field, HttpUrl
from datetime import datetime
from typing import Optional

# ========== Request 相关 Schema ==========
class RequestBase(BaseModel):
    product_name: str = Field(..., max_length=200, description="商品名称")
    product_url: str = Field(..., max_length=500, description="商品链接")
    max_people: int = Field(1, ge=1, le=100, description="接取上限人数")
    phone: str = Field(..., max_length=20, description="发布者手机号")
    qq: str = Field(..., max_length=20, description="发布者QQ")
    priority: int = Field(0, ge=0, le=2, description="优先级: 0普通,1紧急,2特急")
    description: Optional[str] = Field(None, description="详细说明")
    publisher_name: Optional[str] = Field(None, max_length=50, description="发布者称呼")
    publisher_id: Optional[str] = Field(None, max_length=50, description="发布者标识")

class RequestCreate(RequestBase):
    pass

class RequestUpdate(BaseModel):
    max_people: Optional[int] = Field(None, ge=1, le=100)
    priority: Optional[int] = Field(None, ge=0, le=2)
    description: Optional[str] = None

class RequestResponse(RequestBase):
    id: int
    current_people: int
    status: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

# ========== Pickup 相关 Schema ==========
class PickupBase(BaseModel):
    request_id: int
    user_id: str = Field(..., max_length=50, description="接取者唯一标识")
    user_name: Optional[str] = Field(None, max_length=50)
    user_phone: Optional[str] = Field(None, max_length=20)

class PickupCreate(PickupBase):
    pass

class PickupResponse(BaseModel):
    id: int
    request_id: int
    user_id: str
    user_name: Optional[str]
    user_phone: Optional[str]
    picked_at: datetime
    
    class Config:
        from_attributes = True

# 带请求详情的接取记录
class PickupWithRequest(PickupResponse):
    request: RequestResponse

# ========== 通用响应 ==========
class MessageResponse(BaseModel):
    message: str
    success: bool = True

class ErrorResponse(BaseModel):
    detail: str
    success: bool = False