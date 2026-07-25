from dataclasses import dataclass
from enum import Enum, auto


class Orientation(Enum):
    HORIZONTAL = auto()
    VERTICAL = auto()


@dataclass(frozen=True)
class Placement:
    cell: tuple[int, int]
    orientation: Orientation


@dataclass(frozen=True)
class Shot:
    cell: tuple[int, int]


@dataclass(frozen=True)
class ActionResult:
    success: bool
    message: str | None