import requests
from django.core.management.base import BaseCommand
from django.db import transaction

from ...app.Application.dto import CreateBookDTO
from ...app.Infrastructure.parsers.fantnova_parser import FantNovaParser
from ...app.Infrastructure.repositories import AuthorRepository, ReaderRepository, CycleRepository, CategoryRepository
from ...app.Interfaces.forms import BookForm
from ...app.Interfaces.views.book_views import book_service

repo_author = AuthorRepository()
repo_reader = ReaderRepository()
repo_cycle = CycleRepository()
repo_category = CategoryRepository()


class Command(BaseCommand):
    help = "Парсит сайты и сохраняет книги в базу"

    def handle(self, *args, **options):
        self.stdout.write(self.style.MIGRATE_HEADING("===> Запуск парсинга сайтов..."))


        parser = FantNovaParser()


        urls =  parser.get_urls_with_page('https://z4.fantnova.com/page/4/')

        for url in urls:
            book_data = parser.parse(url)
            self.stdout.write(self.style.SUCCESS(f"Спарсено: {book_data.title}"))


            try:
                with transaction.atomic():
                    author = repo_author.get_or_create_by_name(book_data.author_name)
                    reader = repo_reader.get_or_create_by_name(book_data.reader_name)

                    cycle = None
                    if book_data.cycle_name:
                        cycle = repo_cycle.get_or_create_by_name(book_data.cycle_name)

                    category_ids = []
                    for category in book_data.category:
                        cat = repo_category.get_or_create_by_name(category)
                        category_ids.append(cat.id)
                        data = {
                            "title": book_data.title,
                            "description": book_data.description,
                            "author": author.pk,
                            "age": book_data.age,
                            "time": book_data.time,
                            "reader": reader.pk,
                            "is_published": 1,
                            "category": category_ids,
                            "image_url": book_data.image_url,
                        }

                        if cycle:
                            data["cycle"] = cycle.pk
                            data["cycle_number"] = book_data.cycle_number


                    form = BookForm(data)

                    if form.is_valid():
                        dto = CreateBookDTO(**form.cleaned_data)
                        book_service.create(dto)
                        self.stdout.write(self.style.SUCCESS(f"Книга успешно создана"))
                    else:
                        raise ValueError(f"Ошибка валидации формы: {form.errors.get_json_data()}")
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Ошибка при обработке '{book_data.title}': {e}"))
