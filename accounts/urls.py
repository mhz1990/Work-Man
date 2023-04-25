from accounts.views import user_login, user_signup, user_logout
from django.urls import path


urlpatterns = [
    path("login/", user_login, name="login"),
    path("signup/", user_signup, name="signup"),
    path("logout/", user_logout, name="logout"),
]
