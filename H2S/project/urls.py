from django.urls import path
from . import views
urlpatterns = [
    # path("base/",views.base,name="base"),
    path("", views.submit, name="submit"),
    path("analyze/", views.analyze_text, name="analyze"),  
]