from django.test import TestCase
from ..app.Infrastructure.models import Book, Author, Cycle, Reader, Category
from ..app.Domain.value_objects import Slug


class BookModelTest(TestCase):

    def setUp(self):
        self.author = Author.objects.create(title="John Doe")
        self.cycle = Cycle.objects.create(title="Cycle 1")
        self.reader = Reader.objects.create(title="Reader 1")
        self.category1 = Category.objects.create(title="Fantasy")
        self.category2 = Category.objects.create(title="Adventure")

    def test_book_create_and_fields(self):
        book = Book.objects.create(
            title="Test Book",
            description="Test description",
            age=2023,
            time="01:30:00",
            image_url="/static/images/no-img.png",
            is_published=True,
            author=self.author,
            cycle=self.cycle,
            reader=self.reader
        )
        self.assertEqual(book.title, "Test Book")
        self.assertEqual(book.description, "Test description")
        self.assertTrue(book.is_published)
        self.assertEqual(book.age, 2023)
        self.assertEqual(book.time, "01:30:00")
        self.assertEqual(book.image_url, "/static/images/no-img.png")

        self.assertEqual(book.author, self.author)
        self.assertEqual(book.cycle, self.cycle)
        self.assertEqual(book.reader, self.reader)

        expected_slug = Slug.format_str(book.title)
        self.assertEqual(book.slug, expected_slug)

        self.assertEqual(str(book), book.title)

    def test_book_many_to_many_category(self):
        book = Book.objects.create(
            title="Book with categories",
            description="Some description",
            age=2023,
            time="01:00:00",
            image_url="/static/images/no-img2.png"
        )
        book.category.add(self.category1, self.category2)
        self.assertEqual(book.category.count(), 2)
        self.assertIn(self.category1, book.category.all())
        self.assertIn(self.category2, book.category.all())

    def test_book_get_absolute_url(self):
        book = Book.objects.create(
            title="URL Test",
            description="URL desc",
            age=2023,
            time="01:00:00",
            image_url="/static/images/no-img3.png"
        )
        expected_url = f"/{book.slug}"
        self.assertEqual(book.get_absolute_url(), expected_url)

    def test_published_manager(self):
        book1 = Book.objects.create(
            title="Published Book",
            description="desc",
            age=2023,
            time="01:00:00",
            image_url="/static/images/published.png",
            is_published=True
        )
        book2 = Book.objects.create(
            title="Unpublished Book",
            description="desc",
            age=2023,
            time="01:00:00",
            image_url="/static/images/unpublished.png",
            is_published=False
        )

        published_books = Book.published.all()
        self.assertIn(book1, published_books)
        self.assertNotIn(book2, published_books)
