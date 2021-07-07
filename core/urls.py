from django.urls import path
from . import views


urlpatterns = [
    path('core', views.index, name='core'),
    path('core/update_profile/<int:id_user>', views.profile_info.as_view(), name='update_profile'),
    path('core/users', views.users_info, name='users_info'),
    #path('core/updated/<int:id_user>', views.update_profile, name='updated'),
]
