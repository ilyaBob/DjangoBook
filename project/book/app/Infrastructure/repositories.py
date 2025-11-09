from dataclasses import asdict

from .models import Book, Author, Reader, Category, Cycle
from ..Domain import entities


class BookRepository():
    def index(self) -> list[entities.Book]:
        return list(Book.published.all())

    def index_with_filters(self, **filters) -> list[entities.Book]:
        return list(Book.published.filter(**filters))

    def create(self, data: entities.Book):
        book = Book(
            title=data.title,
            slug=data.slug,
            description=data.description,
            age=data.age,
            time=data.time,
            is_published=data.is_published,
            author=data.author,
            reader=data.reader,
            cycle=data.cycle,
            cycle_number=data.cycle_number,
        )

        book.save()

        return book


class AuthorRepository():
    def create(self, data: entities.Author) -> None:
        data = asdict(data)
        author = Author(**data)
        author.save()


class ReaderRepository():
    def create(self, data: entities.Reader) -> None:
        data = asdict(data)
        reader = Reader(**data)
        reader.save()

class CycleRepository():
    def create(self, data: entities.Cycle) -> None:
        data = asdict(data)
        cycle = Cycle(**data)
        cycle.save()


class CategoryRepository():
    def create(self, data: entities.Category) -> None:
        data = asdict(data)
        category = Category(**data)
        category.save()
