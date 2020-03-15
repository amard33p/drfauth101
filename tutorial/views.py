from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.conf.urls import url, include

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def home(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"jwt_token": request.headers['Authorization']})
