from django.urls import path

from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    # path("v1/", views.v1, name="view 1"),
    # path("route1/", views.route1, name="route1"),
    path("<int:id>", views.index, name="index"),
    path("", views.home, name="home"),
    # path("list/", views.list, name="list")
]
