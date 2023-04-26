from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=250)

    def __str__(self):
        return self.name
class Work(models.Model):
    LINK_CHOICES=(
        ('Youtube','Youtube'),
        ('Instagram','Instagram'),
        ('Other','Other')
    )
    link=models.URLField()
    work_type=models.CharField(max_length=250)
    youtube=models.URLField(blank=True, null=True)
    instagram=models.URLField(blank=True, null=True)

    def __str__(self):
        return self.work_type
    
class Artist(models.Model):
    name=models.CharField(max_length=250)
    work=models.ManyToManyField(Work)

    def __str__(self):
        return self.name
    
