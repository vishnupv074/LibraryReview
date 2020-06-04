from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_view, name='login'),
    path('library_list_admin', views.library_list_admin_view, name='library_list_admin'),
    path('library_add', views.library_add_view, name='library_add'),
    path('library_edit/<int:id>', views.library_edit_view, name='library_edit'),
    path('library_delete/<int:id>', views.library_delete_view, name='library_delete'),
    path('logout', views.logout_view, name='logout'),
    path('', views.library_view, name='library_list'),
    path('library/<int:id>', views.library_detail_view, name="library_detail"),
    path('admin_library/<int:id>', views.admin_library_detail, name="admin_library_detail"),
]
