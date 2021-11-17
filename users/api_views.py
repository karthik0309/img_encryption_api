from .models import User
from rest_framework.response import Response
from rest_framework import generics, viewsets
from django.contrib.auth.hashers import make_password
from .serializers import UserSerializer,LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken

class UserViewset(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    http_method_names = ['post','get']

    def get_queryset(self):
        get_data = self.request.query_params
        return User.objects.filter(email=get_data['email'])

    def create(self, request, *args, **kwargs):
        request.data['password']=make_password(request.data['password'])
        serializer = UserSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({'status':403,'error':serializer.errors})
        
        serializer.save()

        user = User.objects.get(full_name=serializer.data['full_name'])
        refresh = RefreshToken.for_user(user)

        return Response({'status':200,'payload':serializer.data,'refresh': str(refresh),
        'access': str(refresh.access_token)})

class LoginViewset(generics.GenericAPIView):
    serializer_class = LoginSerializer
    
    def post(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user=serializer.validated_data
        user=User.objects.get(username=user.username)
        user_serializer=UserSerializer(user)
        refresh = RefreshToken.for_user(user)
        
        return Response({'status':200,'payload':user_serializer.data,'refresh': str(refresh),
        'access': str(refresh.access_token)})
