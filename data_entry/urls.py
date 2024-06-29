from django.urls import path
from . import views

urlpatterns = [
    path('data_entry/', views.set_data_entry, name='set_data_entry'),
    path('pengguna/', views.set_pengguna, name='set_pengguna'),
    path('pengguna/view/<id>', views.view_pengguna, name='view_pengguna'),
    path('api/pengguna/<int:user_id>/', views.get_pengguna_detail_api, name='get_pengguna_detail_api'),
    path('content/', views.set_content, name='set_content'),
    path('pengguna/edit/<int:id>/', views.edit_pengguna, name='edit_pengguna'),
    path('pengguna/set/', views.set_pengguna, name='set_pengguna'),
    path('main/', views.main_view, name='main'),
    path('pengguna/listpenggunabystate', views.search_pengguna_by_state, name='search_pengguna_by_state'),
]