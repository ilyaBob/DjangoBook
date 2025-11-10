from dataclasses import asdict
from typing import TypeVar, Type, Generic

from .models import Book, Author, Reader, Category, Cycle
from ..Domain import entities

T = TypeVar("T")


class BaseRepository(Generic[T]):
    model: Type[T] = None

    def __init__(self):
        if not self.model:
            raise NotImplementedError("Укажите self.model в наследнике")

    def create(self, data) -> None:
        data = asdict(data)
        model = self.model(**data)
        model.save()

    def get_or_create_by_name(self, value) -> T:
        model = self.model.objects.filter(title=value).first()
        if not model:
            model = self.model(title=value)
            model.save()

        return model


class BookRepository:
    def index(self) -> list[entities.Book]:
        return list(Book.published.all())

    def index_with_filters(self, **filters) -> list[entities.Book]:
        return list(Book.published.filter(**filters))

    def create(self, data: entities.Book):
        book = Book(
            title=data.title,
            image_url=data.image_url,
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


class AuthorRepository(BaseRepository):
    model = Author


class ReaderRepository(BaseRepository):
    model = Reader


class CycleRepository(BaseRepository):
    model = Cycle


class CategoryRepository(BaseRepository):
    model = Category
