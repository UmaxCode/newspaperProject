from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    
    age = models.PositiveIntegerField(null=True, blank=True)



class TodoItem(models.Model):

    item_name = models.CharField(max_length=200)
    by_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):

        return self.item_name