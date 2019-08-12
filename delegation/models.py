from django.db import models
from users.models import Delegation

# Create your models here.
class Country(models.Model):

    name = models.CharField(max_length=200, unique=True)
    country_committee = models.ManyToManyField('Committee', through='CountryCommitteeAllocation')

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name

class Committee(models.Model):

    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Delegate(models.Model):

    delegate_delegation = models.ForeignKey(Delegation, on_delete=models.CASCADE)

    delegate_first_name = models.CharField(max_length=200)
    delegate_last_name = models.CharField(max_length=200)
    delegate_email = models.EmailField()
    delegate_dob = models.DateField(null=True)
    delegate_past_conferences = models.IntegerField(null=True)

    delegate_committee_preference = models.ForeignKey(Committee, on_delete=models.SET_NULL, null=True)
    delegate_country_preference = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return f"{self.delegate_first_name} {self.delegate_last_name} - {self.delegate_delegation}"


class CountryCommitteeAllocation(models.Model):

    allocated_delegate = models.OneToOneField(Delegate, on_delete=models.SET_NULL, null=True, blank=True)
    allocated_country = models.ForeignKey(Country, on_delete=models.CASCADE, default=1)
    allocated_committee = models.ForeignKey(Committee, on_delete=models.CASCADE, default=1)

    class Meta:
        unique_together = [['allocated_country', 'allocated_committee']]

    def __str__(self):
        return f"{self.allocated_committee}-{self.allocated_country}"
