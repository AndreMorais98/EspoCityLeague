# 🔧 EspoCity League API Documentation

## Base URL
```
http://localhost:8000
```

## Authentication

All protected endpoints require a valid JWT token in the Authorization header:
```
Authorization: Bearer <your-jwt-token>
```

## 📋 Endpoints Overview

### 🔐 Authentication
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/auth/login` | User login | ❌ |
| POST | `/auth/register` | User registration | ❌ |
| POST | `/auth/logout` | User logout | ✅ |

### 👥 Users
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/users/me` | Get current user profile | ✅ |
| PUT | `/users/me` | Update current user profile | ✅ |
| GET | `/users/` | List all users (admin) | ✅ Admin |

### ⚽ Matches
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/matches/` | List all matches | ✅ |
| GET | `/matches/{id}` | Get match details | ✅ |
| POST | `/matches/` | Create new match (admin) | ✅ Admin |
| PUT | `/matches/{id}` | Update match (admin) | ✅ Admin |
| PATCH | `/matches/{id}/scores` | Update match scores (admin) | ✅ Admin |

### 🎯 Predictions (Bets)
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/bets/` | List user's predictions | ✅ |
| POST | `/bets/` | Create new prediction | ✅ |
| GET | `/bets/{id}` | Get prediction details | ✅ |
| PATCH | `/bets/{id}` | Update existing prediction | ✅ |
| DELETE | `/bets/{id}` | Delete prediction | ✅ |

### 🏆 Stages
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/stages/` | List all stages | ✅ |
| GET | `/stages/{id}` | Get stage details | ✅ |
| GET | `/stages/{id}/matches` | Get stage matches | ✅ |
| GET | `/stages/{id}/bets` | Get stage predictions | ✅ |
| POST | `/stages/` | Create new stage (admin) | ✅ Admin |

### 🏟️ Teams
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/teams/` | List all teams | ✅ |
| GET | `/teams/{id}` | Get team details | ✅ |
| POST | `/teams/` | Create new team (admin) | ✅ Admin |

## 📝 Request/Response Examples

### 🔐 Authentication

#### Login
```http
POST /auth/login
Content-Type: application/json

{
  "username": "user",
  "password": "password123"
}
```

**Response:**
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "token_type": "bearer",
  "user": {
    "id": 1,
    "username": "user",
    "email": "user@example.com",
    "is_superuser": false,
    "created_at": "2024-01-01T00:00:00Z"
  }
}
```

### ⚽ Matches

#### Get All Matches
```http
GET /matches/
Authorization: Bearer <token>
```

**Response:**
```json
[
  {
    "id": 1,
    "home_team": {
      "id": 1,
      "name": "Arsenal",
      "logo_url": "https://example.com/arsenal.png"
    },
    "away_team": {
      "id": 2,
      "name": "Chelsea",
      "logo_url": "https://example.com/chelsea.png"
    },
    "kickoff_at": "2024-01-15T15:00:00Z",
    "home_score": 2,
    "away_score": 1,
    "stage": {
      "id": 1,
      "name": "Matchday 1"
    }
  }
]
```

#### Update Match Scores (Admin)
```http
PATCH /matches/1/scores
Authorization: Bearer <admin-token>
Content-Type: application/json

{
  "home_score": 2,
  "away_score": 1
}
```

### 🎯 Predictions

#### Create Prediction
```http
POST /bets/
Authorization: Bearer <token>
Content-Type: application/json

{
  "match_id": 1,
  "home_score_prediction": 2,
  "away_score_prediction": 1
}
```

**Response:**
```json
{
  "id": 1,
  "user_id": 1,
  "match_id": 1,
  "home_score_prediction": 2,
  "away_score_prediction": 1,
  "points_awarded": 0,
  "created_at": "2024-01-01T00:00:00Z",
  "updated_at": "2024-01-01T00:00:00Z"
}
```

#### Update Prediction
```http
PATCH /bets/1
Authorization: Bearer <token>
Content-Type: application/json

