# visitors.urls.py

from django.urls import path
from django.views import generic

from max import views


app_name = 'max'
urlpatterns = [
    path(route="", view=views.max_dashboard, name="home"),
    path(route="list/souscribers/", view=views.max_soucriber_list, name="max_list_path"),
    path(route="add/souscriber/", view=views.max_suscriber_create, name="max_create_path"),
    path(route="detail/<pk>/", view=views.max_souscriber_detail, name="max_detail_path"),
    path(route="update/<pk>/", view=views.max_suscriber_update, name="max_update_path"),
    path(route='search/', view=views.search_view, name="search"),
]
