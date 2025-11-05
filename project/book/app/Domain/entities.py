from dataclasses import dataclass
from typing import Optional
from ..Domain.value_objects import Slug


@dataclass
class Book:
    title: str
    slug: Slug
    description: str
    age: int
    time: str

    is_published: bool = False
    author_id: Optional[int] = None
    id: Optional[int] = None


@dataclass
class Author:
    title: str
    slug: Slug
    id: Optional[int] = None
