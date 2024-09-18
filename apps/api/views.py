from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .logic import xlsx_export
import json

@ensure_csrf_cookie
@api_view(http_method_names=["GET"])
@permission_classes([AllowAny])
def set_csrf_token(request):
    return Response({"detail": "CSRF cookie set"})

@api_view(http_method_names=["POST", "GET"])
@permission_classes([AllowAny])
def export_to_excel(request):
    print('Exporting to excel...')
    print(request)
    data = request.data
    resp = xlsx_export.create_export(data)
    return resp