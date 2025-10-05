import os
import time
import bcrypt
import jwt

JWT_SECRET = os.getenv("JWT_SECRET")
JWT_ALG = "HS256"
JWT_EXPIRE_SECONDS = 3600


def hash_password(plain: str) -> str:
    return bcrypt.hashpw(plain.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def verify_password(plain: str, hashed: str) -> bool:
    try:
        # Ensure both are bytes for bcrypt.checkpw
        plain_bytes = plain.encode("utf-8")
        if isinstance(hashed, str):
            hashed_bytes = hashed.encode("utf-8")
        else:
            hashed_bytes = hashed
        return bcrypt.checkpw(plain_bytes, hashed_bytes)
    except Exception as e:
        print(f"Password verification error: {e}")
        return False


def create_access_token(sub: str, extra: dict | None = None) -> str:
    now = int(time.time())
    payload = {"sub": sub, "iat": now, "exp": now + JWT_EXPIRE_SECONDS}
    if extra:
        payload.update(extra)
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALG)


def decode_token(token: str) -> dict:
    return jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALG])
