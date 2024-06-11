from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URI: str
    SECRETE_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    if DATABASE_URI.startswith("postgres://"):
        DATABASE_URI = DATABASE_URI.replace("postgres://", "postgresql://", 1)
    DATABASE_URI

    class Config:
        env_file = ".env"


settings = Settings()
