from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from AAA.tasks import send_registration_message
from utils import apiResponses


UserModel = get_user_model()

def ServiceLogin(email , password):
            # find user using email
        user = UserModel.objects.filter(email=email).first()

        if user is None:
            return apiResponses.APIResponse(status=apiResponses.OK, code=apiResponses.CODE_SUCCESS,
                                        messages="User is not registered")

        
        if not user.check_password(password):
            
            return  apiResponses.APIResponse(status=apiResponses.NOK, code=apiResponses.CODE_Failed,
                               messages="credential is not valid !")
            
        JWTTPKENREFRESH = RefreshToken.for_user(user)
        
        response = {
            "email": user.email,
            'refresh': str(JWTTPKENREFRESH),
            'access': str(JWTTPKENREFRESH.access_token)
        }
        send_registration_message.delay(user.username)
        return apiResponses.APIResponse(status=apiResponses.OK, code=apiResponses.CODE_SUCCESS, messages="Login successfully",
                           data=response)
        
def ServiceSignup( email ,password):
    
    
        user = UserModel.objects.filter(email=email).first()
        
        if user is not None:
            return apiResponses.APIResponse(status=apiResponses.OK, code=apiResponses.CODE_SUCCESS,
                                        messages="User already registered")
        
                
        user = UserModel.objects.create_user(username=email , password=password)
        user.email = email
        user.save()
        return apiResponses.APIResponse(status=apiResponses.OK, code=apiResponses.CODE_SUCCESS,
                                        messages="Registered Successfully")

 