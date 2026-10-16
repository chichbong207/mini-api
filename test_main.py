from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_stats_math():
    r = client.get("/matieres/math/stats")
    assert r.status_code == 200
    assert r.json()["nombre"] == 4

def test_matiere_inconnue():
    r = client.get("/matieres/xyz/stats")
    assert r.status_code == 404