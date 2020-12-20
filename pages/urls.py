from django.urls import path
from .views import homepageView

urlpatterns=[
    path('',homepageView,name='home'),
    #path('5/',homepageView,name='home') -> means that if we want go to home page , we should type 5/ after http://127.0.0.1:8000/ => http://127.0.0.1:8000/5/
]