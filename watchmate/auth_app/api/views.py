from rest_framework.decorators import api_view
from auth_app.api.serializers import RegistrationSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from auth_app import models

@api_view(['POST',])
def logout_view(request):
    if request.method == 'POST':
        user = request.user
        if user and user.is_authenticated:
            user.auth_token.delete()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)   

@api_view(['POST', ])
def registeration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            
            data = {
                'response': "Successfully Registered",
                'username': user.username,
                'email': user.email,
                'token': Token.objects.get(user=user).key,
            }
            return Response(data, status=status.HTTP_201_CREATED)  
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
