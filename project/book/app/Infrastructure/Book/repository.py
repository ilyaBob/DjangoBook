from django.shortcuts import get_object_or_404

from book.app.Infrastructure.Book.model import Book
from .abstract_repository import AbstractRepository
from ...Application import dto
from ...Domain import entities


class Repository(AbstractRepository):
    def index(self) -> list[entities.Book]:
        return list(Book.published.all())

    def index_with_filters(self, **filters) -> list[entities.Book]:
        return list(Book.published.filter(**filters))

    def create(self, data: dto.CreateBookDTO) -> Book:
        book = Book(
            title=data.title,
            image_url=data.image_url,
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

    def get_by_slug(self, slug: str) -> Book:
        return get_object_or_404(
            Book.objects.select_related('author', 'cycle', 'reader'),
            slug=slug
        )

    def get_category(self, book: Book) -> list[entities.Category]:
        return list(book.category.all())
