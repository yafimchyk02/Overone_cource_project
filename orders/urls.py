from django.urls import path
from orders import views

urlpatterns = [
    # path('landing/', views.landing, name='landing'),
    path(r'^basket_adding/$', views.basket_adding, name='basket_adding'),
    path('checkout/', views.checkout, name='checkout'),

]
