from django.db import transaction

from .dto import CreateBookDTO
from ..Domain import entities
from ..Domain.exceptions import CreateBookException
from ..Infrastructure.repositories import BookRepository, BaseRepository


class BaseService:
    def __init__(self, repo: BaseRepository):
        self.repo = repo

    def create(self, dto):
        self.repo.create(dto)


class BookService:
    def __init__(self, book_repo: BookRepository):
        self.book_repo = book_repo

    def index(self) -> list[entities.Book]:
        return self.book_repo.index()

    def index_with_filters(self, **filter) -> list[entities.Book]:
        return self.book_repo.index_with_filters(**filter)

    def create(self, dto: CreateBookDTO):
        try:
            with transaction.atomic():
                book = self.book_repo.create(dto)
                book.category.set(dto.category)
        except Exception as e:
            raise CreateBookException()


class AuthorService(BaseService):
    pass


class CycleService(BaseService):
    pass


class ReaderService(BaseService):
    pass


class CategoryService(BaseService):
    pass
