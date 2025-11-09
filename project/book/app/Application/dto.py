from dataclasses import dataclass
from typing import Optional


@dataclass
class CreateBookDTO:
    title: str
    image_url: str
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


@dataclass
class ParsedBookDTO:
    title: str
    description: Optional[str]
    age: Optional[int]
    time: Optional[str]
    is_published: bool = False
    author_name: Optional[str] = None
    reader_name: Optional[str] = None
    cycle_name: Optional[str] = None
    cycle_number: Optional[int] = None
    category: list[str] = None
    image_url: Optional[str] = None