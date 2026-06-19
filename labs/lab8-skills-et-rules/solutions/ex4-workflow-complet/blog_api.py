"""
Blog API - Refactored from legacy code.

This module demonstrates a complete REST API following all skills and rules:
- Architecture en couches (models, repositories, services, routes)
- Conventions de nommage
- Bonnes pratiques de sécurité
- Standards API REST
- Documentation OpenAPI
- Tests unitaires et d'intégration
"""

import logging
from datetime import datetime, timedelta
from typing import Optional

from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, EmailStr
from passlib.context import CryptContext
from jose import JWTError, jwt

# Configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

SECRET_KEY = "your-secret-key-change-in-production"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/auth/token")

# ============================================================================
# MODELS (Domain Layer)
# ============================================================================


class User:
    """User domain model."""

    def __init__(
        self,
        user_id: int,
        username: str,
        email: str,
        hashed_password: str,
        is_active: bool = True,
    ) -> None:
        """Initialize a User."""
        self.user_id = user_id
        self.username = username
        self.email = email
        self.hashed_password = hashed_password
        self.is_active = is_active


class Article:
    """Article domain model."""

    def __init__(
        self,
        article_id: int,
        title: str,
        content: str,
        author_id: int,
        created_at: datetime,
        updated_at: datetime,
        published: bool = False,
    ) -> None:
        """Initialize an Article."""
        self.article_id = article_id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.published = published


# ============================================================================
# SCHEMAS (Pydantic Models for API)
# ============================================================================


class Token(BaseModel):
    """Token response schema."""

    access_token: str
    token_type: str
    expires_in: int


class UserCreate(BaseModel):
    """Schema for creating a user."""

    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=8)


class UserResponse(BaseModel):
    """Schema for user response."""

    user_id: int
    username: str
    email: str
    is_active: bool


class ArticleCreate(BaseModel):
    """Schema for creating an article."""

    title: str = Field(..., min_length=1, max_length=200)
    content: str = Field(..., min_length=1, max_length=10000)
    published: bool = False


class ArticleUpdate(BaseModel):
    """Schema for updating an article."""

    title: Optional[str] = Field(None, min_length=1, max_length=200)
    content: Optional[str] = Field(None, min_length=1, max_length=10000)
    published: Optional[bool] = None


class ArticleResponse(BaseModel):
    """Schema for article response."""

    article_id: int
    title: str
    content: str
    author_id: int
    created_at: datetime
    updated_at: datetime
    published: bool


class PaginatedArticles(BaseModel):
    """Schema for paginated articles response."""

    items: list[ArticleResponse]
    total: int
    skip: int
    limit: int


# ============================================================================
# EXCEPTIONS (Custom Exceptions)
# ============================================================================


class ArticleNotFoundException(Exception):
    """Raised when an article is not found."""

    def __init__(self, article_id: int) -> None:
        """Initialize the exception."""
        self.article_id = article_id
        self.message = f"Article with ID {article_id} not found"
        super().__init__(self.message)


class UserNotFoundException(Exception):
    """Raised when a user is not found."""

    def __init__(self, username: str) -> None:
        """Initialize the exception."""
        self.username = username
        self.message = f"User '{username}' not found"
        super().__init__(self.message)


# ============================================================================
# REPOSITORIES (Data Access Layer)
# ============================================================================


class UserRepository:
    """Repository for user data access."""

    def __init__(self) -> None:
        """Initialize the repository with in-memory storage."""
        self._users: dict[int, User] = {}
        self._users_by_username: dict[str, User] = {}
        self._next_id: int = 1
        logger.info("UserRepository initialized")

    def create(self, username: str, email: str, hashed_password: str) -> User:
        """Create a new user."""
        user = User(
            user_id=self._next_id,
            username=username,
            email=email,
            hashed_password=hashed_password,
        )
        self._users[self._next_id] = user
        self._users_by_username[username] = user
        self._next_id += 1
        logger.info(f"User created: {username}")
        return user

    def get_by_username(self, username: str) -> Optional[User]:
        """Get a user by username."""
        return self._users_by_username.get(username)

    def get_by_id(self, user_id: int) -> Optional[User]:
        """Get a user by ID."""
        return self._users.get(user_id)


