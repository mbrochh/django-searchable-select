from django.urls import re_path

try:
    # Django <=1.9
    from django.conf.urls import patterns
except ImportError:
    # Django 1.10+
    patterns = None
from . import views


urls = [
    re_path('^filter$', views.filter_models, name='searchable-select-filter'),
]

if patterns:
    urlpatterns = patterns('', *urls)
else:
    urlpatterns = urls
