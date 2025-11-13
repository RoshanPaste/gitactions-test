import pytest
import maths

def test_add():
    assert maths.sum(2, 3) == 5

def test_sub():
    assert maths.sub(3, 1) == 2

def test_mul():
    assert maths.mul(2, 3) == 6

def test_div():
    assert maths.div(10, 2) == 5