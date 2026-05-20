import pytest


async def test_register_crea_usuario(client):
    response = await client.post("/auth/register", json={
        "username": "juanes",
        "first_name": "Juan",
        "last_name": "Rendon",
        "email": "juan@test.com",
        "password": "password123",
    })
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "juan@test.com"
    assert data["username"] == "juanes"
    assert "hashed_password" not in data


async def test_register_email_duplicado_devuelve_400(client):
    payload = {
        "username": "juanes",
        "first_name": "Juan",
        "last_name": "Rendon",
        "email": "juan@test.com",
        "password": "password123",
    }
    await client.post("/auth/register", json=payload)

    response = await client.post("/auth/register", json=payload)
    assert response.status_code == 400


async def test_login_devuelve_token(client):
    await client.post("/auth/register", json={
        "username": "juanes",
        "first_name": "Juan",
        "last_name": "Rendon",
        "email": "juan@test.com",
        "password": "password123",
    })

    response = await client.post("/auth/login", json={
        "email": "juan@test.com",
        "password": "password123",
    })
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert len(data["access_token"]) > 0


async def test_login_password_incorrecto_devuelve_401(client):
    await client.post("/auth/register", json={
        "username": "juanes",
        "first_name": "Juan",
        "last_name": "Rendon",
        "email": "juan@test.com",
        "password": "password123",
    })

    response = await client.post("/auth/login", json={
        "email": "juan@test.com",
        "password": "password_equivocado",
    })
    assert response.status_code == 401


async def test_me_con_token_valido(client):
    await client.post("/auth/register", json={
        "username": "juanes",
        "first_name": "Juan",
        "last_name": "Rendon",
        "email": "juan@test.com",
        "password": "password123",
    })
    login = await client.post("/auth/login", json={
        "email": "juan@test.com",
        "password": "password123",
    })
    token = login.json()["access_token"]

    response = await client.get(
        "/auth/me",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert response.json()["email"] == "juan@test.com"


async def test_me_sin_token_devuelve_401(client):
    response = await client.get("/auth/me")
    assert response.status_code == 401