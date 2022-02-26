from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contacts,name='contact'),
    path('search',views.search,name='search'),
    path('signup',views.signup,name='signup'),
    path('login',views.Login,name='login'),
    path('logout',views.Logout,name='logout')
]