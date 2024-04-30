
from AAA.services.auth_services import *
from utils import apiResponses
from utils.apiResponses import APIResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth import get_user_model
from .serializers import *


UserModel = get_user_model()

@api_view(['POST'])
@csrf_exempt
@authentication_classes([])
@permission_classes([])
def signup(request):
    try:
    
        serializer_input = UserNameSignupSerializer(data=request.data)

        if not serializer_input.is_valid():
           return APIResponse(status=apiResponses.NOK, code=apiResponses.CODE_Failed, messages=serializer_input._errors)

        data = serializer_input.validated_data
        email = data.get('email')
        password = data.get('password1')

        return ServiceSignup( email ,password )
        

    except Exception as e:
        return apiResponses.APIResponse(status=apiResponses.NOK, code=apiResponses.CODE_Failed,
                                        messages="Error in registration" + str(e.args))
        



@api_view(['POST'])
@csrf_exempt
@authentication_classes([])
@permission_classes([])
def login(request):
    try:
    
     
        serializer_input = LoginSerializerInput(data=request.data)

        if not serializer_input.is_valid():
            return APIResponse(status=apiResponses.NOK, code=apiResponses.CODE_Failed, messages=serializer_input._errors)

        data = serializer_input.validated_data
        email = data.get('email')
        password = data.get('password')

        return ServiceLogin( email ,password )
        

    except Exception as e:
        return apiResponses.APIResponse(status=apiResponses.NOK, code=apiResponses.CODE_Failed,
                                        messages="Error in registration" + str(e.args))
        



