""" CodeStar demo views """

from django.views import generic


# Create your viewsets here.
class HomeView(generic.TemplateView):
    """CodeStar Home page"""

    template_name = "code_star_demo/index.html"
