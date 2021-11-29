# flex.urls.py

from django.urls import path
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from flex import views


app_name = 'flex'
urlpatterns = [
    path(route="", view=views.visitor_dashboard, name="home"),
    path(route="add/", view=views.visitor_create_view, name="add_visitor"),
    path(route="list/", view=views.visitor_list_view, name="list_visitor")
]
