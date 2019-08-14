from django.db import models
from django.utils import timezone
from delegation.models import Committee
from users.models import User

# Create your models here.
class Chair(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    committee = models.ForeignKey(Committee, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Chair: {self.user} - {self.committee}"

class ProgressSheet(models.Model):

    committee = models.OneToOneField(Committee, on_delete=models.CASCADE)

    data = models.TextField()

    def __str__(self):
        return f"Progress Sheet: {self.committee}"

class LogisticsRequest(models.Model):

    committee = models.ForeignKey(Committee, on_delete=models.CASCADE)

    description = models.CharField(max_length=200)
    timestamp = models.DateTimeField('timestamp')
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Request: {self.committee} - {self.timestamp}"
