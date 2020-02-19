""" The main API view. """
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from application.serializers import DaySerializer
from application.services import to_human_readable_times


@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
        return Response({'message': 'index api view :)'}, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = DaySerializer(data=request.data)
        if serializer.is_valid():
            response_data = to_human_readable_times(serializer.data)
            return Response(response_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
