from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):

    email = models.EmailField(unique=True)

    is_delegation = models.BooleanField('Delegation status', default=False)
    is_chair = models.BooleanField('Chair status', default=False)
    is_secretariat = models.BooleanField('Secretariat status', default=False)

class Delegation(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=200, blank=True, null=True)
    size = models.IntegerField(default=0)
    contact_number = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        if self.name is not None:
            return self.name
        else:
            return f'Delegation Object: {self.user}'
