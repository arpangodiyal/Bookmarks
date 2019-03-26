from django.urls import include, path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('edit', views.edit, name='edit'),
    path('register', views.register, name='register'),
    path('', views.dashboard, name='dashboard'),
    path(
        'password_change',
        auth_views.PasswordChangeView.as_view(template_name='change-password.html'),
        name='password_change'
    ),
    path('password_change_done',
        auth_views. PasswordChangeDoneView.as_view(template_name='passwordChangeDone.html'),
        name='password_change_done'
    ),
    path('password-reset/',
        auth_views.PasswordResetView.as_view(
            template_name='passwordReset.html'
        ),
        name='password_reset'
    ),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='passwordResetDone.html'
         ),
         name='password_reset_done'
    ),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='passwordResetConfirm.html'
         ),
         name='password_reset_confirm'
    ),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='passwordResetComplete.html'
         ),
         name='password_reset_complete'
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)