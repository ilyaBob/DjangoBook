from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from ..serializers import CategorySerializer
from ...Application.dto import CreateCategoryDTO
from ...Application.services import CategoryService, BookService
from ...Infrastructure.repositories import CategoryRepository, BookRepository

from ...Infrastructure.models import Book, Category

repo = CategoryRepository()
service = CategoryService(repo)
book_repo = BookRepository()
book_service = BookService(book_repo)


def index(request, slug: str):
    category = get_object_or_404(Category, slug=slug)

    data = {
        'title': f"Новые аудиокниги в жанре {category.title}",
        'books': book_service.index_with_filters(category=category),
    }

    return render(request, 'web/book/index.html', data)


@csrf_exempt
@require_POST
def store(request):
    serializer = CategorySerializer(data=request.POST.dict())
    serializer.is_valid(raise_exception=True)

    dto = CreateCategoryDTO(**serializer.validated_data)
    service.create(dto)
    return HttpResponse('aaaa')
