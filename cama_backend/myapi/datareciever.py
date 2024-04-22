from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.response import Response
import json

@api_view(['POST'])
def recieve_json(request):
    try:
        json_data = json.loads(request.body)
        return JsonResponse({'message': 'Data recieved'}, status=200)
    except:
        return JsonResponse({'error': 'Invalid JSON'}, status=400) 