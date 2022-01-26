from django.urls import path
from landing import views

urlpatterns = [
    path('', views.home, name='home'),
    path('coming-soon/', views.landing, name='landing'),

]
