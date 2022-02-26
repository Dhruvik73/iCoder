from django.db import models

# Create your models here.
class contact(models.Model):
    srno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    phone=models.IntegerField(max_length=10)
    email=models.CharField(max_length=100)
    query=models.TextField()
    time=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
