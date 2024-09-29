""" API endpoints for code_star_demo.completions """

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


# Create your viewsets here.
class CompletionsHomeView(TemplateView):
    """CodeStar Completions demo home page"""

    template_name = "completions/index.html"


class CompletionView(LoginRequiredMixin, TemplateView):
    """Code editor for demonstrating CodeStar code completions"""

    template_name = "completions/editor.html"
