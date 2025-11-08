from dataclasses import dataclass
from typing import Optional
from ..Domain.value_objects import Slug


@dataclass
class Book:
    title: str
    description: str
    age: int
    time: str
    category: list

    slug: Optional[str] = None
    is_published: bool = False
    author_id: Optional[int] = None
    reader_id: Optional[int] = None
    id: Optional[int] = None


@dataclass
class Author:
    title: str
    id: Optional[int] = None
    slug: Optional[str] = None


@dataclass
class Reader:
    title: str
    id: Optional[int] = None
    slug: Optional[str] = None


@dataclass
class Category:
    title: str
    id: Optional[int] = None
    slug: Optional[str] = None
