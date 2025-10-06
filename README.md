# ⚽ Espo City League

<div align="center">

![Espo City League Logo](frontend/public/images/symbol.png)

**A modern football prediction league platform built with FastAPI and React**

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)](https://reactjs.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)

</div>

## 📋 Table of Contents

- [🎯 Overview](#-overview)
- [✨ Features](#-features)
- [🏗️ Architecture](#️-architecture)
- [🚀 Quick Start](#-quick-start)
- [📁 Project Structure](#-project-structure)
- [🔧 API Documentation](#-api-documentation)
- [🎮 Usage Guide](#-usage-guide)
- [👥 User Roles](#-user-roles)
- [🏆 Scoring System](#-scoring-system)
- [🛠️ Development](#️-development)
- [📦 Deployment](#-deployment)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

## 🎯 Overview

Espo City League is a comprehensive football prediction platform where users can make predictions on UEFA matches and compete with friends. The platform features real-time match updates, leaderboards, and an intuitive admin panel for match management.

### 🌟 Key Highlights

- **Real-time Predictions**: Make predictions before matches start
- **Smart Scoring System**: Points based on prediction accuracy
- **Dynamic Leaderboards**: Track your performance against other players
- **Admin Dashboard**: Manage matches and update results
- **Responsive Design**: Works seamlessly on desktop and mobile
- **Collapsible Sidebar**: Space-efficient navigation

## ✨ Features

### 🎮 User Features
- **Match Predictions**: Predict home and away team scores
- **Real-time Updates**: See match results as they happen
- **Personal Dashboard**: Track your prediction history
- **Community View**: See other players' predictions
- **Leaderboard**: Compete with friends and track rankings
- **Profile Management**: Update your account information

### 👨‍💼 Admin Features
- **Match Management**: Create and update match results
- **User Management**: View and manage user accounts
- **Stage Organization**: Organize matches by stages/matchdays
- **Real-time Scoring**: Automatic point calculation
- **Data Analytics**: Track platform usage and engagement

### 🎨 UI/UX Features
- **Modern Design**: Clean, intuitive interface
- **Dark Theme**: Easy on the eyes with professional styling
- **Collapsible Sidebar**: Maximize content space when needed
- **Responsive Layout**: Optimized for all screen sizes
- **Smooth Animations**: Polished user experience
- **Tooltips & Help**: Contextual guidance throughout the app

## 🏗️ Architecture

### Backend (FastAPI)
```
backend/
├── app/
│   ├── models/          # SQLModel database models
│   ├── routers/         # API route handlers
│   ├── dependencies/    # Authentication & database
│   └── db/             # Database configuration
├── alembic/            # Database migrations
└── requirements.txt    # Python dependencies
```

### Frontend (React + TypeScript)
```
frontend/
├── src/
│   ├── components/     # Reusable UI components
│   ├── pages/         # Page components
│   ├── contexts/      # React context providers
│   ├── services/      # API service layer
│   ├── utils/         # Utility functions
│   └── styles/        # Global styles
├── public/            # Static assets
└── package.json       # Node.js dependencies
```

### Database Schema
- **Users**: Authentication and profile data
- **Teams**: Football team information
- **Stages**: Matchday/stage organization
- **Matches**: Match details and results
- **Bets**: User predictions and scoring

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Node.js 16+
- PostgreSQL 13+
- Docker (optional)

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/espo-city-league.git
cd espo-city-league
```

### 2. Backend Setup
```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your database credentials

# Run database migrations
alembic upgrade head

# Start the development server
uvicorn app.main:app --reload
```

### 3. Frontend Setup
```bash
cd frontend

# Install dependencies
npm install

# Start the development server
npm start
```

### 4. Access the Application
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

## 📁 Project Structure

```
espo-city-league/
├── 📁 backend/                 # FastAPI backend
│   ├── 📁 app/
│   │   ├── 📁 models/         # Database models
│   │   ├── 📁 routers/        # API endpoints
│   │   ├── 📁 dependencies/   # Auth & DB deps
│   │   └── 📁 db/            # Database config
│   ├── 📁 alembic/           # Database migrations
│   └── 📄 requirements.txt   # Python deps
├── 📁 frontend/               # React frontend
│   ├── 📁 src/
│   │   ├── 📁 components/    # UI components
│   │   ├── 📁 pages/        # Page components
│   │   ├── 📁 contexts/     # React contexts
│   │   ├── 📁 services/     # API services
│   │   └── 📁 utils/        # Utilities
│   └── 📄 package.json      # Node deps
├── 📁 docs/                  # Documentation
└── 📄 README.md             # This file
```

## 🔧 API Documentation

### Authentication Endpoints
- `POST /auth/login` - User login
- `POST /auth/register` - User registration
- `POST /auth/logout` - User logout

### Match Endpoints
- `GET /matches/` - List all matches
- `GET /matches/{id}` - Get match details
- `PATCH /matches/{id}/scores` - Update match scores (admin)

### Prediction Endpoints
- `POST /bets/` - Create new prediction
- `PATCH /bets/{id}` - Update existing prediction
- `GET /bets/user/{user_id}` - Get user predictions

### Stage Endpoints
- `GET /stages/` - List all stages
- `GET /stages/{id}/matches` - Get stage matches
- `GET /stages/{id}/bets` - Get stage predictions

## 🎮 Usage Guide

### Making Predictions
1. Navigate to "My Predictions" in the sidebar
2. Select a stage/matchday
3. Click "Predict" on upcoming matches
4. Enter your predicted scores
5. Click "Save" to submit

### Viewing Results
1. Go to "My Predictions" to see your history
2. Check "Community Predictions" to see others' picks
3. Visit "Rankings" to see the leaderboard
4. Points are automatically calculated when matches finish

### Admin Functions
1. Access "Manage Matches" (admin only)
2. Select a stage to view matches
3. Click "Add Score" or "Edit" to update results
4. Scores are automatically saved and points calculated

## 👥 User Roles

### 🎯 Player
- Make predictions on upcoming matches
- View personal prediction history
- See community predictions
- Track leaderboard rankings
- Update profile information

### 👨‍💼 Administrator
- All player features
- Update match results
- Manage match schedules
- View all user data
- Access admin dashboard

## 🏆 Scoring System

The platform uses a color-coded scoring system:

| Result | Points | Description |
|--------|--------|-------------|
| 🟢 **GREEN** | **3 points** | Exact score match |
| 🟡 **YELLOW** | **1 point** | Correct result (win/draw/loss) but wrong score |
| 🔴 **RED** | **0 points** | Wrong result |

### Example Scoring
- **Prediction**: Arsenal 2-1 Chelsea
- **Actual**: Arsenal 2-1 Chelsea → **3 points** (GREEN)
- **Actual**: Arsenal 3-0 Chelsea → **1 point** (YELLOW - correct Arsenal win)
- **Actual**: Chelsea 1-0 Arsenal → **0 points** (RED - wrong result)

## 🛠️ Development

### Backend Development
```bash
cd backend

# Run tests
pytest

# Format code
black .

# Type checking
mypy .

# Database migration
alembic revision --autogenerate -m "Description"
alembic upgrade head
```

### Frontend Development
```bash
cd frontend

# Run tests
npm test

# Build for production
npm run build

# Lint code
npm run lint

# Type checking
npm run type-check
```

### Code Quality
- **Backend**: Black, MyPy, Pytest
- **Frontend**: ESLint, Prettier, TypeScript
- **Database**: Alembic migrations
- **API**: FastAPI automatic documentation

## 📦 Deployment

### Docker Deployment
```bash
# Build and run with Docker Compose
docker-compose up --build

# Production deployment
docker-compose -f docker-compose.prod.yml up -d
```

### Manual Deployment
1. **Backend**: Deploy to your preferred Python hosting (Railway, Heroku, etc.)
2. **Frontend**: Build and deploy to Vercel, Netlify, or similar
3. **Database**: Set up PostgreSQL instance
4. **Environment**: Configure production environment variables

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Development Guidelines
- Follow existing code style and patterns
- Write tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **FastAPI** - Modern, fast web framework for building APIs
- **React** - A JavaScript library for building user interfaces
- **PostgreSQL** - The world's most advanced open source relational database
- **UEFA** - For providing the football match data inspiration

---

<div align="center">

**Made with ❤️ by the Espo City League Team**

[Report Bug](https://github.com/yourusername/espo-city-league/issues) · [Request Feature](https://github.com/yourusername/espo-city-league/issues) · [Documentation](https://github.com/yourusername/espo-city-league/wiki)

</div>