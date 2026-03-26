from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.routers import requests

# 创建数据库表
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="拼单互助平台 API",
    description="帮助用户发布和接取拼单请求",
    version="1.0.0"
)

# 配置 CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # Vite 开发服务器
        "http://localhost:3000",  # 其他开发服务器
        "https://repiece.top",     # 你的生产域名
        "https://*.repiece.top",   # 子域名
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由
app.include_router(requests.router)

@app.get("/")
def root():
    return {
        "message": "拼单互助平台 API",
        "docs": "/docs",
        "version": "1.0.0"
    }