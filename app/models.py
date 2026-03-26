from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Index
from sqlalchemy.sql import func
from app.database import Base

class Request(Base):
    """拼单请求模型"""
    __tablename__ = "requests"
    
    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String(200), nullable=False, comment="商品名称")
    product_url = Column(String(500), nullable=False, comment="商品链接")
    max_people = Column(Integer, default=1, comment="接取上限人数")
    current_people = Column(Integer, default=1, comment="当前已接取人数")
    phone = Column(String(20), nullable=False, comment="发布者手机号")
    qq = Column(String(20), comment="发布者QQ")
    priority = Column(Integer, default=0, comment="优先级: 0普通,1紧急,2特急")
    description = Column(Text, nullable=True, comment="详细说明")
    publisher_name = Column(String(50), nullable=True, comment="发布者称呼")
    publisher_id = Column(String(50), nullable=True, comment="发布者唯一标识")
    status = Column(String(20), default="active", comment="状态: active/completed")
    created_at = Column(DateTime(timezone=True), server_default=func.now(), comment="创建时间")
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), comment="更新时间")
    
    # 索引优化
    __table_args__ = (
        Index('idx_status', 'status'),
        Index('idx_priority', 'priority'),
    )


class Pickup(Base):
    """接取记录模型"""
    __tablename__ = "pickups"
    
    id = Column(Integer, primary_key=True, index=True)
    request_id = Column(Integer, ForeignKey("requests.id", ondelete="CASCADE"), nullable=False, comment="请求ID")
    user_id = Column(String(50), nullable=False, comment="接取者唯一标识")
    user_name = Column(String(50), nullable=True, comment="接取者称呼")
    user_phone = Column(String(20), nullable=True, comment="接取者手机号")
    picked_at = Column(DateTime(timezone=True), server_default=func.now(), comment="接取时间")
    
    __table_args__ = (
        Index('idx_request_user', 'request_id', 'user_id', unique=True),  # 防止重复接取
        Index('idx_user_id', 'user_id'),
    )