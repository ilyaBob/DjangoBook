from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from ..forms import CycleForm
from ...Application.dto import CreateCycleDTO
from ...Application.services import CycleService
from ...Infrastructure.Cycle.repository import Repository as CycleRepository

repo = CycleRepository()
service = CycleService(repo)


@csrf_exempt
@require_POST
def store(request):
    form = CycleForm(request.POST)
    try:
        if form.is_valid():
            dto = CreateCycleDTO(**form.cleaned_data)
            service.create(dto)
            return JsonResponse({"success": True, "message": "Цикл успешно создан"})
        else:
            return JsonResponse({"success": False, "errors": form.errors.get_json_data()}, status=400)

    except Exception as e:
        return JsonResponse({"success": False, 'message': str(e)}, status=500)
