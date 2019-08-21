from django.db import models
from users.models import Delegation

# Create your models here.
class Country(models.Model):

    name = models.CharField(max_length=200, unique=True)
    committee = models.ManyToManyField('Committee', through='Allocation')

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name

class Committee(models.Model):

    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Delegate(models.Model):

    delegation = models.ForeignKey(Delegation, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    dob = models.DateField(null=True)
    past_conferences = models.IntegerField(null=True)

    committee_preference = models.ForeignKey(Committee, on_delete=models.SET_NULL, null=True)
    country_preference = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Allocation(models.Model):

    delegate = models.OneToOneField(Delegate, on_delete=models.SET_NULL, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, default=1)
    committee = models.ForeignKey(Committee, on_delete=models.CASCADE, default=1)

    class Meta:
        unique_together = [['country', 'committee']]

    def __str__(self):
        return f"{self.committee}-{self.country}"

class PositionPaper(models.Model):

    delegate = models.OneToOneField(Delegate, on_delete=models.CASCADE)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Position Paper: {self.delegate} - {self.uploaded_at}"
