from fastapi import FastAPI

from app.customers.routers import router as customer_routers

app = FastAPI(title="FastAPI - Jeitto")


app.include_router(customer_routers)


@app.get(
    path="/health",
    name="Health check",
    description="Check if API is working",
    tags=["Api status"],
)
def healthcheck():
    return {"message": "The API is live!"}
