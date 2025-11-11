from django.test import TestCase

from book.app.Application.dto import CreateBookDTO
from book.app.Infrastructure.models import Book, Author, Reader, Category, Cycle
from book.app.Infrastructure.repositories import (
    BookRepository, AuthorRepository, CategoryRepository
)


class BaseRepositoryTestCase(TestCase):

    def test_author_create_and_get_or_create(self):
        repo = AuthorRepository()
        # Создание через create
        from dataclasses import dataclass
        @dataclass
        class DummyAuthor:
            title: str

        data = DummyAuthor(title="Author 1")
        repo.create(data)

        self.assertEqual(Author.objects.count(), 1)
        self.assertEqual(Author.objects.first().title, "Author 1")

        obj = repo.get_or_create_by_name("Author 1")
        self.assertEqual(obj.title, "Author 1")
        self.assertEqual(Author.objects.count(), 1)

        obj2 = repo.get_or_create_by_name("Author 2")
        self.assertEqual(obj2.title, "Author 2")
        self.assertEqual(Author.objects.count(), 2)


class BookRepositoryTestCase(TestCase):

    def setUp(self):
        self.author = Author.objects.create(title="Author 1")
        self.reader = Reader.objects.create(title="Reader 1")
        self.cycle = Cycle.objects.create(title="Cycle 1")
        self.category = Category.objects.create(title="Category 1")
        self.book_repo = BookRepository()

    def test_book_create_and_index(self):
        dto = CreateBookDTO(
            title="Book 1",
            image_url="/static/images/no-img.png",
            description="Some description",
            age=2023,
            time="01:00:00",
            is_published=True,
            author=self.author,
            reader=self.reader,
            cycle=self.cycle,
            cycle_number=1,
            category=[self.category.pk],
        )
        book = self.book_repo.create(dto)

        # Проверяем, что объект сохранён
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(book.title, "Book 1")
        self.assertTrue(book.is_published)

        # Проверяем индекс опубликованных книг
        books_list = self.book_repo.index()
        self.assertIn(book, books_list)

    def test_index_with_filters(self):
        # Создаём две книги, одна опубликованная, одна нет
        dto1 = CreateBookDTO(
            title="Book A",
            image_url="/static/images/no-img-a.png",
            description="Desc A",
            age=2023,
            time="01:00:00",
            is_published=True,
            author=self.author,
            reader=self.reader,
            cycle=self.cycle,
            cycle_number=1,
            category=[self.category.pk],

        )
        dto2 = CreateBookDTO(
            title="Book B",
            image_url="/static/images/no-img-b.png",
            description="Desc B",
            age=2023,
            time="02:00:00",
            is_published=False,
            author=self.author,
            reader=self.reader,
            cycle=self.cycle,
            cycle_number=2,
            category=[self.category.pk],
        )
        book1 = self.book_repo.create(dto1)
        book2 = self.book_repo.create(dto2)

        # Фильтруем по is_published=True
        published_books = self.book_repo.index_with_filters(is_published=True)
        self.assertIn(book1, published_books)
        self.assertNotIn(book2, published_books)


class BaseRepositoryGenericTest(TestCase):

    def test_category_create(self):
        repo = CategoryRepository()
        from dataclasses import dataclass
        @dataclass
        class DummyCategory:
            title: str

        data = DummyCategory(title="Cat 1")
        repo.create(data)

        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(Category.objects.first().title, "Cat 1")
