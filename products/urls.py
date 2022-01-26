from django.urls import path
from products import views

urlpatterns = [

    path('product/<int:product_id>/', views.product, name='product_item'),

]
