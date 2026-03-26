#!/bin/bash

# 设置颜色输出
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}=== 开始部署前端 ===${NC}"
echo -e "${GREEN}=== frontend ===${NC}"
scp -r -P 50704 ./dist/ root@110.42.96.105:/opt/1panel/www/sites/repiece.top/frontend/
echo -e "${GREEN}=== backend ===${NC}"

# 上传到 backend 目录，让 app 文件夹成为其子目录
scp -r -P 50704 ./app root@110.42.96.105:/opt/1panel/www/sites/repiece.top/backend/
echo -e "${GREEN}=== restart ===${NC}"
ssh -p 50704 root@110.42.96.105 "pm2 restart all"