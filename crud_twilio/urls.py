from django.urls import path
from . import views  # Importing our views to be used in urls

urlpatterns = [
    path("", views.homepage, name="home"),  # Lets assign our homepage view to a path
]
