import pytest

from battleship.core.actions import Orientation
from battleship.ui.cell_input import CellInput


@pytest.fixture
def cell_input_10():
    letters = [chr(x + 65) for x in range(10)]
    numbers = [str(x) for x in range(10)]
    return CellInput(letters, numbers)

@pytest.mark.parametrize("cell, expected", [
    pytest.param("B1", True, id="upper-normal"),
    pytest.param("b1", True, id="lower-normal"),
    pytest.param(" B1", True, id="leading-space"),
    pytest.param("B1 ", True, id="trailing-space"),
    pytest.param("A10", False, id="number-exceeds"),
    pytest.param("K1", False, id="letter-exceeds"),
    pytest.param("K10", False, id="both-exceed"),
    pytest.param("", False, id="empty"),
    pytest.param(" ", False, id="space"),
    pytest.param("d1jdkal", False, id="garbage")
]
)
def test_validate_input_cell(cell_input_10, cell, expected):
    assert cell_input_10.validate_input_cell(cell) == expected


@pytest.mark.parametrize("cell, expected", [
    pytest.param("A1", (0,1), id="upper-normal"),
    pytest.param("c8", (2,8), id="lower-normal"),
]
)
def test_parse_input_cell(cell_input_10, cell, expected):
    assert cell_input_10.parse_input_cell(cell) == expected


@pytest.mark.parametrize("dir, expected", [
    pytest.param("H", True, id="upper-horizontal"),
    pytest.param("h", True, id="lower-horizontal"),
    pytest.param("V", True, id="upper-vertical"),
    pytest.param("v", True, id="lower-vertical"),
    pytest.param(" V", True, id="leading-space"),
    pytest.param("V ", True, id="trailing-space"),
    pytest.param("", False, id="empty"),
    pytest.param(" ", False, id="space"),
    pytest.param("Vjdsoai", False, id="garbage")
]
)
def test_validate_input_dir(cell_input_10, dir, expected):
    assert cell_input_10.validate_input_dir(dir) == expected

@pytest.mark.parametrize("dir, expected", [
    pytest.param("V", Orientation.VERTICAL, id="upper-vertical"),
    pytest.param("v", Orientation.VERTICAL, id="lower-vertical"),
    pytest.param("H", Orientation.HORIZONTAL, id="upper-horizontal"),
    pytest.param("h", Orientation.HORIZONTAL, id="lower-horizontal")
]
)
def test_parse_input_dir(cell_input_10, dir, expected):
    assert cell_input_10.parse_input_dir(dir) == expected