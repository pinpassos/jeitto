from typing import Dict, Union

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.customers.models import Customer
from app.customers.schemas import CreateCustomer, RetrieveCustomer
from app.dependencies import get_db

router = APIRouter(prefix="/customers", tags=["customers"])


@router.get(
    path="/{customer_id}",
    name="Retrieve client by id",
    description="Uses the id of client to retrieve only the specified",
    response_model=Union[RetrieveCustomer, Dict],
    status_code=status.HTTP_200_OK,
)
def get_customer(customer_id: int, db_session: Session = Depends(get_db)):
    customer_query = db_session.query(Customer).filter_by(id=customer_id).one_or_none()
    if not customer_query:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found"
        )

    return customer_query


@router.post(
    path="/",
    name="Create new customer",
    description="Create a new customer with the provided details",
    response_model=RetrieveCustomer,
    status_code=status.HTTP_201_CREATED,
)
def create_customer(customer: CreateCustomer, db_session: Session = Depends(get_db)):
    try:
        new_customer = Customer(**customer.model_dump())
        db_session.add(new_customer)
        db_session.commit()
        db_session.refresh(new_customer)
    except IntegrityError as err:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err.__cause__)
        ) from err

    return new_customer
