from django.urls import path

from .views import FileUploadAPIView, AllFilesAPIView


urlpatterns = [
    path('upload', FileUploadAPIView.as_view(), name='upload', ),
    path('files', AllFilesAPIView.as_view(), name='files'),
]
