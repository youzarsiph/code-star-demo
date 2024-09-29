""" API endpoints for code_star_demo.chats """

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from code_star.chats.models import Chat
from code_star_demo.chat.mixins import ChatContextMixin, OwnerFilterMixin, OwnerMixin


# Create your viewsets here.
class ChatsHomeView(generic.TemplateView):
    """CodeStar Chats demo home page"""

    template_name = "chats/index.html"


class ChatCreateView(
    ChatContextMixin,
    OwnerMixin,
    LoginRequiredMixin,
    generic.CreateView,
):
    """Create a new chat"""

    model = Chat
    fields = ["title", "description"]
    template_name = "chats/form.html"
    success_url = reverse_lazy("code-star:chats:list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ChatListView(
    OwnerFilterMixin,
    LoginRequiredMixin,
    generic.ListView,
):
    """List all chats"""

    model = Chat
    template_name = "chats/list.html"
    context_object_name = "chats"


class ChatDetailView(
    ChatContextMixin,
    OwnerFilterMixin,
    LoginRequiredMixin,
    generic.DetailView,
):
    """Detail view for a chat"""

    model = Chat
    template_name = "chats/details.html"
    context_object_name = "chat"


class ChatUpdateView(
    ChatContextMixin,
    OwnerFilterMixin,
    LoginRequiredMixin,
    generic.UpdateView,
):
    """Update a chat"""

    model = Chat
    fields = ["title", "description"]
    template_name = "chats/form.html"
    success_url = reverse_lazy("code-star:chats:list")


class ChatDeleteView(
    ChatContextMixin,
    OwnerFilterMixin,
    LoginRequiredMixin,
    generic.DeleteView,
):
    """Delete a chat"""

    model = Chat
    template_name = "chats/delete.html"
    success_url = reverse_lazy("code-star:chats:list")
