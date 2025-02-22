from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.custom_logout, name='logout'),  # Usa la vista personalizada
    path('editar/', views.editar_view, name='editar'),
    path('delete/<int:post_id>/', views.delete_post, name='delete'),  
    path('register/', views.register_view, name='register'),
    path('login/', LoginView.as_view(template_name='twitter/login.html'), name='login'),
    path('profile/<str:username>/', views.profile, name='profile'),  # Corregido srt -> str
    path('follow/<str:username>/', views.follow, name='follow'),
    path('unfollow/<str:username>/', views.unfollow, name='unfollow'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



