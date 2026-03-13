import pytest

from package_sorter import Stack, sort


@pytest.mark.parametrize(
    ("width", "height", "length", "mass", "expected"),
    [
        (10, 10, 10, 1, Stack.STANDARD),
        (100, 100, 100, 10, Stack.SPECIAL),
        (150, 10, 10, 5, Stack.SPECIAL),
        (149, 149, 149, 20, Stack.REJECTED),
        (150, 10, 10, 20, Stack.REJECTED),
        (100, 100, 100, 20, Stack.REJECTED),
        (149, 149, 45, 19.99, Stack.STANDARD),
        (149.5, 149.5, 44.8, 19.99, Stack.SPECIAL),
    ],
)
def test_sort_returns_expected_stack(
    width: int | float,
    height: int | float,
    length: int | float,
    mass: int | float,
    expected: Stack,
) -> None:
    assert sort(width, height, length, mass) == expected


def test_volume_boundary_is_bulky() -> None:
    assert sort(100, 100, 100, 19.99) == Stack.SPECIAL


def test_dimension_boundary_is_bulky() -> None:
    assert sort(150, 1, 1, 0.1) == Stack.SPECIAL


def test_mass_boundary_is_heavy() -> None:
    assert sort(1, 1, 1, 20) == Stack.SPECIAL


def test_non_positive_measurements_raise_value_error() -> None:
    with pytest.raises(ValueError, match=r"Measurements must be greater than zero; got width=-1"):
        sort(-1, 1, 1, 1)


def test_zero_measurements_raise_value_error() -> None:
    with pytest.raises(ValueError, match=r"Measurements must be greater than zero; got width=0"):
        sort(0, 1, 1, 1)


def test_non_positive_measurements_list_all_invalid_fields() -> None:
    with pytest.raises(
        ValueError,
        match=r"Measurements must be greater than zero; got width=-1, height=0, length=-3, mass=0",
    ):
        sort(-1, 0, -3, 0)
