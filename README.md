# web-site

This template should help get you started developing with Vue 3 in Vite.

### Running
```sh
# 启动带参数的应用
pm2 start "uvicorn main:app --host 0.0.0.0 --port 8000" --name shipping-api

# 启动 serve 静态服务
pm2 start serve -- -- -s . -l 8080 --name frontend
```

## Project Setup

```sh
# 安装 nvm
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash

# 安装完成后，重新打开终端或执行
source ~/.bashrc

# 查看可安装的 Node.js 版本
nvm list-remote

# 安装最新 LTS 版本
nvm install --lts

# 或安装指定版本
nvm install 18.19.0
nvm install 20.11.0

# 查看已安装的版本
nvm list

# 切换版本
nvm use 18

# 设置默认版本
nvm alias default 18

# 验证
node -v
npm -v
```


### SetUp fastapi
```sh
# 安装 FastAPI 和服务器
pip install fastapi uvicorn

# 可选：自动 API 文档需要的依赖
pip install python-multipart

# 数据库驱动（你项目用 MySQL）
pip install mysql-connector-python
```
### pm2 Usage
```sh
# 查看所有进程
pm2 status
pm2 list
pm2 ls

# 查看详细信息
pm2 show shipping-api

# 停止进程
pm2 stop shipping-api      # 停止指定进程
pm2 stop all               # 停止所有进程

# 重启进程
pm2 restart shipping-api   # 重启指定进程
pm2 restart all            # 重启所有进程

# 删除进程
pm2 delete shipping-api    # 删除指定进程
pm2 delete all             # 删除所有进程

# 重载进程（0秒停机重启）
pm2 reload all
```

