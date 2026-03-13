from enum import StrEnum

VOLUME_THRESHOLD_CM3 = 1_000_000
DIMENSION_THRESHOLD_CM = 150
MASS_THRESHOLD_KG = 20


class Stack(StrEnum):
    STANDARD = "STANDARD"
    SPECIAL = "SPECIAL"
    REJECTED = "REJECTED"


def sort(width: int | float, height: int | float, length: int | float, mass: int | float) -> str:
    _validate_non_negative(width=width, height=height, length=length, mass=mass)

    bulky = _is_bulky(width=width, height=height, length=length)
    heavy = mass >= MASS_THRESHOLD_KG

    if bulky and heavy:
        return Stack.REJECTED
    if bulky or heavy:
        return Stack.SPECIAL
    return Stack.STANDARD


def _is_bulky(*, width: int | float, height: int | float, length: int | float) -> bool:
    dimensions = (width, height, length)
    volume = width * height * length
    return volume >= VOLUME_THRESHOLD_CM3 or any(
        dimension >= DIMENSION_THRESHOLD_CM for dimension in dimensions
    )


def _validate_non_negative(**measurements: int | float) -> None:
    invalid_measurements = [f"{name}={value}" for name, value in measurements.items() if value <= 0]

    if invalid_measurements:
        joined = ", ".join(invalid_measurements)
        raise ValueError(f"Measurements must be greater than zero; got {joined}")
