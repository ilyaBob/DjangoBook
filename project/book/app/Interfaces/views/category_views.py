from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from ..forms import CategoryForm
from ...Application.dto import CreateCategoryDTO
from ...Application.services import CategoryService, BookService
from ...Infrastructure.Category.model import Category
from ...Infrastructure.Category.repository import Repository as CategoryRepository
from ...Infrastructure.Book.repository import Repository as BookRepository
from book.app.Infrastructure.Book.cached_repository import CacheBookRepository

repo = CategoryRepository()
service = CategoryService(repo)
book_repo = CacheBookRepository(BookRepository())
book_service = BookService(book_repo)


def index(request, slug: str):
    category = get_object_or_404(Category, slug=slug)

    books = book_service.index_with_filters(category=category)
    paginator = Paginator(books, 20)
    page = request.GET.get('page')
    page_data = paginator.get_page(page)

    data = {
        'title': f"Новые аудиокниги в жанре {category.title}",
        'books': page_data,
    }

    return render(request, 'web/book/index.html', data)


@csrf_exempt
@require_POST
def store(request):
    form = CategoryForm(request.POST)
    try:
        if form.is_valid():
            dto = CreateCategoryDTO(**form.cleaned_data)
            service.create(dto)
            return JsonResponse({"success": True, "message": "Категория успешно создана"})
        else:
            return JsonResponse({"success": False, "errors": form.errors.get_json_data()}, status=400)

    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)}, status=500)
