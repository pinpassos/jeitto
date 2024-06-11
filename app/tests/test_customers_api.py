from .fixtures import specific_customer, user_payload  # pylint: disable=unused-import


def test_create_customer(test_client, user_payload, specific_customer):
    """Test to create a customer through API."""
    new_client = test_client.post("/customers", json=user_payload.model_dump())
    assert new_client.status_code == 201
    assert new_client.json() == specific_customer.model_dump()


def test_ensure_email_customer_constraint(test_client, user_payload):
    """Ensure that there are no users with the same email in the database can be saved."""
    test_client.post("/customers", json=user_payload.model_dump())
    customer_two = test_client.post("/customers", json=user_payload.model_dump())

    assert customer_two.status_code == 500
    assert customer_two.json() == {
        "detail": "UNIQUE constraint failed: customers.email"
    }


def test_retrieve_customer(test_client, user_payload, specific_customer):
    """Test to retrieve a customer through API."""
    test_client.post("/customers", json=user_payload.model_dump())
    specific_retrieved_client = test_client.get("/customers/1")
    assert specific_retrieved_client.status_code == 200
    assert specific_retrieved_client.json() == specific_customer.model_dump()


def test_customer_not_found(test_client):
    """Test to retrieve a customer through API."""
    specific_retrieved_client = test_client.get("/customers/1")
    assert specific_retrieved_client.status_code == 404
    assert specific_retrieved_client.json() == {"detail": "Customer not found"}
