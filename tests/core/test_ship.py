import pytest

from battleship.core.actions import Orientation, Placement
from battleship.core.ship import Ship


@pytest.fixture
def cruiser():
    return Ship("Cruiser", 3)

@pytest.fixture
def battleship():
    return Ship("Battleship", 4)


@pytest.mark.parametrize("center, expected", [
    pytest.param(Placement(cell=(0,1), orientation=Orientation.HORIZONTAL),
                 [(0,0),(0,1),(0,2)],
                 id="Horizontal"),
    pytest.param(Placement(cell=(1,0), orientation=Orientation.VERTICAL),
                 [(0,0),(1,0),(2,0)],
                 id="Vertical")
]
)
def test_cruiser_extent(cruiser, center, expected):
    assert cruiser.get_extent(center) == expected


@pytest.mark.parametrize("center, expected", [
    pytest.param(Placement(cell=(0,1), orientation=Orientation.HORIZONTAL),
                 [(0,0),(0,1),(0,2),(0,3)],
                 id="Horizontal"),
    pytest.param(Placement(cell=(1,0), orientation=Orientation.VERTICAL),
                 [(0,0),(1,0),(2,0),(3,0)],
                 id="Vertical")
]
)
def test_battleship_extent(battleship, center, expected):
    assert battleship.get_extent(center) == expected