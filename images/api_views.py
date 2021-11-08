import os 
from io import BytesIO
from django.core.files.base import File
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from .serializers import ImageSerializer
from .models import Images
from users.models import User
from .encryption import process_image
from django.core.files.uploadedfile import InMemoryUploadedFile


PATH = os.getcwd()+'/img/'

class ImagesViewset(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    http_method_names = ['post','get']

    def get_queryset(self):
        get_data = self.request.query_params
        return Images.objects.filter(user=get_data['user'])
    
    def create(self, request, *args, **kwargs):
        info = request.data
        user = User.objects.get(id=info['user'])

        if info['type']=='encrypt':
            new_img = Images(user=user,
                    name=info['name'],
                    image=info['image'],
                    message=info['message']
                    )

            new_img.save()

        secrete_key = user.secrete_key
        process_image(info['image'],info['type'],secrete_key,info['message'],info['name'])

        image_file = PATH+'encrypted_'+info['name']+'.png'
        encrypted_img = Images(user=user,
        name='encrypted_'+info['name'],
        image=image_file,
        message=info['message']
        )

        if info['type']=='encrypt':
            encrypted_img.save()
        serializer = ImageSerializer(encrypted_img)

        return Response(serializer.data)
        