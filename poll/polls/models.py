from django.db import models

# Create your models here.

class Faculty(models.Model):
    faculty_name = models.CharField(max_length= 50)
    faculty_dept = models.CharField(max_length=5)
    def __str__(self):
        return self.faculty_name

class Choice(models.Model):
    faculty= models.ForeignKey(Faculty, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length =50)
    votes =models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
