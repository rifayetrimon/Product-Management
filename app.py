from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from models import (Supplier, supplier_pydantic, supplier_pydanticIn, Product, product_pydantic, product_pydanticIn)

app = FastAPI()

@app.get("/")
async def index():
    return {"message": "go to /docs for API documentation"}


@app.post("/supplier")
async def add_supplier(supplier_info: supplier_pydanticIn): # type: ignore
    supplier_obj = await Supplier.create(**supplier_info.dict(exclude_unset=True))
    response = await supplier_pydantic.from_tortoise_orm(supplier_obj)
    return {"status": "success", "data": response}


@app.post("/product")
async def add_product(product_info: product_pydanticIn): # type: ignore
    product_obj = await Product.create(**product_info.dict(exclude_unset=True))
    response = await product_pydantic.from_tortoise_orm(product_obj)  # Use the correct product_pydantic here
    return {"status": "success", "data": response}


register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True
)