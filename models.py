from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator


class Product(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255, nullable=False)
    quantity_in_stock = fields.IntField(default=0)
    quantity_sold = fields.IntField(default=0)
    unit_price = fields.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    revnue = fields.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    supplied_by = fields.ForeignKeyField("models.Supplier", related_name="goods_supplied")


class Supplier(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=20)
    company = fields.CharField(max_length=20)
    email = fields.CharField(max_length=70)
    phone = fields.CharField(max_length=20)



product_pydantic = pydantic_model_creator(Product, name="Product")
product_pydanticIn = pydantic_model_creator(Product, name="ProductIn", exclude_readonly=True)


supplier_pydantic = pydantic_model_creator(Supplier, name="Supplier")
supplier_pydanticIn = pydantic_model_creator(Supplier, name="SupplierIn", exclude_readonly=True)