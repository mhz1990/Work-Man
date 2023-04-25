from accounts.views import user_login, user_signup
from django.urls import path


urlpatterns = [
    path("login/", user_login, name="login"),
    path("signup/", user_signup, name="signup"),
]
