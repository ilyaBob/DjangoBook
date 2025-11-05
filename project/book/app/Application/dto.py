from dataclasses import dataclass
from typing import Optional


@dataclass
class CreateBookDTO:
    title: str
    description: str
    age: int
    time: str
    is_published: bool = False
    author_id: Optional[int] = None


@dataclass
class CreateAuthorDTO:
    title: str
