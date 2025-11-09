from dataclasses import dataclass
from typing import Optional


@dataclass
class Book:
    title: str
    image_url: str
    description: str
    age: int
    time: str
    category: list

    slug: Optional[str] = None
    is_published: bool = False
    author: Optional[int] = None
    reader: Optional[int] = None
    cycle: Optional[int] = None
    id: Optional[int] = None
    cycle_number: Optional[str] = None


@dataclass
class Author:
    title: str
    id: Optional[int] = None
    slug: Optional[str] = None


@dataclass
class Cycle:
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
