from rest_framework.generics import CreateAPIView,RetrieveUpdateAPIView
from django.contrib.auth import get_user_model,authenticate
from rest_framework.views import  APIView
from rest_framework.response import Response
from rest_framework import permissions,status


from .serializers import UserSerializer



class SignInView(APIView):

    permission_classes = (permissions.AllowAny,)

    authentication_classes = ()

    def post(self,request,format=None):
        
        data = request.data

        primary = data.get("primary")

        user = None

        if self.check_is_email(primary):
            user = authenticate(email=primary,password=data.get("password"))
        else:
            user = authenticate(phone=primary,password=data.get("password"))

        if not user:
            return Response({'detail': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)

        token = user.encode_auth_token(user.id)

        serialized_user = UserSerializer(user)

        return Response({
            # 'user': serialized_user.data,           
            'token': token.decode(),
        },status=status.HTTP_200_OK)




    

    def check_is_email(self,e):
        if "@" in e:
            return True
        return False



class CreateUserView(APIView):

    permission_classes = (permissions.AllowAny,)

    authentication_classes = ()

    def post(self,request,format=None):
        user_payload = request.data
        serialized_data = UserSerializer(data=user_payload)
        serialized_data.is_valid(raise_exception=True)
        serialized_data.save()
        return Response({},status=status.HTTP_201_CREATED)



class UserProfileView(APIView):

    def get(self,request,format=None):
        serialized_user = UserSerializer(request.user)
        return Response(serialized_user.data,status=status.HTTP_200_OK)

    
    def put(self,request,format=None):
        serialized_user = UserSerializer(instance=request.user,data=request.data,partial=True)
        serialized_user.is_valid(raise_exception=True)
        serialized_user.save()
        return Response(status=status.HTTP_205_RESET_CONTENT)