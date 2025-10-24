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
- [📦 Deployment](#-deployment)
- [🛠️ Development](#️-development)
- [📄 License](#-license)

## 🎯 Overview

The Espo City League backend is a modern REST API built with FastAPI that powers the football prediction platform. It provides secure authentication, match management, prediction handling, and real-time scoring calculations.

### 🌟 Key Features

- **FastAPI Framework**: High-performance async API with automatic OpenAPI documentation
- **JWT Authentication**: Secure token-based authentication system
- **SQLModel ORM**: Type-safe database operations with automatic validation
- **PostgreSQL Database**: Robust relational database with migrations
- **Admin Panel Support**: Role-based access control for administrators
- **Real-time Scoring**: Automatic point calculation for predictions
- **Tie-Breaking System**: Advanced leaderboard ranking with multiple criteria
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
│   │   ├── bets.py      # Prediction endpoints
│   │   └── leaderboard.py # Leaderboard and tie-breaking endpoints
│   ├── services/        # Business logic services
│   │   └── tie_breaking.py # Tie-breaking statistics calculation
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
docker-compose up --build
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

#### Local Development
- **API Base**: http://localhost:8000/api
- **Interactive Docs**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

#### Production Server
- **Live API**: https://espocity-league.mooo.com/api
- **Live Frontend**: https://espocity-league.mooo.com

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
- **`leaderboard.py`**: User rankings and tie-breaking statistics

### Services (`app/services/`)
- **`tie_breaking.py`**: Advanced tie-breaking logic and statistics calculation

### Dependencies (`app/dependencies/`)
- **`auth.py`**: JWT token validation and user authentication
- **`database.py`**: Database session management and connection pooling

## 🔧 API Endpoints

### 🔐 Authentication
```http
POST /api/auth/login      # User login
GET  /api/auth/me         # Get current user profile
PUT  /api/auth/me         # Update current user profile
```

### ⚽ Matches
```http
GET   /api/matches/           # List all matches
GET   /api/matches/{id}       # Get match details
POST  /api/matches/           # Create new match (admin)
PUT   /api/matches/{id}       # Update match (admin)
PATCH /api/matches/{id}/scores # Update match scores (admin)
```

### 🎯 Predictions (Bets)
```http
GET    /api/bets/             # List all bets
POST   /api/bets/             # Create new prediction
GET    /api/bets/{id}         # Get prediction details
PATCH  /api/bets/{id}         # Update existing prediction
GET    /api/bets/user/{user_id} # Get user predictions
```

### 🏆 Stages
```http
GET  /api/stages/              # List all stages
POST /api/stages/              # Create new stage (admin)
GET  /api/stages/{id}          # Get stage details
PUT  /api/stages/{id}          # Update stage (admin)
DEL  /api/stages/{id}          # Delete stage (admin)
GET  /api/stages/{id}/matches  # Get stage matches
GET  /api/stages/{id}/bets     # Get stage predictions
```

### 🏟️ Teams
```http
GET  /api/teams/              # List all teams
GET  /api/teams/{id}          # Get team details
POST /api/teams/              # Create new team (admin)
```

### 🏅 Leaderboard
```http
GET  /api/leaderboard/         # Get user rankings with tie-breaking
POST /api/leaderboard/update-stats # Update tie-breaking statistics (admin)
```

### ❤️ Health
```http
GET /api/health               # API health check
```

## 🗄️ Database Models

### User Model
```python
class User(SQLModel, table=True):
    id: int = Field(primary_key=True)
    username: str = Field(unique=True, index=True)
    phone: str = Field(unique=True, index=True)
    hashed_password: str
    is_active: bool = Field(default=True)
    is_superuser: bool = Field(default=False)
    score: int = Field(default=0)
    correct_results: int = Field(default=0)      # Exact score predictions
    lone_wolf_victories: int = Field(default=0)  # Unique correct predictions
    defeats: int = Field(default=0)              # Games with 0 points
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

## 🏆 Tie-Breaking System

### Ranking Criteria
The leaderboard uses a sophisticated tie-breaking system when users have the same score:

1. **Correct Results** (Exact Score Predictions)
   - Counts predictions where both home and away scores match exactly
   - Higher count ranks higher

2. **Lone Wolf Victories** (Unique Correct Predictions)
   - Counts correct predictions where only that user got it right
   - Rewards bold, unique predictions
   - Higher count ranks higher

3. **Defeats** (Zero-Point Games)
   - Counts games where the user got 0 points (completely wrong result)
   - Lower count ranks higher (fewer defeats is better)

### Automatic Updates
- Tie-breaking statistics are automatically updated when match results are processed
- Admins can manually trigger updates via `/api/leaderboard/update-stats`
- Statistics are recalculated when match scores are edited

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

### Production Considerations
- Use environment variables for configuration
- Set up proper logging
- Configure CORS for your frontend domain
- Use HTTPS in production
- Set up database connection pooling
- Configure rate limiting
- Set up monitoring and health checks

## 🛠️ Development

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

**Note**: All API endpoints are prefixed with `/api`. For example:
- Login: `POST /api/auth/login`
- Get matches: `GET /api/matches/`
- Health check: `GET /api/health`

## 📚 Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLModel Documentation](https://sqlmodel.tiangolo.com/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Alembic Documentation](https://alembic.sqlalchemy.org/)
- [Pytest Documentation](https://docs.pytest.org/)


## 📄 License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.
