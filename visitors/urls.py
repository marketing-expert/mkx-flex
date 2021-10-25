# visitors.urls.py

from django.urls import path
from django.views import generic

from visitors import views


app_name = 'visitors'
urlpatterns = [
    path(route="", view=generic.TemplateView.as_view(
        template_name="index.html"
    ), name="home"),
    path(route="register/visitor/", view=views.visitor_create_view, name="add_visitor"),
    path(route="visitors/", view=views.visitor_list_view, name="list_visitor")
]
