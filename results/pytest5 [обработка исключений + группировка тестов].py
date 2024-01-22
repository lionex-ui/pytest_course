import pytest
from contextlib import nullcontext as does_not_raise

from src.main import Calculator


class TestCalculator:
    @pytest.mark.parametrize(
        "x, y, res, expectation",
        [
            (1, 2, 0.5, does_not_raise()),
            (5, -1, -5, does_not_raise()),
            (5, "-1", -5, pytest.raises(TypeError))
        ]
    )
    def test_divide(self, x, y, res, expectation):
        with expectation:
            assert Calculator().divide(x, y) == res

    @pytest.mark.parametrize(
        "x, y, res",
        [
            (1, 1, 2),
            (1, 2, 3),
            (-1, 1, 0),
            (-100, +100, 0)
        ]
    )
    def test_add(self, x, y, res):
        assert Calculator().add(x, y) == res
