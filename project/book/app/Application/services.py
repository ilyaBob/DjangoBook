from .dto import CreateAuthorDTO, CreateBookDTO, CreateReaderDTO, CreateCategoryDTO
from ..Domain import entities
from ..Domain.value_objects import Slug
from ..Infrastructure.repositories import BookRepository, AuthorRepository, ReaderRepository, CategoryRepository
from dataclasses import asdict


class BookService:
    def __init__(self, book_repo: BookRepository):
        self.book_repo = book_repo

    def index(self) -> list[entities.Book]:
        return self.book_repo.index()

    def index_with_filters(self, **filter) -> list[entities.Book]:
        return self.book_repo.index_with_filters(**filter)

    def create(self, dto: CreateBookDTO):
        data = entities.Book(
            title = dto.title,
            description = dto.description,
            slug = Slug.format_str(dto.title),
            age = dto.age,
            time = dto.time,
            categories = dto.categories,
            is_published = dto.is_published,
            author_id = dto.author_id,
            reader_id = dto.reader_id,
        )

        book = self.book_repo.create(data)
        book.category.set(dto.categories)



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
        data = entities.Reader(**dto_dict, slug=slug)
        self.repo.create(data)


class CategoryService:
    def __init__(self, repo: CategoryRepository):
        self.repo = repo

    def create(self, data: CreateCategoryDTO):
        slug = Slug.format_str(data.title)
        dto_dict = asdict(data)
        data = entities.Category(**dto_dict, slug=slug)
        self.repo.create(data)
