#!/bin/bash

# 设置颜色输出
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}=== 开始部署前端 ===${NC}"
echo -e "${GREEN}=== frontend ===${NC}"
scp -r -P 50704 ./dist/ root@110.42.96.105:/opt/1panel/www/sites/repiece.top/frontend/dist/
echo -e "${GREEN}=== backend ===${NC}"

scp -r -P 50704 ./app/ root@110.42.96.105:/opt/1panel/www/sites/repiece.top/backend/app/

