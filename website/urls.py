from django.urls import path
from . import views

app_name = 'website'
urlpatterns = [
    path('', views.main, name='index'),
    path('login/', views.login, name='login')
]