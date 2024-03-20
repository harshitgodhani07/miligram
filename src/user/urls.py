from django.urls import path
from user.views import UserCreateView, UserLoginView

urlpatterns = [
    path("create", UserCreateView.as_view()),
    path("login", UserLoginView.as_view()),
]