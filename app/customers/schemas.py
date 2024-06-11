from pydantic import BaseModel, EmailStr


class CommonCustomer(BaseModel):
    """
    Schema representing common customer details.

    Attributes:
        name (str): The name of the customer.
        email (EmailStr): The email address of the customer.
        phone (str): The phone number of the customer.
    """

    name: str
    email: EmailStr
    phone: str


class RetrieveCustomer(CommonCustomer):
    """
    Schema representing retrieved customer details.

    Inherits:
        CommonCustomer

    Attributes:
        id (int): The ID of the customer.
    """

    id: int


class CreateCustomer(CommonCustomer):
    """
    Schema representing details for creating a new customer.

    Inherits:
        CommonCustomer
    """

    pass
