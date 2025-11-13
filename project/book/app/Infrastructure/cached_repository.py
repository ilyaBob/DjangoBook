from django.core.cache import cache

from .abstract_repository import AbstractBookRepository
from .repositories import BookRepository
from ..Application import dto
from ..Domain import entities
from ..Infrastructure.models import Book


class CacheBookRepository(AbstractBookRepository):
    def __init__(self, repo: BookRepository):
        self.repo = repo

    def index(self) -> list[entities.Book]:
        return self.repo.index()

    def index_with_filters(self, **filters) -> list[entities.Book]:
        return self.repo.index_with_filters(**filters)

    def create(self, data: dto.CreateBookDTO) -> Book:
        return self.repo.create(data)

    def get_by_slug(self, slug: str):
        key = f"book:show:{slug}"

        if cache.has_key(key):
            return cache.get(key)

        data = self.repo.get_by_slug(slug)
        # cache.set(key, data, 3600)
        return data

    def get_category(self, book: Book) -> list[entities.Category]:
        key = f"book-category:show:{book.slug}"

        if cache.has_key(key):
            return cache.get(key)

        data = self.repo.get_category(book)
        # cache.set(key, data, 3600)

        return data
