import pytest

from app.customers.schemas import CreateCustomer, RetrieveCustomer


@pytest.fixture()
def user_payload():
    """Generate a customer payload."""
    return CreateCustomer(
        name="Matheus", email="matheus@example.com", phone="21999999999"
    )


@pytest.fixture()
def specific_customer():
    """Generate an specific customer return."""
    return RetrieveCustomer(
        id=1,
        name="Matheus",
        email="matheus@example.com",
        phone="21999999999",
    )
