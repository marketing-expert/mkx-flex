# flex.urls.py

from django.urls import path
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from flex import views


app_name = 'flex'
urlpatterns = [
    path(route="", view=views.flex_dashboard, name="home"),
    path(route="add/visitor/", view=views.flex_create_visitor_view, name="add_visitor"),
    path(route="list/visitors/", view=views.flex_list_visitor_view, name="list_visitor")
]
