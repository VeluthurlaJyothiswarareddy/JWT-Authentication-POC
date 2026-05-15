from datetime import datetime, timedelta
import logging
from jose import JWTError, jwt
from passlib.context import CryptContext
from config import settings
from models.user import TokenData

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.access_token_expire_minutes)
    to_encode.update({"exp": expire, "type": "access"})
    encoded_jwt = jwt.encode(to_encode, settings.private_key, algorithm=settings.algorithm)
    print(f"Created access token for {data.get('sub')} and private key: {settings.private_key}")  # Debugging line
    return encoded_jwt

def create_refresh_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=settings.refresh_token_expire_days)
    to_encode.update({"exp": expire, "type": "refresh"})
    encoded_jwt = jwt.encode(to_encode, settings.private_key, algorithm=settings.algorithm)
    return encoded_jwt

def verify_token(token: str, token_type: str = "access"):
    try:
        payload = jwt.decode(token, settings.public_key, algorithms=[settings.algorithm])
        username: str = payload.get("sub")
        email: str = payload.get("email")
        token_type_claim: str = payload.get("type")
        print(f"Decoded token for {username} with email {email} and type {token_type_claim} and public key: {settings.public_key}")  # Debugging line 
        if username is None or token_type_claim != token_type:
            return None
        return TokenData(username=username, email=email)
    except JWTError:
        return None