from .dto import CreateAuthorDTO, CreateBookDTO, CreateReaderDTO, CreateCategoryDTO, CreateCycleDTO
from ..Domain import entities
from ..Infrastructure.repositories import BookRepository, AuthorRepository, ReaderRepository, CategoryRepository, \
    CycleRepository
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
            title=dto.title,
            description=dto.description,
            age=dto.age,
            time=dto.time,
            category=dto.category,
            is_published=dto.is_published,
            author=dto.author,
            reader=dto.reader,
            cycle=dto.cycle,
            cycle_number=dto.cycle_number,
            image_url=dto.image_url,
        )

        book = self.book_repo.create(data)

        book.category.set(dto.category)


class AuthorService:
    def __init__(self, author_repo: AuthorRepository):
        self.author_repo = author_repo

    def create(self, dto: CreateAuthorDTO):
        data = entities.Author(**asdict(dto))
        self.author_repo.create(data)


class CycleService:
    def __init__(self, repo: CycleRepository):
        self.repo = repo

    def create(self, dto: CreateCycleDTO):
        data = entities.Cycle(**asdict(dto))
        self.repo.create(data)


class ReaderService:
    def __init__(self, repo: ReaderRepository):
        self.repo = repo

    def create(self, dto: CreateReaderDTO):
        data = entities.Reader(**asdict(dto))
        self.repo.create(data)


class CategoryService:
    def __init__(self, repo: CategoryRepository):
        self.repo = repo

    def create(self, dto: CreateCategoryDTO):
        data = entities.Category(**asdict(dto))
        self.repo.create(data)
