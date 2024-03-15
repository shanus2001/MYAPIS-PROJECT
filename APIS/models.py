from django.db import models

# Create your models here.
class apitool(models.Model):
    tool_title=models.CharField(max_length=120)
    tool_desc=models.TextField()
    date=models.DateTimeField(auto_now_add=True)