from django.urls import path
from . import views


urlpatterns = [
    path('core', views.index, name='core'),
    path('core/update_profile/<int:id_user>', views.profile_info.as_view(), name='update_profile'),
    path('core/users', views.users_info.as_view(), name='users_info'),
    path('core/consultas', views.consultas.as_view(), name='consultas'),
    path('core/recetas', views.recetas.as_view(), name='recetas'),
    path('core/citas', views.citas.as_view(), name='citas'),
    path('core/equipos', views.equipos.as_view(), name='equipos'),
    #path('core/updated/<int:id_user>', views.update_profile, name='updated'),
]
