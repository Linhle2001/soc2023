from django.urls import path, include
from . import views
urlpatterns = [
    path('getshoesbyname<str:name>/', views.getshoesbyname),
    path('getshoes<str:id>/', views.getshoes ),
    path('addshoes/', views.newshoes),
    path('getshoesbycategory<str:category>/', views.getshoesbycategory),
]
