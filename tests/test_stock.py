from app.stock import restock
import pytest

def test_restock_basic():
    assert restock(10, 5) == 15

def test_restock_cap():
    assert restock(95, 10) == 100

def test_restock_negative():
    with pytest.raises(ValueError):
        restock(10, -1)
