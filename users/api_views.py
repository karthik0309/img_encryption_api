from rest_framework import viewsets
from .serializers import UserSerializer
from .models import User

class UserViewset(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    http_method_names = ['post','get']

    def get_queryset(self):
        get_data = self.request.query_params
        return User.objects.filter(email=get_data['email'])
