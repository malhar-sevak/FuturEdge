from django.db import models

# Create your models here.
class CareerInput(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    education = models.CharField(max_length=100)
    skills = models.TextField()  
    interest = models.TextField()
    predicted_career = models.CharField(max_length=100, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.predicted_career or 'Pending'}"
