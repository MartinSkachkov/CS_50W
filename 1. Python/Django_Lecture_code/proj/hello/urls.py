from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"), # localhost/hello/
    path("marto", views.marto, name="marto"), # localhost/hello/marto
    path("david", views.david, name="david"), # localhost/hello/david
    path("<str:name>", views.greet, name="greet") # what the user enters after localhost/hello/<name> will be saved ti name & passed to greet function
]
