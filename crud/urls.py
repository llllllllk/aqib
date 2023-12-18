from django.urls import path, include
from crud import views
urlpatterns = [
    path("aqib/", views.aqib),
    path("saqib/", views.saqib),

]
