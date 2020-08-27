from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_antiquities, name='all_antiquities'),
    path('<int:antiquity_id>/', views.single_antiquity, name='single_antiquity'),
    path('add/', views.add_antiquity, name='add_antiquity'),
    # path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    # path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
]