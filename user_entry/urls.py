from django.urls import path
from .views import CreateMediaLink, UpdateMediaLink, GetMediaLinks

urlpatterns = [
    path('media-links/', GetMediaLinks.as_view(), name='get_media_links'),
    path('media-links/create/', CreateMediaLink.as_view(), name='create_media_link'),
    path('media-links/update/<int:pk>/', UpdateMediaLink.as_view(), name='update_media_link'),
]
