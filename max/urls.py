# visitors.urls.py

from django.urls import path
from django.views import generic

from max import views


app_name = 'max'
urlpatterns = [
    path(route="", view=views.soucriber_list, name="list_souscriber"),
    path(route="d/<slug>/", view=views.souscriber_detail, name="detail_soucriber"),
    path(route="add/", view=views.suscriber_create, name="create_souscriber"),
]
