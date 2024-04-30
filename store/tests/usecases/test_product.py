import pytest
from schemas.product import ProductOut
from usecases.product import product_usecase


async def test_usecases_should_return_success(product_in):
    result = await product_usecase.create(body=product_in)

    assert isinstance(result, ProductOut)
    assert result.name == "IPHONE 13"


async def test_usecases_get_should_return_success(product_id):
    try:
        result = await product_usecase.get(id=product_id)

        assert isinstance(result, ProductOut)
        assert result.name == "IPHONE 15"

    except Exception as e:
        pytest.fail(f"A comparacao de valores foi divergente: {e}")
