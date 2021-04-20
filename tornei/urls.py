from django.urls import path
from . import views

app_name="tornei"
urlpatterns = [
    path('', views.indexTornei, name="indexTornei"),
]
