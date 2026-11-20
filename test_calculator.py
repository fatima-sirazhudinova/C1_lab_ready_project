import pytest
from calculator import Calculator


@pytest.fixture
def calc() -> Calculator:
    return Calculator()


def test_add(calc: Calculator) -> None:
    assert calc.add(2, 3) == 5


def test_subtract(calc: Calculator) -> None:
    assert calc.subtract(7, 2) == 5


def test_multiply(calc: Calculator) -> None:
    assert calc.multiply(3, 4) == 12


def test_divide(calc: Calculator) -> None:
    assert calc.divide(8, 2) == 4


def test_divide_by_zero(calc: Calculator) -> None:
    with pytest.raises(ValueError):
        calc.divide(5, 0)


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [(1.5, 0.5, 3.0), (7.5, 2.5, 3.0), (1.0, 4.0, 0.25)],
)
def test_divide_fractional_numbers(
    calc: Calculator, a: float, b: float, expected: float
) -> None:
    assert calc.divide(a, b) == pytest.approx(expected)


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [(2, 3, 6), (-2, 3, -6), (0, 10, 0)],
)
def test_multiply_various_values(
    calc: Calculator, a: float, b: float, expected: float
) -> None:
    assert calc.multiply(a, b) == expected
