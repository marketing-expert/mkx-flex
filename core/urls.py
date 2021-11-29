"""
core URL Configuration
"""

from django.contrib import admin
from django.conf import settings
from django.views import generic
from django.shortcuts import render
from django.urls import path, include
from django.contrib.auth import views
from django.conf.urls.static import static

admin.site.site_header = "FLEX VISITORS"
admin.site.site_title = admin.site.site_header
admin.site.index_title = f"WELCOME TO {admin.site.site_header}"


urlpatterns = [
    path(route='', view=generic.TemplateView.as_view(
        template_name="board.html",
        extra_context={"page_title": "dashboard"}
    ), name='dashboard'),

    path(route='login/', view=views.LoginView.as_view(
        template_name="login.html",
        extra_context={"page_title": "connexion"}
    ), name='login'),
    path(route='deconnexion/', view=views.LogoutView.as_view(), name='logout'),

    path('flex/', include('flex.urls', namespace='flex')),
    path('max/', include('max.urls', namespace='max')),
    
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path(settings.ADMIN_URL, admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )
