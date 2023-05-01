
from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = 'accounts/index.html'


class ThanksPage(TemplateView):
    template_name = 'accounts/thanks.html'