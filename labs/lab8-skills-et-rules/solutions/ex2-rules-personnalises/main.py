"""FastAPI application entry point.

This module sets up the FastAPI application and routes.
"""

import logging
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

from models import User
from user_repository import UserRepository
from user_service import UserService
from exceptions import UserNotFoundException, ValidationError

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="User Management API",
    description="API for managing users with layered architecture",
    version="1.0.0",
)

# Initialize dependencies
repository = UserRepository()
user_service = UserService(repository)


# Pydantic models for request/response
class UserCreateRequest(BaseModel):
    """Request model for creating a user."""

    name: str = Field(..., min_length=1, description="User's full name")
    email: str = Field(..., description="User's email address")
    age: int = Field(..., ge=0, le=150, description="User's age in years")


class UserUpdateRequest(BaseModel):
    """Request model for updating a user."""

    name: str = Field(..., min_length=1, description="User's full name")
    email: str = Field(..., description="User's email address")
    age: int = Field(..., ge=0, le=150, description="User's age in years")


class UserResponse(BaseModel):
    """Response model for user data."""

    user_id: int
    name: str
    email: str
    age: int

    class Config:
        """Pydantic configuration."""

        from_attributes = True


# API Routes
@app.get("/", tags=["Health"])
async def root() -> dict[str, str]:
    """Health check endpoint.

    Returns:
        A simple health check message.
    """
    return {"status": "healthy", "service": "User Management API"}


@app.get("/users/{user_id}", response_model=UserResponse, tags=["Users"])
async def get_user(user_id: int) -> UserResponse:
    """Retrieve a user by ID.

    Args:
        user_id: The unique identifier of the user.

    Returns:
        The user data.

    Raises:
        HTTPException: If user not found or validation fails.
    """
    try:
        user = user_service.get_user_by_id(user_id)
        return UserResponse(**user.__dict__)
    except ValidationError as e:
        logger.error(f"Validation error: {e.message}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e.message,
        )
    except UserNotFoundException as e:
        logger.error(f"User not found: {e.message}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.message,
        )


@app.get("/users", response_model=list[UserResponse], tags=["Users"])
async def list_users() -> list[UserResponse]:
    """List all users.

    Returns:
        A list of all users.
    """
    users = user_service.list_all_users()
    return [UserResponse(**user.__dict__) for user in users]


@app.post(
    "/users",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Users"],
)
async def create_user(request: UserCreateRequest) -> UserResponse:
    """Create a new user.

    Args:
        request: The user creation request data.

    Returns:
        The created user data.

    Raises:
        HTTPException: If validation fails.
    """
    try:
        user = user_service.create_user(
            name=request.name,
            email=request.email,
            age=request.age,
        )
        return UserResponse(**user.__dict__)
    except ValidationError as e:
        logger.error(f"Validation error: {e.message}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e.message,
        )


@app.put("/users/{user_id}", response_model=UserResponse, tags=["Users"])
async def update_user(user_id: int, request: UserUpdateRequest) -> UserResponse:
    """Update an existing user.

    Args:
        user_id: The unique identifier of the user to update.
        request: The user update request data.

    Returns:
        The updated user data.

    Raises:
        HTTPException: If user not found or validation fails.
    """
    try:
        user = user_service.update_user(
            user_id=user_id,
            name=request.name,
            email=request.email,
            age=request.age,
        )
        return UserResponse(**user.__dict__)
    except ValidationError as e:
        logger.error(f"Validation error: {e.message}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e.message,
        )
    except UserNotFoundException as e:
        logger.error(f"User not found: {e.message}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.message,
        )


@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Users"])
async def delete_user(user_id: int) -> None:
    """Delete a user.

    Args:
        user_id: The unique identifier of the user to delete.

    Raises:
        HTTPException: If user not found or validation fails.
    """
    try:
        user_service.delete_user(user_id)
    except ValidationError as e:
        logger.error(f"Validation error: {e.message}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e.message,
        )
    except UserNotFoundException as e:
        logger.error(f"User not found: {e.message}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.message,
        )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

# Made with Bob
