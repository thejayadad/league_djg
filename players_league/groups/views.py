from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class GroupPage(TemplateView):
    template_name = 'groups/group_list.html'



