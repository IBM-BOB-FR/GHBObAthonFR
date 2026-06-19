"""Tests for the Blog API.

This module demonstrates testing following TDD principles and best practices.
"""

import pytest
from fastapi.testclient import TestClient
from blog_api import app, user_repository, article_repository


@pytest.fixture
def client():
    """Create a test client."""
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_repositories():
    """Reset repositories before each test."""
    user_repository._users.clear()
    user_repository._users_by_username.clear()
    user_repository._next_id = 1
    article_repository._articles.clear()
    article_repository._next_id = 1
    yield


def test_health_check(client):
    """Test the health check endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_register_user(client):
    """Test user registration."""
    response = client.post(
        "/api/v1/auth/register",
        json={
            "username": "testuser",
            "email": "test@example.com",
            "password": "password123",
        },
    )
    assert response.status_code == 201
    data = response.json()
    assert data["username"] == "testuser"
    assert data["email"] == "test@example.com"
    assert "user_id" in data


def test_register_duplicate_user(client):
    """Test registering a duplicate user fails."""
    user_data = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "password123",
    }
    client.post("/api/v1/auth/register", json=user_data)
    response = client.post("/api/v1/auth/register", json=user_data)
    assert response.status_code == 400


def test_login(client):
    """Test user login."""
    # Register user
    client.post(
        "/api/v1/auth/register",
        json={
            "username": "testuser",
            "email": "test@example.com",
            "password": "password123",
        },
    )

    # Login
    response = client.post(
        "/api/v1/auth/token",
        data={"username": "testuser", "password": "password123"},
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_login_invalid_credentials(client):
    """Test login with invalid credentials."""
    response = client.post(
        "/api/v1/auth/token",
        data={"username": "nonexistent", "password": "wrong"},
    )
    assert response.status_code == 401


def test_create_article_requires_auth(client):
    """Test that creating an article requires authentication."""
    response = client.post(
        "/api/v1/articles",
        json={"title": "Test Article", "content": "Test content"},
    )
    assert response.status_code == 401


def test_create_article(client):
    """Test creating an article with authentication."""
    # Register and login
    client.post(
        "/api/v1/auth/register",
        json={
            "username": "testuser",
            "email": "test@example.com",
            "password": "password123",
        },
    )
    login_response = client.post(
        "/api/v1/auth/token",
        data={"username": "testuser", "password": "password123"},
    )
    token = login_response.json()["access_token"]

    # Create article
    response = client.post(
        "/api/v1/articles",
        json={
            "title": "Test Article",
            "content": "This is test content",
            "published": True,
        },
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Article"
    assert data["content"] == "This is test content"
    assert data["published"] is True


def test_list_articles(client):
    """Test listing articles."""
    response = client.get("/api/v1/articles")
    assert response.status_code == 200
    data = response.json()
    assert "items" in data
    assert "total" in data
    assert isinstance(data["items"], list)


def test_get_article(client):
    """Test getting a specific article."""
    # Create an article first
    client.post(
        "/api/v1/auth/register",
        json={
            "username": "testuser",
            "email": "test@example.com",
            "password": "password123",
        },
    )
    login_response = client.post(
        "/api/v1/auth/token",
        data={"username": "testuser", "password": "password123"},
    )
    token = login_response.json()["access_token"]

    create_response = client.post(
        "/api/v1/articles",
        json={"title": "Test Article", "content": "Test content"},
        headers={"Authorization": f"Bearer {token}"},
    )
    article_id = create_response.json()["article_id"]

    # Get the article
    response = client.get(f"/api/v1/articles/{article_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["article_id"] == article_id
    assert data["title"] == "Test Article"


def test_get_nonexistent_article(client):
    """Test getting a nonexistent article returns 404."""
    response = client.get("/api/v1/articles/999")
    assert response.status_code == 404


def test_update_article(client):
    """Test updating an article."""
    # Setup: Create user and article
    client.post(
        "/api/v1/auth/register",
        json={
            "username": "testuser",
            "email": "test@example.com",
            "password": "password123",
        },
    )
    login_response = client.post(
        "/api/v1/auth/token",
        data={"username": "testuser", "password": "password123"},
    )
    token = login_response.json()["access_token"]

    create_response = client.post(
        "/api/v1/articles",
        json={"title": "Original Title", "content": "Original content"},
        headers={"Authorization": f"Bearer {token}"},
    )
    article_id = create_response.json()["article_id"]

    # Update the article
    response = client.put(
        f"/api/v1/articles/{article_id}",
        json={"title": "Updated Title", "published": True},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Title"
    assert data["published"] is True


def test_update_article_unauthorized(client):
    """Test that users can only update their own articles."""
    # Create first user and article
    client.post(
        "/api/v1/auth/register",
        json={
            "username": "user1",
            "email": "user1@example.com",
            "password": "password123",
        },
    )
    login1 = client.post(
        "/api/v1/auth/token",
        data={"username": "user1", "password": "password123"},
    )
    token1 = login1.json()["access_token"]

    create_response = client.post(
        "/api/v1/articles",
        json={"title": "User1 Article", "content": "Content"},
        headers={"Authorization": f"Bearer {token1}"},
    )
    article_id = create_response.json()["article_id"]

    # Create second user
    client.post(
        "/api/v1/auth/register",
        json={
            "username": "user2",
            "email": "user2@example.com",
            "password": "password123",
        },
    )
    login2 = client.post(
        "/api/v1/auth/token",
        data={"username": "user2", "password": "password123"},
    )
    token2 = login2.json()["access_token"]

    # Try to update with second user
    response = client.put(
        f"/api/v1/articles/{article_id}",
        json={"title": "Hacked Title"},
        headers={"Authorization": f"Bearer {token2}"},
    )
    assert response.status_code == 403


def test_delete_article(client):
    """Test deleting an article."""
    # Setup
    client.post(
        "/api/v1/auth/register",
        json={
            "username": "testuser",
            "email": "test@example.com",
            "password": "password123",
        },
    )
    login_response = client.post(
        "/api/v1/auth/token",
        data={"username": "testuser", "password": "password123"},
    )
    token = login_response.json()["access_token"]

    create_response = client.post(
        "/api/v1/articles",
        json={"title": "To Delete", "content": "Content"},
        headers={"Authorization": f"Bearer {token}"},
    )
    article_id = create_response.json()["article_id"]

    # Delete
    response = client.delete(
        f"/api/v1/articles/{article_id}",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 204

    # Verify deletion
    get_response = client.get(f"/api/v1/articles/{article_id}")
    assert get_response.status_code == 404


def test_pagination(client):
    """Test article pagination."""
    # Create multiple articles
    client.post(
        "/api/v1/auth/register",
        json={
            "username": "testuser",
            "email": "test@example.com",
            "password": "password123",
        },
    )
    login_response = client.post(
        "/api/v1/auth/token",
        data={"username": "testuser", "password": "password123"},
    )
    token = login_response.json()["access_token"]

    for i in range(15):
        client.post(
            "/api/v1/articles",
            json={"title": f"Article {i}", "content": f"Content {i}"},
            headers={"Authorization": f"Bearer {token}"},
        )

    # Test pagination
    response = client.get("/api/v1/articles?skip=0&limit=10")
    assert response.status_code == 200
    data = response.json()
    assert len(data["items"]) == 10
    assert data["total"] == 15


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

# Made with Bob
