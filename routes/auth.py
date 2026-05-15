from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from models.user import UserCreate, UserLogin, Token, UserInDB
from utils.auth import get_password_hash, verify_password, create_access_token, create_refresh_token, verify_token
from database import users_collection
from bson import ObjectId
import logging

router = APIRouter()
security = HTTPBearer()

@router.post("/register", response_model=dict)
async def register(user: UserCreate):
    # Check if user exists
    existing_user = users_collection.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    existing_username = users_collection.find_one({"username": user.username})
    if existing_username:
        raise HTTPException(status_code=400, detail="Username already taken")
    
    hashed_password = get_password_hash(user.password)
    user_dict = {
        "username": user.username,
        "email": user.email,
        "hashed_password": hashed_password
    }
    users_collection.insert_one(user_dict)
    return {"message": "User registered successfully"}

@router.post("/login", response_model=Token)
async def login(user: UserLogin):
    db_user = users_collection.find_one({"email": user.email})
    if not db_user or not verify_password(user.password, db_user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token = create_access_token(data={"sub": db_user["username"], "email": db_user["email"]})
    refresh_token = create_refresh_token(data={"sub": db_user["username"], "email": db_user["email"]})
    return Token(access_token=access_token, refresh_token=refresh_token)

@router.post("/logout")
async def logout(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    token_data = verify_token(token, "access")
    if not token_data:
        raise HTTPException(status_code=401, detail="Invalid token")
    # In a real app, you might blacklist the token, but for POC, just verify
    return {"message": "Logged out successfully"}