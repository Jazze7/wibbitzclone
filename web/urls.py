from operator import index
from django.urls import include, path
from web.views import index, subscribe, contact


app_name = "web"


urlpatterns = [

    path("", index, name="index"),
    path("subscribe/", subscribe, name="subscribe"),
    path("contact/", contact, name="contact"),
]
