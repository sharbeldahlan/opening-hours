""" The main API view. """
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def index(request):
    return Response({'message': 'index api view :)'}, status=status.HTTP_200_OK)
