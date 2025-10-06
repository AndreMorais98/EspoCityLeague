# 🚀 Espo City League Backend

<div align="center">

**FastAPI Backend for Espo City League Football Prediction Platform**

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![SQLModel](https://img.shields.io/badge/SQLModel-FF6B6B?style=for-the-badge&logo=sqlmodel&logoColor=white)](https://sqlmodel.tiangolo.com/)

</div>

## 📋 Table of Contents

- [🎯 Overview](#-overview)
- [🏗️ Architecture](#️-architecture)
- [🚀 Quick Start](#-quick-start)
- [📁 Project Structure](#-project-structure)
- [🔧 API Endpoints](#-api-endpoints)
- [🗄️ Database Models](#️-database-models)
- [🔐 Authentication](#-authentication)
- [🧪 Testing](#-testing)
- [📦 Deployment](#-deployment)
- [🛠️ Development](#️-development)

## 🎯 Overview

The Espo City League backend is a modern REST API built with FastAPI that powers the football prediction platform. It provides secure authentication, match management, prediction handling, and real-time scoring calculations.

### 🌟 Key Features

- **FastAPI Framework**: High-performance async API with automatic OpenAPI documentation
- **JWT Authentication**: Secure token-based authentication system
- **SQLModel ORM**: Type-safe database operations with automatic validation
- **PostgreSQL Database**: Robust relational database with migrations
- **Admin Panel Support**: Role-based access control for administrators
- **Real-time Scoring**: Automatic point calculation for predictions
- **Comprehensive Testing**: Unit and integration tests with pytest

## 🏗️ Architecture

```
backend/
├── app/
│   ├── models/          # SQLModel database models
│   │   ├── user.py      # User model and schemas
│   │   ├── team.py      # Team model and schemas
│   │   ├── stage.py     # Stage model and schemas
│   │   ├── match.py     # Match model and schemas
│   │   └── bet.py       # Bet (prediction) model and schemas
│   ├── routers/         # API route handlers
│   │   ├── auth.py      # Authentication endpoints
│   │   ├── users.py     # User management endpoints
│   │   ├── teams.py     # Team endpoints
│   │   ├── stages.py    # Stage endpoints
│   │   ├── matches.py   # Match endpoints
│   │   └── bets.py      # Prediction endpoints
│   ├── dependencies/    # Dependency injection
│   │   ├── auth.py      # Authentication dependencies
│   │   └── database.py  # Database session management
│   ├── db/             # Database configuration
│   │   └── database.py  # Database connection setup
│   └── main.py         # FastAPI application entry point
├── alembic/            # Database migrations
│   ├── versions/       # Migration files
│   └── env.py         # Alembic configuration
├── tests/              # Test files
├── requirements.txt    # Python dependencies
└── .env.example       # Environment variables template
```

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- PostgreSQL 13+
- pip (Python package manager)

### 1. Environment Setup
```bash
# Clone the repository
git clone https://github.com/yourusername/espo-city-league.git
cd espo-city-league/backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Database Setup
```bash
# Create PostgreSQL database
createdb espo_city_league

# Set up environment variables
cp .env.example .env
# Edit .env with your database credentials:
# DATABASE_URL=postgresql://username:password@localhost/espo_city_league
# SECRET_KEY=your-secret-key-here
```

### 3. Run Migrations
```bash
# Run database migrations
alembic upgrade head
```

### 4. Start Development Server
```bash
# Start the FastAPI server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 5. Access the API
- **API**: http://localhost:8000
- **Interactive Docs**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 📁 Project Structure

### Models (`app/models/`)
- **`user.py`**: User authentication and profile management
- **`team.py`**: Football team information and metadata
- **`stage.py`**: Matchday/stage organization
- **`match.py`**: Match details, results, and scheduling
- **`bet.py`**: User predictions and scoring logic

### Routers (`app/routers/`)
- **`auth.py`**: Login, registration, and token management
- **`users.py`**: User profile and management endpoints
- **`teams.py`**: Team information endpoints
- **`stages.py`**: Stage and matchday endpoints
- **`matches.py`**: Match management and results
- **`bets.py`**: Prediction creation and management

### Dependencies (`app/dependencies/`)
- **`auth.py`**: JWT token validation and user authentication
- **`database.py`**: Database session management and connection pooling

## 🔧 API Endpoints

### 🔐 Authentication
```http
POST /auth/login          # User login
POST /auth/register       # User registration
POST /auth/logout         # User logout
```

### 👥 Users
```http
GET  /users/me            # Get current user profile
PUT  /users/me            # Update current user profile
GET  /users/              # List all users (admin only)
```

### ⚽ Matches
```http
GET   /matches/           # List all matches
GET   /matches/{id}       # Get match details
POST  /matches/           # Create new match (admin)
PUT   /matches/{id}       # Update match (admin)
PATCH /matches/{id}/scores # Update match scores (admin)
```

### 🎯 Predictions (Bets)
```http
GET    /bets/             # List user's predictions
POST   /bets/             # Create new prediction
GET    /bets/{id}         # Get prediction details
PATCH  /bets/{id}         # Update existing prediction
DELETE /bets/{id}         # Delete prediction
```

### 🏆 Stages
```http
GET /stages/              # List all stages
GET /stages/{id}          # Get stage details
GET /stages/{id}/matches  # Get stage matches
GET /stages/{id}/bets     # Get stage predictions
```

### 🏟️ Teams
```http
GET  /teams/              # List all teams
GET  /teams/{id}          # Get team details
POST /teams/              # Create new team (admin)
```

## 🗄️ Database Models

### User Model
```python
class User(SQLModel, table=True):
    id: int = Field(primary_key=True)
    username: str = Field(unique=True, index=True)
    email: str = Field(unique=True, index=True)
    hashed_password: str
    is_superuser: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
```

### Match Model
```python
class Match(SQLModel, table=True):
    id: int = Field(primary_key=True)
    home_team_id: int = Field(foreign_key="teams.id")
    away_team_id: int = Field(foreign_key="teams.id")
    stage_id: int = Field(foreign_key="stages.id")
    kickoff_at: datetime = Field(index=True)
    home_score: Optional[int] = None
    away_score: Optional[int] = None
    place: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
```

### Bet (Prediction) Model
```python
class Bet(SQLModel, table=True):
    id: int = Field(primary_key=True)
    user_id: int = Field(foreign_key="users.id")
    match_id: int = Field(foreign_key="matches.id")
    home_score_prediction: int
    away_score_prediction: int
    points_awarded: int = Field(default=0)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
```

## 🔐 Authentication

### JWT Token System
- **Access Token**: Short-lived (24 hours) for API access
- **Token Validation**: Automatic validation on protected endpoints
- **Password Hashing**: Secure bcrypt hashing for passwords
- **Role-based Access**: Admin and user role separation

### Authentication Flow
1. User provides username/password
2. Server validates credentials
3. JWT token generated and returned
4. Client includes token in Authorization header
5. Server validates token on each request

### Example Usage
```python
# Login request
{
    "username": "user",
    "password": "password123"
}

# Response
{
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "token_type": "bearer",
    "user": {
        "id": 1,
        "username": "user",
        "email": "user@example.com",
        "is_superuser": false
    }
}
```

## 🧪 Testing

### Running Tests
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app --cov-report=html

# Run specific test file
pytest tests/test_auth.py

# Run with verbose output
pytest -v
```

### Test Structure
```python
# tests/test_auth.py
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_login_success():
    """Test successful user login."""
    response = client.post("/auth/login", json={
        "username": "testuser",
        "password": "testpass"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_login_invalid_credentials():
    """Test login with invalid credentials."""
    response = client.post("/auth/login", json={
        "username": "testuser",
        "password": "wrongpass"
    })
    assert response.status_code == 401
```

### Test Database
- Uses separate test database
- Automatic cleanup after tests
- Fixtures for common test data
- Mock external dependencies

## 📦 Deployment

### Environment Variables
```bash
DB_NAME=DB_NAME
DB_USER=DB_USER
DB_PASSWORD=DB_PASSWORD
DB_HOST=DB_HOST
DB_PORT=DB_PORT

ADMIN_USERNAME=ADMIN_USERNAME
ADMIN_PHONE=ADMIN_PHONE
ADMIN_PASSWORD=ADMIN_PASSWORD

JWT_SECRET=JWT_SECRET
```

### Docker Deployment
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Production Considerations
- Use environment variables for configuration
- Set up proper logging
- Configure CORS for your frontend domain
- Use HTTPS in production
- Set up database connection pooling
- Configure rate limiting
- Set up monitoring and health checks

## 🛠️ Development

### Code Quality Tools
```bash
# Format code
black .

# Sort imports
isort .

# Type checking
mypy .

# Lint code
flake8 .
```

### Database Migrations
```bash
# Create new migration
alembic revision --autogenerate -m "Description of changes"

# Apply migrations
alembic upgrade head

# Rollback migration
alembic downgrade -1
```

### Development Server
```bash
# Start with auto-reload
uvicorn app.main:app --reload

# Start with specific host/port
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

# Start with debug mode
uvicorn app.main:app --reload --log-level debug
```

### API Documentation
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI JSON**: http://localhost:8000/openapi.json

## 🔧 Configuration

### Database Configuration
```python
# app/db/database.py
from sqlmodel import SQLModel, create_engine
from app.core.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG,  # Log SQL queries in debug mode
    pool_pre_ping=True,   # Verify connections before use
    pool_recycle=300,     # Recycle connections every 5 minutes
)
```

### CORS Configuration
```python
# app/main.py
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## 📚 Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLModel Documentation](https://sqlmodel.tiangolo.com/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Alembic Documentation](https://alembic.sqlalchemy.org/)
- [Pytest Documentation](https://docs.pytest.org/)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Run the test suite
6. Submit a pull request

For detailed contribution guidelines, see [CONTRIBUTING.md](../CONTRIBUTING.md).

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.

---

<div align="center">

**Built with ❤️ using FastAPI**

[Report Bug](https://github.com/yourusername/espo-city-league/issues) · [Request Feature](https://github.com/yourusername/espo-city-league/issues)

</div>