from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('editar/', views.editar_view, name='editar'),
    path('delete/<int:post_id>/', views.delete_post, name='delete'),  
    path('register/', views.register_view, name='register'),
]
