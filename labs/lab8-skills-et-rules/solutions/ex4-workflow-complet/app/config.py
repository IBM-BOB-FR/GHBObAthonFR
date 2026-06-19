"""Application configuration using Pydantic Settings."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings.

    All settings can be overridden via environment variables.
    """

    # Application
    app_name: str = "Blog API"
    app_version: str = "1.0.0"
    debug: bool = False

    # Security
    secret_key: str = "your-secret-key-change-in-production"
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    # Database
    database_url: str = "sqlite:///./blog.db"

    # CORS
    cors_origins: list[str] = ["http://localhost:3000"]

    class Config:
        """Pydantic configuration."""

        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()

# Made with Bob
