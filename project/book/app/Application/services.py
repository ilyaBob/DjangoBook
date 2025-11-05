from .dto import CreateAuthorDTO, CreateBookDTO, CreateReaderDTO
from ..Domain import entities
from ..Domain.value_objects import Slug
from ..Infrastructure.repositories import BookRepository, AuthorRepository, ReaderRepository
from dataclasses import asdict

class BookService:
    def __init__(self, book_repo: BookRepository):
        self.book_repo = book_repo

    def list(self) -> list[entities.Book]:
        return self.book_repo.list()

    def create(self, dto: CreateBookDTO):
        slug = Slug.format_str(dto.title)
        dto_dict = asdict(dto)
        data = entities.Book(**dto_dict, slug=slug)

        self.book_repo.create(data)

class AuthorService:
    def __init__(self, author_repo: AuthorRepository):
        self.author_repo = author_repo

    def create(self, dto: CreateAuthorDTO):
        slug = Slug.format_str(dto.title)
        dto_dict = asdict(dto)
        data = entities.Author(**dto_dict, slug=slug)
        self.author_repo.create(data)

class ReaderService:
    def __init__(self, repo: ReaderRepository):
        self.repo = repo

    def create(self, data: CreateReaderDTO):
        slug = Slug.format_str(data.title)
        dto_dict = asdict(data)
        data = entities.Reader(**dto_dict, slug = slug)
        self.repo.create(data)