class ArticleRepository:
    """Repository for article data access."""

    def __init__(self) -> None:
        """Initialize the repository with in-memory storage."""
        self._articles: dict[int, Article] = {}
        self._next_id: int = 1
        logger.info("ArticleRepository initialized")

    def create(self, title: str, content: str, author_id: int, published: bool) -> Article:
        """Create a new article."""
        now = datetime.utcnow()
        article = Article(
            article_id=self._next_id,
            title=title,
            content=content,
            author_id=author_id,
            created_at=now,
            updated_at=now,
            published=published,
        )
        self._articles[self._next_id] = article
        self._next_id += 1
        logger.info(f"Article created: {title}")
        return article

    def get_by_id(self, article_id: int) -> Optional[Article]:
        """Get an article by ID."""
        return self._articles.get(article_id)

    def get_all(self, skip: int = 0, limit: int = 10) -> list[Article]:
        """Get all articles with pagination."""
        articles = list(self._articles.values())
        return articles[skip : skip + limit]

    def count(self) -> int:
        """Count total articles."""
        return len(self._articles)

    def update(self, article_id: int, **kwargs) -> Optional[Article]:
        """Update an article."""
        article = self._articles.get(article_id)
        if not article:
            return None

        for key, value in kwargs.items():
            if value is not None and hasattr(article, key):
                setattr(article, key, value)

        article.updated_at = datetime.utcnow()
        logger.info(f"Article updated: {article_id}")
        return article

    def delete(self, article_id: int) -> bool:
        """Delete an article."""
        if article_id in self._articles:
            del self._articles[article_id]
            logger.info(f"Article deleted: {article_id}")
            return True
        return False


# ============================================================================
# SERVICES (Business Logic Layer)
# ============================================================================


class AuthService:
    """Service for authentication and authorization."""

    def __init__(self, user_repository: UserRepository) -> None:
        """Initialize the service."""
        self._user_repository = user_repository

    def hash_password(self, password: str) -> str:
        """Hash a password."""
        return pwd_context.hash(password)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """Verify a password."""
        return pwd_context.verify(plain_password, hashed_password)

    def create_access_token(self, data: dict) -> str:
        """Create a JWT access token."""
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    def authenticate_user(self, username: str, password: str) -> Optional[User]:
        """Authenticate a user."""
        user = self._user_repository.get_by_username(username)
        if not user:
            return None
        if not self.verify_password(password, user.hashed_password):
            return None
        return user

    def get_current_user(self, token: str) -> User:
        """Get the current user from a token."""
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                raise credentials_exception
        except JWTError:
            raise credentials_exception

        user = self._user_repository.get_by_username(username)
        if user is None:
            raise credentials_exception
        return user


class ArticleService:
    """Service for article business logic."""

    def __init__(self, article_repository: ArticleRepository) -> None:
        """Initialize the service."""
        self._article_repository = article_repository

    def create_article(
        self, title: str, content: str, author_id: int, published: bool
    ) -> Article:
        """Create a new article."""
        logger.info(f"Creating article: {title}")
        return self._article_repository.create(title, content, author_id, published)

    def get_article(self, article_id: int) -> Article:
        """Get an article by ID."""
        article = self._article_repository.get_by_id(article_id)
        if not article:
            raise ArticleNotFoundException(article_id)
        return article

    def list_articles(self, skip: int = 0, limit: int = 10) -> tuple[list[Article], int]:
        """List articles with pagination."""
        articles = self._article_repository.get_all(skip, limit)
        total = self._article_repository.count()
        return articles, total

    def update_article(self, article_id: int, author_id: int, **kwargs) -> Article:
        """Update an article."""
        article = self.get_article(article_id)

        # Authorization check
        if article.author_id != author_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not authorized to update this article",
            )

        updated_article = self._article_repository.update(article_id, **kwargs)
        if not updated_article:
            raise ArticleNotFoundException(article_id)
        return updated_article

    def delete_article(self, article_id: int, author_id: int) -> None:
        """Delete an article."""
        article = self.get_article(article_id)

        # Authorization check
        if article.author_id != author_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not authorized to delete this article",
            )

        if not self._article_repository.delete(article_id):
            raise ArticleNotFoundException(article_id)


# ============================================================================
# FASTAPI APPLICATION
# ============================================================================

