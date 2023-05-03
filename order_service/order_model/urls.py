from django.urls import path, include
from . import views
urlpatterns = [
    path("initiate_model/",views.add_to_order),
]