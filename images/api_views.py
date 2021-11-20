import os
from .serializers import ImageSerializer
from .models import Images
from .encryption import process_image
from users.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

PATH = os.getcwd()+'/media/'

class ImagesViewset(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    http_method_names = ['post','get']
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        get_data = self.request.query_params
        return Images.objects.filter(user=get_data['user'])
    
    def create(self, request, *args, **kwargs):
        info = request.data
        user = User.objects.get(id=info['user'])

        new_img = Images(user=user,
                    name=info['name'],
                    image=info['image'],
                    message=info['message'],
                    type=info['type']
                    )
        new_img.save()

        secrete_key = user.secrete_key
        decoded_message=process_image(new_img,secrete_key)


        if info['type'].startswith('encrypt'):
            image_file =PATH+'encrypted_'+info['name']+'.png'
        else:
            image_file =PATH+'decrypted_'+info['name']+'.png'

        if info['type'].startswith('encrypt'):
            encrypted_img = Images(user=user,
            name='encrypted_'+info['name'],
            image=image_file,
            message=info['message'],
            type=info['type']
            )
        else:
            encrypted_img=Images(user=user,
            name='decrypted_'+info['name'],
            image=image_file,
            message=decoded_message,
            type=info['type']
            )


        encrypted_img.save()
        serializer = ImageSerializer(encrypted_img)

        return Response(serializer.data)
        