""" API endpoints for code_star_demo.chats """

from django.urls import reverse_lazy
from django.views import generic

from code_star.chats.models import Chat


# Create your viewsets here.
class ChatsHomeView(generic.TemplateView):
    """CodeStar Chats demo home page"""

    template_name = "chats/index.html"


class ChatCreateView(generic.CreateView):
    """Create a new chat"""

    model = Chat
    fields = ["title", "description"]
    template_name = "chats/form.html"
    success_url = reverse_lazy("chats:list")


class ChatListView(generic.ListView):
    """List all chats"""

    model = Chat
    template_name = "chats/list.html"
    context_object_name = "chats"


class ChatDetailView(generic.DetailView):
    """Detail view for a chat"""

    model = Chat
    template_name = "chats/details.html"
    context_object_name = "chat"


class ChatUpdateView(generic.UpdateView):
    """Update a chat"""

    model = Chat
    fields = ["title", "description"]
    template_name = "chats/form.html"
    success_url = reverse_lazy("chats:list")


class ChatDeleteView(generic.DeleteView):
    """Delete a chat"""

    model = Chat
    template_name = "chats/delete.html"
    success_url = reverse_lazy("chats:list")
