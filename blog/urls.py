from django.urls import path
from . import views
urlpatterns=[
    #api for comments
    path('blogcomments',views.blogcomments,name='blogcomment'),

    path('',views.bloghome,name='bloghome'),
    path('<str:slug>',views.blogposts,name='blogpost')

]