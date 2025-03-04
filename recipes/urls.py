from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('add/', views.add_recipe, name='add_recipe'),
    path('edit/<int:recipe_id>/', views.edit_recipe, name='edit_recipe'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('accounts/password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('user/<str:username>/', views.user_recipes, name='user_recipes'),  # Убедитесь, что этот маршрут присутствует
]
