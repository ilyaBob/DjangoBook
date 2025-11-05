from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from ..serializers import ReaderSerializer
from ...Application.dto import CreateReaderDTO
from ...Application.services import AuthorService, ReaderService
from ...Infrastructure.repositories import ReaderRepository

repo = ReaderRepository()
service = ReaderService(repo)


@csrf_exempt
@require_POST
def store(request):
    serializer = ReaderSerializer(data=request.POST.dict())
    serializer.is_valid(raise_exception=True)

    dto = CreateReaderDTO(**serializer.validated_data)
    service.create(dto)

    return HttpResponse(f'1111')
