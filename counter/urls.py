from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("save", views.save, name="save"),# url parameter
    path("model", views.get_model_results, name="model") # url parameter
]
