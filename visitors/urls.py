# visitors.urls.py

from django.urls import path

from visitors import views


app_name = 'visitors'
urlpatterns = [
    path(route="", view=views.visitor_create_view, name="add_visitor")
]
