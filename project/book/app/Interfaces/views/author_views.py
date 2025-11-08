from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from ..forms import AuthorForm
from ...Application.dto import CreateAuthorDTO
from ...Application.services import AuthorService
from ...Infrastructure.repositories import AuthorRepository

repo = AuthorRepository()
service = AuthorService(repo)


@csrf_exempt
@require_POST
def store(request):
    form = AuthorForm(request.POST)
    try:
        if form.is_valid():
            dto = CreateAuthorDTO(**form.cleaned_data)
            service.create(dto)
            return JsonResponse({"success": True, "message": "Автор успешно создан"})
        else:
            return JsonResponse({"success": False, "errors": form.errors.get_json_data()}, status=400)

    except Exception as e:
        return JsonResponse({"success": False, 'message': str(e)}, status=500)
