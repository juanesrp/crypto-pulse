from core.security import (
    hash_password,
    verify_password,
    create_access_token,
    decode_access_token,
)


def test_hash_password_genera_hash_diferente_al_original():
    hashed = hash_password("mi_password")
    assert hashed != "mi_password"


def test_hash_password_dos_hashes_del_mismo_password_son_distintos():
    hash1 = hash_password("mi_password")
    hash2 = hash_password("mi_password")
    assert hash1 != hash2


def test_verify_password_correcto():
    hashed = hash_password("mi_password")
    assert verify_password("mi_password", hashed) is True


def test_verify_password_incorrecto():
    hashed = hash_password("mi_password")
    assert verify_password("password_equivocado", hashed) is False


def test_token_roundtrip():
    user_id = "123e4567-e89b-12d3-a456-426614174000"
    token = create_access_token(user_id)
    decoded = decode_access_token(token)
    assert decoded == user_id


def test_decode_token_invalido_devuelve_none():
    resultado = decode_access_token("esto.no.es.un.token.valido")
    assert resultado is None


def test_decode_token_vacio_devuelve_none():
    resultado = decode_access_token("")
    assert resultado is None
