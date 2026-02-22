"""
Demo test suite — tests for math_utils.
When the bug is introduced (add returns a - b), test_add will fail.
"""

from src.math_utils import add, subtract, multiply


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply():
    assert multiply(4, 3) == 12
