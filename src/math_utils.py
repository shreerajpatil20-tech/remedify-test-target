"""
Demo helper — a simple math module for the demo repository.
Intentionally introduce a bug here (change + to -) to trigger CI failure.
"""


def add(a: int, b: int) -> int:
    return a + b


def subtract(a: int, b: int) -> int:
    return a - b


def multiply(a: int, b: int) -> int:
    return a * b
