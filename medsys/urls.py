from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='medsys'),
    path('new_request', views.new_request, name='new_request')
]
