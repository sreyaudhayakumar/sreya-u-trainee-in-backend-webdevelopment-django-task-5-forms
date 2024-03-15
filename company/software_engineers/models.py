from django.db import models

class HighEmployee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    department = models.CharField(max_length=250)
    yearofjoin=models.IntegerField()

class MiddleEmployee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    department = models.CharField(max_length=250)
    yearofjoin=models.IntegerField()

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name

