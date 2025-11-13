from django.db import transaction

from .dto import CreateBookDTO
from ..Domain import entities
from ..Domain.exceptions import CreateBookException
from ..Infrastructure.abstract_repository import AbstractBookRepository
from ..Infrastructure.repositories import BookRepository, BaseRepository


class BaseService:
    def __init__(self, repo: BaseRepository):
        self.repo = repo

    def create(self, dto):
        self.repo.create(dto)


class BookService:
    def __init__(self, book_repo: AbstractBookRepository):
        self.repo = book_repo

    def index(self) -> list[entities.Book]:
        return self.repo.index()

    def index_with_filters(self, **filter) -> list[entities.Book]:
        return self.repo.index_with_filters(**filter)

    def create(self, dto: CreateBookDTO):
        try:
            with transaction.atomic():
                book = self.repo.create(dto)
                book.category.set(dto.category)
        except Exception as e:
            raise CreateBookException()

    def get_book_detail_by_slug(self, slug: str):

        book = self.repo.get_by_slug(slug)
        categories = self.repo.get_category(book)

        return {
            'title': book.title,
            'book': book,
            'first_category': categories[0],
            'categories': categories,
        }


class AuthorService(BaseService):
    pass


class CycleService(BaseService):
    pass


class ReaderService(BaseService):
    pass


class CategoryService(BaseService):
    pass
