async def registrar_y_login(client) -> tuple[str, str]:
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

    me = await client.get("/auth/me", headers={"Authorization": f"Bearer {token}"})
    user_id = me.json()["id"]

    return token, user_id


async def test_crear_alerta(client):
    token, user_id = await registrar_y_login(client)

    response = await client.post(
        "/alerts",
        json={"user_id": user_id, "coin": "bitcoin", "threshold": 50000.0},
    )
    assert response.status_code == 200


async def test_obtener_alertas(client):
    token, user_id = await registrar_y_login(client)

    await client.post(
        "/alerts",
        json={"user_id": user_id, "coin": "bitcoin", "threshold": 50000.0},
    )

    response = await client.get(f"/alerts/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert "bitcoin" in data["alerts"]
    assert data["alerts"]["bitcoin"] == 50000.0


async def test_actualizar_alerta_existente(client):
    token, user_id = await registrar_y_login(client)

    await client.post(
        "/alerts",
        json={"user_id": user_id, "coin": "bitcoin", "threshold": 50000.0},
    )
    await client.post(
        "/alerts",
        json={"user_id": user_id, "coin": "bitcoin", "threshold": 75000.0},
    )

    response = await client.get(f"/alerts/{user_id}")
    assert response.json()["alerts"]["bitcoin"] == 75000.0