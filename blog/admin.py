from django.contrib import admin
from blog.models import blogpost,blogcomment
# Register your models here.
admin.site.register((blogpost,blogcomment))