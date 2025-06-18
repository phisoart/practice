import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from calculator.calc import add, sub, mul, div

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_sub():
    assert sub(3, 2) == 1
    assert sub(0, 5) == -5
    assert sub(-1, -1) == 0

def test_mul():
    assert mul(2, 3) == 6
    assert mul(-1, 5) == -5
    assert mul(0, 100) == 0

def test_div():
    assert div(6, 3) == 2
    assert div(-10, 2) == -5
    assert div(5, 2) == 2.5

def test_div_zero():
    import pytest
    with pytest.raises(ValueError):
        div(1, 0) 