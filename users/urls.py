from django.urls import path
from . import views
from users import views as userViews
from django.contrib.auth import views as authViews

urlpatterns = [
    path('reg/', views.register, name='register'),
    path('profile/', userViews.profile, name='profile'),
    path('user/', authViews.LoginView.as_view(template_name='users/user.html'), name='user'),
    path('exit/', authViews.LogoutView.as_view(template_name='users/exit.html'), name='exit'),
    path('pass-reset/', authViews.PasswordResetView.as_view(template_name='users/pass-reset.html'), name='pass-reset'),
    path('password_reset_complete/', authViews.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    path('password_reset_confirm/<uidb64>/<token>/', authViews.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_done/', authViews.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),

]
