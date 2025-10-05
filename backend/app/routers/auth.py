from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlmodel import Session, select
from app.db import get_session
from app.models.user import User
from app.security import verify_password, create_access_token, hash_password
from app.dependencies import get_current_user

router = APIRouter(prefix="/auth", tags=["auth"])


class LoginRequest(BaseModel):
    username: str
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    phone: str
    score: int
    is_active: bool
    is_superuser: bool

    class Config:
        from_attributes = True


class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserResponse


class UpdateUserRequest(BaseModel):
    username: str | None = None
    phone: str | None = None
    password: str | None = None


@router.post("/login", response_model=LoginResponse)
def login(payload: LoginRequest, session: Session = Depends(get_session)) -> LoginResponse:
    user = session.exec(select(User).where(User.username == payload.username)).first()
    if not user or not verify_password(payload.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_access_token(sub=str(user.id), extra={"username": user.username, "phone": user.phone})
    
    return LoginResponse(
        access_token=token,
        user=UserResponse(
            id=user.id,
            username=user.username,
            phone=user.phone,
            score=user.score,
            is_active=user.is_active,
            is_superuser=user.is_superuser
        )
    )


@router.get("/me", response_model=UserResponse)
def get_current_user_info(current_user: User = Depends(get_current_user)) -> UserResponse:
    return UserResponse(
        id=current_user.id,
        username=current_user.username,
        phone=current_user.phone,
        score=current_user.score,
        is_active=current_user.is_active,
        is_superuser=current_user.is_superuser
    )


@router.put("/me", response_model=UserResponse)
def update_current_user(
    update_data: UpdateUserRequest,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
) -> UserResponse:
    # Check if username is being updated and if it's already taken
    if update_data.username and update_data.username != current_user.username:
        existing_user = session.exec(select(User).where(User.username == update_data.username)).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Username already taken")
        current_user.username = update_data.username

    # Update phone if provided
    if update_data.phone:
        current_user.phone = update_data.phone

    # Update password if provided
    if update_data.password:
        current_user.hashed_password = hash_password(update_data.password)

    # Save changes to database
    session.add(current_user)
    session.commit()
    session.refresh(current_user)

    return UserResponse(
        id=current_user.id,
        username=current_user.username,
        phone=current_user.phone,
        score=current_user.score,
        is_active=current_user.is_active,
        is_superuser=current_user.is_superuser
    )
