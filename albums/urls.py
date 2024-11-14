from django.urls import path, include

from albums import views
from albums.views import AddAlbum

urlpatterns = [
    path('add/', AddAlbum.as_view(), name='add'),
    path('<int:pk>', include([
        path('details/', views.details, name='albums_details'),
        path('edit/', views.edit, name='edit'),
        path('delete/', views.delete, name='albums_delete'),
    ]))
]