from django.urls import path
from . import views

urlpatterns = [
    path('status/<str:id>', views.all_status, name='all_status'),
    path('file-upload/', views.file_upload, name='file_upload'),
    path('get-card-status/<str:id>', views.current_status, name='all_status'),
]
