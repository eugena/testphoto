from django.conf.urls import url
from django.views.generic import TemplateView

from .views import PhotoListView


urlpatterns = [
    url(r'^(?P<slug>[\w\,]+)/?$', PhotoListView.as_view()),
    url(r'^(?P<slug>[\w\,]+)/sortby(?P<sort>[\-\w]+)/?$', PhotoListView.as_view()),
    url(r'$', TemplateView.as_view(template_name='index.html'), )  ]