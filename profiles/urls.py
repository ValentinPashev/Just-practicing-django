from django.urls import path

from profiles import views

urlpatterns = [
    path('details/', views.details, name='details'),
    path('delete/', views.delete, name='delete'),
]