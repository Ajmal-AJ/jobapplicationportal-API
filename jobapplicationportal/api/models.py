from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title

class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    applicant_name = models.CharField(max_length=255)
    email = models.EmailField()
    applied_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.applicant_name
