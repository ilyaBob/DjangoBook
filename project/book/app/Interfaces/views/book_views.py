from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from ..forms import BookForm
from ...Application.dto import CreateBookDTO
from ...Application.services import BookService
from ...Infrastructure.cached_repository import CacheBookRepository
from ...Infrastructure.repositories import BookRepository

repo = CacheBookRepository(BookRepository())
service = BookService(repo)


def index(request):
    books = service.index()
    paginator = Paginator(books, 20)
    page = request.GET.get('page')
    page_data = paginator.get_page(page)

    data = {
        'title': 'aaaaaaaaaaaa',
        'books': page_data,
    }
    return render(request, 'web/book/index.html', data)


def show(request, slug: str):
    data = service.get_book_detail_by_slug(slug)
    return render(request, 'web/book/show.html', data)


@csrf_exempt
@require_POST
def store(request):
    form = BookForm(request.POST)
    try:
        if form.is_valid():
            dto = CreateBookDTO(**form.cleaned_data)
            service.create(dto)
            return JsonResponse({"success": True, "message": "Книга успешно создана"})
        else:
            return JsonResponse({"success": False, "errors": form.errors.get_json_data()}, status=400)

    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)}, status=500)
