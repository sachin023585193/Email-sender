from django.db import models
from uuid import uuid4

# Create your models here.
class SecretKey(models.Model):
    projectname = models.CharField(max_length=50,null=False,blank=False)
    key = models.UUIDField(primary_key=True,editable=False,default=uuid4,unique=True)
    email = models.EmailField(null=False,blank=False)
    def __str__(self):
        return self.email