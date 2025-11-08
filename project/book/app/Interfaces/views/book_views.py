from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from ..forms import BookForm
from ...Application.dto import CreateBookDTO
from ...Application.services import BookService
from ...Infrastructure.models import Book
from ...Infrastructure.repositories import BookRepository

repo = BookRepository()
book_service = BookService(repo)


def index(request):
    data = {
        'title': 'aaaaaaaaaaaa',
        'books': book_service.index(),
    }
    return render(request, 'web/book/index.html', data)


def show(request, slug: str):
    book = get_object_or_404(Book, slug=slug)
    data = {
        'title': book.title,
        'book': book
    }
    return render(request, 'web/book/show.html', data)


@csrf_exempt
@require_POST
def store(request):
    form = BookForm(request.POST)
    try:
        if form.is_valid():
            dto = CreateBookDTO(**form.cleaned_data)
            book_service.create(dto)
            return JsonResponse({"success": True, "message": "Книга успешно создана"})
        else:
            return JsonResponse({"success": False, "errors": form.errors.get_json_data()}, status=400)

    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)}, status=500)
