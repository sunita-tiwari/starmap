from django.views.generic import TemplateView


class ViewSiteCreateStarMap(TemplateView):
    """
    This class is used for create star map
    """

    template_name = "site/create_star_map.html"