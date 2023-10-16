from django.urls import path

from .views import site_index_view

urlpatterns = [
    path('', site_index_view, name='site_index'),
]
