from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class blogpost(models.Model):
    srno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=1000)
    content=models.TextField()
    author=models.CharField(max_length=50)
    slug=models.CharField(max_length=100)
    time=models.DateTimeField(blank=True)
    image=models.ImageField(upload_to='blog/images')
    def __str__(self):
        return self.title
class blogcomment(models.Model):
    srno=models.AutoField(primary_key=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    blog=models.ForeignKey(blogpost, on_delete=models.CASCADE)
    comment=models.TextField()
    time=models.DateTimeField(default=now)
    parent=models.ForeignKey('self', on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.user.first_name
    
    