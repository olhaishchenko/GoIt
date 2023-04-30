from unittest.mock import MagicMock, AsyncMock

from src.conf import detail
from src.database.models import User

def test_create_user(client, user, monkeypatch):
    mock_send_email = MagicMock()
    monkeypatch.setattr('fastapi_limiter.FastAPILimiter.redis', AsyncMock())
    monkeypatch.setattr('fastapi_limiter.FastAPILimiter.identifier', AsyncMock())
    monkeypatch.setattr('fastapi_limiter.FastAPILimiter.http_callback', AsyncMock())
    monkeypatch.setattr("src.routes.auth.send_email", mock_send_email)
    response = client.post("/api/auth/signup", json=user)
    assert response.status_code == 201, response.text
    payload = response.json()
    assert payload["email"] == user.get('email')


def test_repeat_create_user(client, user, monkeypatch):
    mock_send_email = MagicMock()
    monkeypatch.setattr('fastapi_limiter.FastAPILimiter.redis', AsyncMock())
    monkeypatch.setattr('fastapi_limiter.FastAPILimiter.identifier', AsyncMock())
    monkeypatch.setattr('fastapi_limiter.FastAPILimiter.http_callback', AsyncMock())
    monkeypatch.setattr("src.routes.auth.send_email", mock_send_email)
    response = client.post("/api/auth/signup", json=user)
    assert response.status_code == 409, response.text
    payload = response.json()
    assert payload["detail"] == detail.ACCOUNT_AlREADY_EXISTS


def test_login_user_not_confirmed_email(client, user):
    response = client.post("/api/auth/login", data={"username": user.get("email"), "password": user.get("password")})
    assert response.status_code == 401, response.text
    payload = response.json()
    assert payload["detail"] == detail.EMAIL_NOT_CONFIRMED


def test_login_user(client, user, session):
    current_user: User = session.query(User).filter(User.email == user.get("email")).first()
    current_user.confirmed = True
    session.commit()
    response = client.post("/api/auth/login", data={"username": user.get("email"), "password": user.get("password")})
    assert response.status_code == 200, response.text
    payload = response.json()
    assert payload["token_type"] == "bearer"


def test_login_user_with_wrong_password(client, user, session):
    current_user: User = session.query(User).filter(User.email == user.get("email")).first()
    current_user.confirmed = True
    session.commit()
    response = client.post("/api/auth/login", data={"username": user.get("email"), "password": "password"})
    assert response.status_code == 401, response.text
    payload = response.json()
    assert payload["detail"] == detail.INVALID_PASSWORD


def test_login_user_with_wrong_email(client, user, session):
    current_user: User = session.query(User).filter(User.email == user.get("email")).first()
    current_user.confirmed = True
    session.commit()
    response = client.post("/api/auth/login", data={"username": "eaxample@test.com", "password": user.get("password")})
    assert response.status_code == 401, response.text
    payload = response.json()
    assert payload["detail"] == detail.INVALID_EMAIL


def test_refresh_token_ok(client, session, user):
    current_user: User = session.query(User).filter(User.email == user.get('email')).first()
    headers = {'Authorization': f'Bearer {current_user.refresh_token}'}
    response = client.get('api/auth/refresh_token', headers=headers)
    assert response.status_code == 200, response.text
    assert response.json()['token_type'] == 'bearer'  # m.TOKEN_TYPE
    assert response.json()['access_token'] is not None
    assert response.json()['refresh_token'] is not None


def test_invalid_refresh_token_ok(client, session, user):
    current_user: User = session.query(User).filter(User.email == user.get('email')).first()
    headers = {'Authorization': f'Bearer {"ghjg"}'}
    response = client.get('api/auth/refresh_token', headers=headers)
    assert response.status_code == 401, response.text
