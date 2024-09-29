""" Mixins for code_star_demo.chats """

from typing import Any, Dict

from code_star.chats.models import Chat


# Create your mixins here.
class ChatContextMixin:
    """Adds common context variables to views"""

    def get_context_data(self, **kwargs: Dict) -> Dict[str, Any]:
        """Adds common context variables to views"""

        context = super().get_context_data(**kwargs)

        context["chats"] = Chat.objects.filter(user=self.request.user)

        return context


class OwnerMixin:
    """Adds the owner of the object when creating automatically"""

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class OwnerFilterMixin:
    """Filter queryset by owner"""

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
