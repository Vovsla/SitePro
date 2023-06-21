from django.urls import path

from .views import sova_index

app_name = 'sovamain'
urlpatterns = [
    path("", sova_index, name="main"),
]
