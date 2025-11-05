from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from ..serializers import AuthorSerializer
from ...Application.dto import CreateAuthorDTO
from ...Application.services import AuthorService
from ...Infrastructure.repositories import AuthorRepository

repo = AuthorRepository()
service = AuthorService(repo)


@csrf_exempt
@require_POST
def store(request):
    serializer = AuthorSerializer(data=request.POST.dict())
    serializer.is_valid(raise_exception=True)

    dto = CreateAuthorDTO(**serializer.validated_data)
    service.create(dto)

    return HttpResponse(f'1111')
