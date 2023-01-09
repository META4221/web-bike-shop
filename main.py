from django.template.loader import render_to_string
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class ErrorView(TemplateView):
    template_name = '404.html'


class AccessoriesView(TemplateView):
    template_name = 'accessories.html'


class BicyclesView(TemplateView):
    template_name = 'bicycles.html'


class CartView(TemplateView):
    template_name = 'cart.html'


class PartsView(TemplateView):
    template_name = 'parts.html'


class SingleView(TemplateView):
    template_name = 'single.html'
