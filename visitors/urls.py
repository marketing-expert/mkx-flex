# visitors.urls.py

from django.urls import path
from django.views import generic

from visitors import views


app_name = 'visitors'
urlpatterns = [
    path(route="", view=generic.TemplateView.as_view(
        template_name="index.html",
        extra_context={"page_title": "dashboard"}
    ), name="home"),
    path(route="add/v/", view=views.visitor_create_view, name="add_visitor"),
    path(route="vl/", view=views.visitor_list_view, name="list_visitor")
]
