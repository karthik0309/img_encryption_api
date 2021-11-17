from django.db import models
from users.models import User
from cloudinary.models import CloudinaryField

class Images(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    image = CloudinaryField('image')
    type  = models.CharField(max_length=40,choices=(('encrypt_cbc','Encrypt_CBC'),('decrypt_cbc','Decrypt_CBC'),('encrypt_ecb','Encrypt_ECB'),('decrypt_ecb','Decrypt_ECB')))
    message = models.CharField(max_length=40,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
	    return '{}-{}'.format(str(self.user.email),str(self.name))

    class Meta:
	    unique_together = ('name', 'user',)
