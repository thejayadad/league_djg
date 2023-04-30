from django.urls import path, include


from . import views

app_name = 'posts'


urlpatterns = [
    path('', views.GroupPage.as_view(), name='all')
]