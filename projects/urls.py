from django.urls import path
from projects.views import project_list


urlpatterns = [
    path("", project_list, name="list_projects"),
]
