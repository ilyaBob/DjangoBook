from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from ..forms import ReaderForm
from ...Application.dto import CreateReaderDTO
from ...Application.services import ReaderService
from ...Infrastructure.Reader.repository import Repository

repo = Repository()
service = ReaderService(repo)


@csrf_exempt
@require_POST
def store(request):
    form = ReaderForm(request.POST)
    try:
        if form.is_valid():
            dto = CreateReaderDTO(**form.cleaned_data)
            service.create(dto)
            return JsonResponse({"success": True, "message": "Чтец успешно создан"})
        else:
            return JsonResponse({"success": False, "errors": form.errors.get_json_data()}, status=400)

    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)}, status=500)
