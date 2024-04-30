from uuid import UUID

from pydantic import ValidationError
import pytest

from schemas.product import ProductIn
from tests.factories import product_data


def test_schemas_return_success():
    # data = {"name": "IPHONE 13", "quantity": 10, "price": 8.500, "status": True}
    data = product_data()
    product = ProductIn.model_validate(data)

    assert product.name == "IPHONE 13"
    assert product.quantity == 10
    assert product.price == 8.500
    assert isinstance(product.id, UUID)


def test_schemas_return_raise():
    data = {"name": "IPHONE 13", "quantity": 10, "price": 8.500}

    with pytest.raises(ValidationError) as err:
        ProductIn.model_validate(data)

    assert err.value.errors()[0] == {
        "type": "missing",
        "loc": ("status",),
        "msg": "Field required",
        "input": {"name": "IPHONE 13", "quantity": 10, "price": 8.5},
        "url": "https://errors.pydantic.dev/2.7/v/missing",
    }
