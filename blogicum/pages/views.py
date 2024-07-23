from django.views.generic.base import TemplateView
from django.shortcuts import render


class AboutPageView(TemplateView):

    template_name = 'pages/about.html'


class RulesPageView(TemplateView):

    template_name = 'pages/rules.html'


def page_not_found(request, exception):
    return render(request, 'pages/404.html', status=404)


def csrf_failure(request, reason=''):
    return render(request, 'pages/403csrf.html', status=403)


def custom_500(request):
    return render(request, 'pages/500.html', status=500)
