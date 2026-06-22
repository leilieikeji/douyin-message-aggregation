# 抖音私信聚合

一个现代化的抖音私信消息聚合平台，支持多账号管理、消息存储、数据分析和自动回复等功能。

## 🚀 主要特性

- **多账号管理**：支持多个抖音账号同时管理
- **消息聚合**：实时聚合来自不同账号的私信
- **智能分类**：自动分类和标签管理
- **数据分析**：消息统计、趋势分析
- **自动回复**：支持模板和关键词回复
- **数据导出**：支持多种格式导出
- **用户友好的UI**：现代化的网页后台管理界面

## 📦 技术栈

### 后端
- **框架**：FastAPI (Python 3.9+)
- **数据库**：MongoDB
- **缓存**：Redis
- **异步**：Celery + Redis
- **服务器**：Uvicorn

### 前端
- **框架**：React 18 + TypeScript
- **UI库**：Ant Design
- **状态管理**：Redux Toolkit
- **HTTP**：Axios

### DevOps
- **容器**：Docker + Docker Compose
- **CI/CD**：GitHub Actions

## 🏃 快速启动

### 前置要求

- Docker & Docker Compose
- Git

### 启动步骤

```bash
# 1. 克隆项目
git clone https://github.com/leilieikeji/douyin-message-aggregation.git
cd douyin-message-aggregation

# 2. 启动所有服务
docker-compose up -d

# 3. 初始化数据库
sleep 10  # 等待服务启动

# 4. 访问应用
# 前端：http://localhost:3000
# API文档：http://localhost:8000/docs
# 健康检查：http://localhost:8000/health
```

### 本地开发

**后端开发**：

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

**前端开发**：

```bash
cd frontend
npm install
cp .env.example .env
npm start
```

## 📚 API 文档

启动后端服务后，访问 `http://localhost:8000/docs` 查看完整的 Swagger API 文档。

### 主要端点

#### 账户管理
- `POST /api/v1/accounts` - 创建账户
- `GET /api/v1/accounts` - 获取账户列表
- `GET /api/v1/accounts/{id}` - 获取账户详情
- `PUT /api/v1/accounts/{id}` - 更新账户
- `DELETE /api/v1/accounts/{id}` - 删除账户

#### 消息管理
- `GET /api/v1/messages` - 获取消息列表
- `GET /api/v1/messages/{id}` - 获取消息详情
- `POST /api/v1/messages/search` - 搜索消息
- `POST /api/v1/messages/{id}/reply` - 回复消息

#### 数据分析
- `GET /api/v1/analytics/summary` - 获取统计摘要
- `GET /api/v1/analytics/messages/trends` - 消息趋势
- `GET /api/v1/analytics/accounts/stats` - 账户统计

#### 自动回复
- `GET /api/v1/auto-reply/rules` - 获取回复规则
- `POST /api/v1/auto-reply/rules` - 创建规则
- `PUT /api/v1/auto-reply/rules/{id}` - 更新规则
- `DELETE /api/v1/auto-reply/rules/{id}` - 删除规则

## 🐳 Docker 服务

项目包含以下 Docker 服务：

| 服务 | 端口 | 说明 |
|------|------|------|
| MongoDB | 27017 | 数据库 |
| Redis | 6379 | 缓存 |
| Backend | 8000 | 后端 API |
| Frontend | 3000 | 前端应用 |

## 📁 项目结构

```
douyin-message-aggregation/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── v1/
│   │   │   │   ├── accounts.py
│   │   │   │   ├── messages.py
│   │   │   │   ├── analytics.py
│   │   │   │   └── auto_reply.py
│   │   │   └── router.py
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── tasks/
│   │   ├── middleware/
│   │   ├── utils/
│   │   ├── config.py
│   │   └── main.py
│   ├── tests/
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .env.example
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── store/
│   │   ├── types/
│   │   ├── utils/
│   │   ├── App.tsx
│   │   └── index.tsx
│   ├── public/
│   ├── package.json
│   ├── Dockerfile
│   └── .env.example
├── docker-compose.yml
├── .github/
│   └── workflows/
├── .gitignore
└── README.md
```

## 🔧 环境配置

### 后端 (.env)

```env
APP_NAME=抖音私信聚合系统
DEBUG=True
SECRET_KEY=your-secret-key

MONGODB_URL=mongodb://admin:admin123@mongodb:27017
DATABASE_NAME=douyin_aggregation
REDIS_URL=redis://:redis123@redis:6379/0

DOUYIN_API_KEY=your-api-key
DOUYIN_API_SECRET=your-api-secret
```

### 前端 (.env)

```env
REACT_APP_API_URL=http://localhost:8000/api/v1
REACT_APP_WS_URL=ws://localhost:8000/ws
```

## 🧪 测试

```bash
# 后端测试
cd backend
pytest tests/ -v

# 前端测试
cd frontend
npm test
```

## 📊 监控

- **API 文档**：http://localhost:8000/docs
- **健康检查**：http://localhost:8000/health
- **MongoDB**：localhost:27017
- **Redis**：localhost:6379

## 🤝 贡献

欢迎提交 Pull Request 或报告 Issue！

## 📄 许可证

MIT License

## 👤 作者

- GitHub: [@leilieikeji](https://github.com/leilieikeji)

## 🙏 致谢

感谢所有贡献者和使用者的支持！
