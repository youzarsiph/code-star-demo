""" URLConf for code_star_demo.chats """

from django.urls import path

from code_star_demo.chat import views


# Create your URLConf here.
app_name = "chats"

urlpatterns = [
    path("", views.ChatsHomeView.as_view(), name="home"),
    path("new/", views.ChatCreateView.as_view(), name="create"),
    path("chats/", views.ChatListView.as_view(), name="list"),
    path("chats/<int:pk>/", views.ChatDetailView.as_view(), name="details"),
    path("chats/<int:pk>/update/", views.ChatUpdateView.as_view(), name="update"),
    path("chats/<int:pk>/delete/", views.ChatDeleteView.as_view(), name="delete"),
]
