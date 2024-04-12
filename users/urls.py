from django.urls import path
from users.views import (
    UserRegistrationView,
    UserLoginView,
    SendPasswordResetEmailView,
    UserPasswordResetView,
    CheckEmailExistsView,
    UserLogoutView,
    UserProfileView,
    UserChangePasswordView,
    RefreshTokenView,
    UserProfileImageView,
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("check-email/", CheckEmailExistsView.as_view(), name="check_email_exists"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("profile/", UserProfileView.as_view(), name="profile"),
    path("change-password/", UserChangePasswordView.as_view(), name="change-password"),
    path(
        "send-reset-password-email/",
        SendPasswordResetEmailView.as_view(),
        name="send-reset-password-email",
    ),
    path(
        "reset-password/<uid>/<token>/",
        UserPasswordResetView.as_view(),
        name="reset-password",
    ),
    path("refresh-token/", RefreshTokenView.as_view(), name="refresh-token"),
    path("profile/", UserProfileImageView.as_view(), name="user-profile"),
]

# Ajoutez ces lignes pour servir les fichiers médias en mode développement.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
