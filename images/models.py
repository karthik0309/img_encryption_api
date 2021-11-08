from django.db import models

from users.models import User
# Create your models here.

class Images(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    image = models.ImageField()
    type  = models.CharField(max_length=40,choices=(('encrypt','Encrypt'),('decrypt','Decrypt')))
    message = models.CharField(max_length=40,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
	    return '{}-{}'.format(str(self.user.email),str(self.name))

    class Meta:
	    unique_together = ('name', 'user',)