app = FastAPI(
    title="Blog API",
    description="Modern REST API for blog management with JWT authentication",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize repositories and services
user_repository = UserRepository()
article_repository = ArticleRepository()
auth_service = AuthService(user_repository)
article_service = ArticleService(article_repository)


# ============================================================================
# DEPENDENCIES
# ============================================================================


async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    """Dependency to get the current authenticated user."""
    return auth_service.get_current_user(token)


# ============================================================================
# ROUTES
# ============================================================================


@app.get("/", tags=["Health"])
async def root() -> dict[str, str]:
    """Health check endpoint."""
    return {"status": "healthy", "service": "Blog API", "version": "1.0.0"}


@app.post(
    "/api/v1/auth/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Authentication"],
    summary="Register a new user",
)
async def register(user_data: UserCreate) -> UserResponse:
    """Register a new user."""
    # Check if user already exists
    existing_user = user_repository.get_by_username(user_data.username)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered",
        )

    # Create user
    hashed_password = auth_service.hash_password(user_data.password)
    user = user_repository.create(user_data.username, user_data.email, hashed_password)

    return UserResponse(
        user_id=user.user_id,
        username=user.username,
        email=user.email,
        is_active=user.is_active,
    )


@app.post(
    "/api/v1/auth/token",
    response_model=Token,
    tags=["Authentication"],
    summary="Login to get access token",
)
async def login(form_data: OAuth2PasswordRequestForm = Depends()) -> Token:
    """Authenticate and get access token."""
    user = auth_service.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = auth_service.create_access_token(data={"sub": user.username})
    return Token(
        access_token=access_token,
        token_type="bearer",
        expires_in=ACCESS_TOKEN_EXPIRE_MINUTES * 60,
    )


@app.get(
    "/api/v1/articles",
    response_model=PaginatedArticles,
    tags=["Articles"],
    summary="List all articles",
)
async def list_articles(skip: int = 0, limit: int = 10) -> PaginatedArticles:
    """List all articles with pagination."""
    articles, total = article_service.list_articles(skip, limit)

    return PaginatedArticles(
        items=[
            ArticleResponse(
                article_id=a.article_id,
                title=a.title,
                content=a.content,
                author_id=a.author_id,
                created_at=a.created_at,
                updated_at=a.updated_at,
                published=a.published,
            )
            for a in articles
        ],
        total=total,
        skip=skip,
        limit=limit,
    )


@app.get(
    "/api/v1/articles/{article_id}",
    response_model=ArticleResponse,
    tags=["Articles"],
    summary="Get an article by ID",
)
async def get_article(article_id: int) -> ArticleResponse:
    """Get a specific article by ID."""
    try:
        article = article_service.get_article(article_id)
        return ArticleResponse(
            article_id=article.article_id,
            title=article.title,
            content=article.content,
            author_id=article.author_id,
            created_at=article.created_at,
            updated_at=article.updated_at,
            published=article.published,
        )
    except ArticleNotFoundException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.message)


@app.post(
    "/api/v1/articles",
    response_model=ArticleResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Articles"],
    summary="Create a new article",
)
async def create_article(
    article_data: ArticleCreate,
    current_user: User = Depends(get_current_user),
) -> ArticleResponse:
    """Create a new article (authentication required)."""
    article = article_service.create_article(
        title=article_data.title,
        content=article_data.content,
        author_id=current_user.user_id,
        published=article_data.published,
    )

    return ArticleResponse(
        article_id=article.article_id,
        title=article.title,
        content=article.content,
        author_id=article.author_id,
        created_at=article.created_at,
        updated_at=article.updated_at,
        published=article.published,
    )


@app.put(
    "/api/v1/articles/{article_id}",
    response_model=ArticleResponse,
    tags=["Articles"],
    summary="Update an article",
)
async def update_article(
    article_id: int,
    article_data: ArticleUpdate,
    current_user: User = Depends(get_current_user),
) -> ArticleResponse:
    """Update an article (authentication required, author only)."""
    try:
        update_data = article_data.model_dump(exclude_unset=True)
        article = article_service.update_article(
            article_id, current_user.user_id, **update_data
        )

        return ArticleResponse(
            article_id=article.article_id,
            title=article.title,
            content=article.content,
            author_id=article.author_id,
            created_at=article.created_at,
            updated_at=article.updated_at,
            published=article.published,
        )
    except ArticleNotFoundException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.message)


@app.delete(
    "/api/v1/articles/{article_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Articles"],
    summary="Delete an article",
)
async def delete_article(
    article_id: int,
    current_user: User = Depends(get_current_user),
) -> None:
    """Delete an article (authentication required, author only)."""
    try:
        article_service.delete_article(article_id, current_user.user_id)
    except ArticleNotFoundException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.message)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

# Made with Bob
