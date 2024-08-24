from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_item():
    """
    Test case for creating a new item.
    """
    item_data = {
        "name": "Test Item",
        "description": "A test item",
        "category": "GADGET",
        "quantity": 10,
        "price": 99.99
    }
    response = client.post("/item", json=item_data)
    assert response.status_code == 201
    assert response.json()["name"] == item_data["name"]


def test_read_items():
    """
   Test case for reading the list of items.
   """
    # First, create an item to ensure there's something to read
    item_data = {
        "name": "Test Item",
        "description": "A test item",
        "category": "GADGET",
        "quantity": 10,
        "price": 99.99
    }
    client.post("/item", json=item_data)

    # Now read the items
    response = client.get("/items")
    assert response.status_code == 200
    assert len(response.json()["items"]) > 0  # assuming pagination


def test_read_item():
    """
    Test case for reading a single item by ID.
    """
    # Create an item first
    item_data = {
        "name": "Test Item",
        "description": "A test item",
        "category": "GADGET",
        "quantity": 10,
        "price": 99.99
    }
    post_response = client.post("/item", json=item_data)
    item_id = post_response.json()["id"]

    # Now read the specific item
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json()["name"] == item_data["name"]


def test_read_nonexistent_item():
    """
    Test case for reading an item that does not exist.
    """
    response = client.get("/items/9999")  # Assuming 9999 is an ID that does not exist
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}


def test_update_item():
    """
    Test case for updating an existing item.
    """
    # Create an item first
    item_data = {
        "name": "Test Item",
        "description": "A test item",
        "category": "GADGET",
        "quantity": 10,
        "price": 99.99
    }
    post_response = client.post("/item", json=item_data)
    item_id = post_response.json()["id"]

    # Update the item
    update_data = {
        "name": "Updated Test Item",
        "description": "An updated test item",
        "category": "GADGET",
        "quantity": 20,
        "price": 199.99
    }
    response = client.put(f"/item/{item_id}", json=update_data)
    assert response.status_code == 200
    assert response.json()["name"] == update_data["name"]
    assert response.json()["quantity"] == update_data["quantity"]


def test_update_nonexistent_item():
    """
    Test case for updating an item that does not exist.
    """
    update_data = {
        "name": "Updated Item",
        "description": "Updated description",
        "category": "GADGET",
        "quantity": 20,
        "price": 199.99
    }

    response = client.put("/item/9999", json=update_data)  # Assuming 9999 is an ID that does not exist
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}


def test_delete_item():
    """
    Test case for deleting an existing item.
    """
    # Create an item first
    item_data = {
        "name": "Test Item",
        "description": "A test item",
        "category": "GADGET",
        "quantity": 10,
        "price": 99.99
    }
    post_response = client.post("/item", json=item_data)
    item_id = post_response.json()["id"]

    # Now delete the item
    response = client.delete(f"/item/{item_id}")
    assert response.status_code == 200

    # Verify the item is deleted
    get_response = client.get(f"/items/{item_id}")
    assert get_response.status_code == 404


def test_delete_nonexistent_item():
    """
    Test case for deleting an item that does not exist.
    """
    response = client.delete(f"/item/9999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}
