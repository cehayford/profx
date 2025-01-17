from django.urls import path
from .views import *

urlpatterns = [
    path('get/', getProjectsView.as_view(), name='get_projects'),
    path('create/', createProjectView.as_view(), name='create_project'),
    path('update/<uuid:pk>/', updateProjectView.as_view(), name='update_project'),
    path('delete/<uuid:pk>/', deleteProjectView.as_view(), name='delete_project'),
    
    path('contact/', contactFormView.as_view(), name='contact_form'),
]
