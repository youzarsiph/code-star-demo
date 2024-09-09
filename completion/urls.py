""" URLConf for code_star_demo.completions """

from django.urls import path

from code_star_demo.completion import views


# Create your URLConf here.
app_name = "completions"

urlpatterns = [
    path("", views.CompletionsHomeView.as_view(), name="home"),
]
