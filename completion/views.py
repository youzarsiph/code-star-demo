""" API endpoints for code_star_demo.completions """

from django.views import generic


# Create your viewsets here.
class CompletionsHomeView(generic.TemplateView):
    """CodeStar Completions demo home page"""

    template_name = "completions/index.html"
