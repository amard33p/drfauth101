from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from django.conf.urls import url, include

@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def home(request):
    if not request.session.session_key:
        request.session.create()
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"session_key": request.session.session_key})
