from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

load_dotenv()

class Settings(BaseSettings):
    algorithm: str = "RS256"
    access_token_expire_minutes: int = 30
    refresh_token_expire_days: int = 7
    mongo_uri: str
    private_key: str = ""
    public_key: str = ""

    class Config:
        env_file = ".env"

settings = Settings()