{
  "home_score_prediction": 3,
  "away_score_prediction": 0
}
```

### 🏆 Stages

#### Get Stage Matches
```http
GET /stages/1/matches
Authorization: Bearer <token>
```

**Response:**
```json
[
  {
    "id": 1,
    "home_team": {
      "id": 1,
      "name": "Arsenal",
      "logo_url": "https://example.com/arsenal.png"
    },
    "away_team": {
      "id": 2,
      "name": "Chelsea",
      "logo_url": "https://example.com/chelsea.png"
    },
    "kickoff_at": "2024-01-15T15:00:00Z",
    "home_score": null,
    "away_score": null,
    "user_bet": {
      "id": 1,
      "home_score_prediction": 2,
      "away_score_prediction": 1,
      "points_awarded": 0
    }
  }
]
```

## 🚨 Error Responses

### Validation Error (400)
```json
{
  "detail": [
    {
      "loc": ["body", "home_score_prediction"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```

### Authentication Error (401)
```json
{
  "detail": "Could not validate credentials"
}
```

### Authorization Error (403)
```json
{
  "detail": "Only administrators can update match scores"
}
```

### Not Found Error (404)
```json
{
  "detail": "Match not found"
}
```

### Business Logic Error (400)
```json
{
  "detail": "Cannot update bet after match has started"
}
```

## 📊 Data Models

### User
```typescript
interface User {
  id: number;
  username: string;
  email: string;
  is_superuser: boolean;
  created_at: string;
  updated_at: string;
}
```

### Match
```typescript
interface Match {
  id: number;
  home_team: Team;
  away_team: Team;
  kickoff_at: string;
  home_score: number | null;
  away_score: number | null;
  stage: Stage;
  place?: string;
  created_at: string;
  updated_at: string;
}
```

### Bet (Prediction)
```typescript
interface Bet {
  id: number;
  user_id: number;
  match_id: number;
  home_score_prediction: number;
  away_score_prediction: number;
  points_awarded: number;
  created_at: string;
  updated_at: string;
}
```

### Stage
```typescript
interface Stage {
  id: number;
  name: string;
  date: string;
  created_at: string;
  updated_at: string;
}
```

### Team
```typescript
interface Team {
  id: number;
  name: string;
  logo_url?: string;
  stadium_name?: string;
  history?: string;
  created_at: string;
  updated_at: string;
}
```

## 🔒 Security Features

### JWT Authentication
- Tokens expire after 24 hours
- Refresh token mechanism
- Secure HTTP-only cookies (optional)

### Input Validation
- All inputs validated using Pydantic models
- SQL injection protection via SQLModel
- XSS protection through proper escaping

### Authorization
- Role-based access control (RBAC)
- Admin-only endpoints protected
- User can only access their own data

### Rate Limiting
- API rate limiting to prevent abuse
- Configurable limits per endpoint
- IP-based and user-based limiting

## 🧪 Testing

### Running Tests
```bash
# Backend tests
cd backend
pytest

# Frontend tests
cd frontend
npm test
```

### Test Coverage
- Unit tests for all business logic
- Integration tests for API endpoints
- Frontend component tests
- End-to-end tests for critical flows

## 📈 Performance

### Database Optimization
- Indexed foreign keys and search fields
- Efficient queries with proper joins
- Connection pooling for high concurrency

### Caching Strategy
- Redis caching for frequently accessed data
- API response caching
- Static asset caching

### API Performance
- Async/await for non-blocking operations
- Pagination for large datasets
- Optimized database queries

## 🔧 Configuration

### Environment Variables
```bash
# Database
DATABASE_URL=postgresql://user:password@localhost/espo_city_league

# JWT
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=1440

# CORS
ALLOWED_ORIGINS=http://localhost:3000,https://yourdomain.com

# Admin
ADMIN_USERNAME=admin
ADMIN_PASSWORD=admin_password
ADMIN_EMAIL=admin@example.com
```

## 📚 Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Documentation](https://reactjs.org/docs/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [SQLModel Documentation](https://sqlmodel.tiangolo.com/)

---

For more information, visit the [main README](README.md) or contact the development team.
