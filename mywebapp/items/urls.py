from django.urls import path, re_path
from django.views.generic.base import RedirectView

from . import views

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^favicon\.ico$', favicon_view),
]
