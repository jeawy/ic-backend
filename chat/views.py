from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .business import (
    get_all_request, get_request, post_request, put_request, patch_request, delete_request
)


# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class CompanyView(View):
    def get(self, request, *args, **kwargs):
        data = get_all_request()
        return JsonResponse(data, safe=False)

    def get_one(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        response_data = get_request(pk)
        return JsonResponse(response_data, safe=False)

    def post(self, request, *args, **kwargs):
        response_data = post_request(request.body)
        status_code = 201 if 'error' not in response_data else 400
        return JsonResponse(response_data, status=status_code)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        response_data = put_request(pk, request.body)
        status_code = 200 if 'error' not in response_data else 404
        return JsonResponse(response_data, status=status_code)

    def patch(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        response_data = patch_request(pk, request.body)
        status_code = 200 if 'error' not in response_data else 404
        return JsonResponse(response_data, status=status_code)

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        response_data = delete_request(pk)
        status_code = 200 if 'error' not in response_data else 404
        return JsonResponse(response_data, status=status_code)