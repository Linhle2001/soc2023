
from django.urls import path, include
from . import views
urlpatterns = [
    path("add_to_cart/", views.add_to_cart ),
    path('getcartbyusername<str:uname>/<str:proid>/', views.getcartbyusernameandproid),
]