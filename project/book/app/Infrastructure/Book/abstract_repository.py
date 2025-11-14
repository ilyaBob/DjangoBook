from abc import ABC, abstractmethod

from book.app.Application import dto
from book.app.Domain import entities
from book.app.Infrastructure.Book.model import Book


class AbstractRepository(ABC):

    @abstractmethod
    def index(self) -> list[entities.Book]:
        pass

    @abstractmethod
    def index_with_filters(self, **f) -> list[entities.Book]:
        pass

    @abstractmethod
    def create(self, data: dto.CreateBookDTO) -> Book:
        pass

    @abstractmethod
    def get_by_slug(self, slug: str):
        pass

    @abstractmethod
    def get_category(self, book: Book):
        pass
