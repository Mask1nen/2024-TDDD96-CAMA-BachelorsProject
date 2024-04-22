from django.shortcuts import render
import requests

# Create your views here.
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def hello_world(request):
    return Response({'message': 'Hello, world! haha'})


@api_view(['POST'])
def get_orcid_info(request):
    code = request.data.get('code')
    
    client_id = 'APP-IZWWE416AT5JC4N6',
    client_secret = '51bd4130-6aad-4777-9102-4755f7a5c01a',
    redirect_uri = 'http://192.168.0.34:3000/Login'

    # Make a request to the ORCID API to get the auth token
    token_url = 'https://orcid.org/oauth/token'
    headers = {'Accept': 'application/json',
               'Content-Type': 'application/x-www-form-urlencoded'}
    data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': redirect_uri
    }
    response = requests.post(token_url, headers=headers, data=data)

    # Check if the request was successful
    if response.status_code == 200:
        json_response = response.json()
        access_token = json_response.get('access_token')
        refresh_token = json_response.get('refresh_token')
        expires_in = json_response.get('expires_in')
        name = json_response.get('name')
        orcid = json_response.get('orcid')
        # Use the access token to make further requests to the ORCID API
        # Your code here
        return Response({'name': name, 'orcid': orcid})
    else:
        return Response({'error': 'Failed to get auth token', "response": response})