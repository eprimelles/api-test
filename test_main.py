from main import app
from fastapi.testclient import TestClient


client = TestClient(app)

def test_solutions(data, solution):

    response = client.post("/solutions", json=data)

    assert response.status_code == 200
    assert response.json() == solution


if __name__ == "__main__":

    data = {
        "orders" : [
          {
            "id" : 1,
            "item" : "Laptop",
            "quantity": 1,
            "price" : 499.90,
            "status": "completed"
        },
        {
            "id" : 2,
            "item" : "Mouse",
            "quantity": 5,
            "price" : 20,
            "status": "completed"
        },
        {
            "id" : 3,
            "item" : "Mouse",
            "quantity": 4,
            "price" : 20,
            "status": "pending"
        }
    ],
    "criterion" : "all"
    }
    #
    solution = {
        "status": 200,
        "message": 679.9
    }

    test_solutions(data=data, solution=solution)