from django.urls import path
from .views import *


urlpatterns = [
    path('userinfo/', UserinfoView.as_view(), name='userinfo'),
    path('update-userinfo/<int:pk>/', UpdateUserinfo.as_view(), name='update-userinfo'),
    path('skills/', SkillsView.as_view(), name='skills'),
    # sub-urls for skills view
    path('prog-languages/', ProgLanguageView.as_view(), name='prog_languages'),
    path('other-languages/', OtherLanguageView.as_view(), name='other_languages'),
    path('tools/', ToolsView.as_view(), name='tools'),
    path('databases/', DatabasesView.as_view(), name='databases'),
    path('frameworks/', FrameworksView.as_view(), name='frameworks'),

    path('media-links/', GetMediaLinks.as_view(), name='get_media_links'),
    path('media-links/create/', CreateMediaLink.as_view(), name='create_media_link'),
    path('media-links/update/<int:pk>/', UpdateMediaLink.as_view(), name='update_media_link'),
    
]
