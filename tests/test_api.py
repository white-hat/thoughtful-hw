import pytest
from starlette.testclient import TestClient

from package_sorter.api import app


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


def test_sort_standard(client: TestClient) -> None:
    response = client.post("/sort", json={"width": 10, "height": 10, "length": 10, "mass": 5})
    assert response.status_code == 200
    assert response.json() == {"stack": "STANDARD"}


def test_sort_special_bulky(client: TestClient) -> None:
    # Volume = 100 * 100 * 100 = 1,000,000 cm³ (bulky), mass = 5 kg (not heavy)
    response = client.post("/sort", json={"width": 100, "height": 100, "length": 100, "mass": 5})
    assert response.status_code == 200
    assert response.json() == {"stack": "SPECIAL"}


def test_sort_special_heavy(client: TestClient) -> None:
    # Small package (not bulky), mass = 20 kg (heavy)
    response = client.post("/sort", json={"width": 10, "height": 10, "length": 10, "mass": 20})
    assert response.status_code == 200
    assert response.json() == {"stack": "SPECIAL"}


def test_sort_rejected(client: TestClient) -> None:
    # Bulky (volume ≥ 1,000,000) AND heavy (mass ≥ 20)
    response = client.post("/sort", json={"width": 100, "height": 100, "length": 100, "mass": 20})
    assert response.status_code == 200
    assert response.json() == {"stack": "REJECTED"}


def test_sort_invalid_input(client: TestClient) -> None:
    response = client.post("/sort", json={"width": -1, "height": 10, "length": 10, "mass": 5})
    assert response.status_code == 422
    data = response.json()
    assert "width" in data["detail"]


def test_index_returns_html(client: TestClient) -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
