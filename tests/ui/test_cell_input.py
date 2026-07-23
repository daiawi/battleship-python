import pytest

from battleship.ui.cell_input import CellInput


@pytest.fixture
def cell_input_10():
    letters = [chr(x + 65) for x in range(10)]
    numbers = [str(x) for x in range(10)]
    return CellInput(letters, numbers)

@pytest.mark.parametrize("cell, expected", [
    pytest.param("B1", True, id="upper-normal"),
    pytest.param("b1", True, id="lower-normal"),
    pytest.param("A10", False, id="number-exceeds"),
    pytest.param("K1", False, id="letter-exceeds"),
    pytest.param("K10", False, id="both-exceed"),
    pytest.param("", False, id="empty"),
    pytest.param(" ", False, id="space"),
    pytest.param("dsjdkal", False, id="garbage")
]
)
def test_validate_input(cell_input_10, cell, expected):
    assert cell_input_10.validate_input_cell(cell) == expected


@pytest.mark.parametrize("cell, expected", [
    pytest.param("A1", (0,1), id="upper-normal"),
    pytest.param("c8", (2,8), id="lower-normal"),
]
)
def test_parse_input(cell_input_10, cell, expected):
    assert cell_input_10.parse_input_cell(cell) == expected