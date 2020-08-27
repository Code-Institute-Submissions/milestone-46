from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_antiquities, name='all_antiquities'),
    path('<int:antiquity_id>/', views.single_antiquity, name='single_antiquity'),
    path('add/', views.add_antiquity, name='add_antiquity'),
    path('edit/<int:antiquity_id>/', views.edit_antiquity, name='edit_antiquity'),
    # path('delete/<int:antiquity_id>/', views.delete_antiquity, name='delete_antiquity'),
]