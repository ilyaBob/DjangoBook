from dataclasses import asdict

from .models import Book, Author
from ..Domain import entities


class BookRepository():
    def create(self, data: entities.Book) -> None:
        data = asdict(data)
        book = Book(**data)
        book.save()

    def list(self) -> list[entities.Book]:
        return list(Book.published.all())


class AuthorRepository():
    def create(self, data: entities.Author) -> None:
        data = asdict(data)
        author = Author(**data)
        author.save()
