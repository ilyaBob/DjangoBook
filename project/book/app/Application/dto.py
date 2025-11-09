from dataclasses import dataclass
from typing import Optional


@dataclass
class CreateBookDTO:
    title: str
    description: str
    age: int
    time: str
    category: list[int]
    is_published: bool = False
    author: Optional[int] = None
    reader: Optional[int] = None
    cycle: Optional[int] = None
    cycle_number: Optional[str] = None


@dataclass
class CreateAuthorDTO:
    title: str


@dataclass
class CreateReaderDTO:
    title: str


@dataclass
class CreateCategoryDTO:
    title: str

@dataclass
class CreateCycleDTO:
    title: str
