from django.db import models
from django.utils import timezone

# Create your models here.

class Mentee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.CharField(max_length=5)
    current_education = models.CharField(max_length=255)
    career_path = models.CharField(max_length=255)
    industry_interest = models.CharField(max_length=255)
    desired_skill = models.TextField()
    availability = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} {self.email} {self.created_at}"

    class Meta: 
        ordering = ['first_name', 'last_name']
        
class Mentor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.CharField(max_length=5)
    current_position = models.CharField(max_length=255)
    current_industry = models.CharField(max_length=255)
    previous_industry_exp = models.TextField()
    areas_of_expertise = models.TextField()
    availability = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} {self.email} {self.created_at}"

    class Meta: 
        ordering = ['first_name', 'last_name']

