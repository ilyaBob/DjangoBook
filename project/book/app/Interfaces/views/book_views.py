import json

from django.core.exceptions import ValidationError
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from ..serializers import BookSerializer
from ...Application.dto import CreateBookDTO
from ...Application.services import BookService
from ...Infrastructure.models import Book
from ...Infrastructure.repositories import BookRepository

repo = BookRepository()
book_service = BookService(repo)


def index(request):
    data = {
        'title': 'aaaaaaaaaaaa',
        'books': book_service.list(),
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
    serializer = BookSerializer(data=request.POST.dict())
    serializer.is_valid(raise_exception=True)

    dto = CreateBookDTO(**serializer.validated_data)
    book_service.create(dto)
    return HttpResponse('aaaa')
