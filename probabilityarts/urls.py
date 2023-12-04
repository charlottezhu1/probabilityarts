from django.urls import path
from . import views

# URLConf module
urlpatterns = [
    path('', views.index,name="probabilityarts"),
    path('create', views.create_art,name="create-art"),
]
