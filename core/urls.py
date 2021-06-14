from django.urls import path
from . import views
urlpatterns = [
    path('core', views.index, name='core'),
    path('core/update_profile', views.profile_info, name='update_profile')
]
