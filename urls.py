""" CodeStar demo URLConf """

from django.urls import path, include

from code_star_demo.views import HomeView


# Create your URLConf here.
app_name = "code-star"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("chat/", include("code_star_demo.chats.urls")),
    path("completions/", include("code_star_demo.completions.urls")),
]
