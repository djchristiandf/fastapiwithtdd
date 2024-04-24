from uuid import UUID

from schemas.product import ProductIn


def test_schemas_validated():
    data = {"name": "IPHONE 13", "quantity": 10, "price": 8.500, "status": True}
    product = ProductIn.model_validate(data)

    assert product.name == "IPHONE 13"
    assert product.quantity == 10
    assert product.price == 8.500
    assert isinstance(product.id, UUID)
