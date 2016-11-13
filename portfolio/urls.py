from django.conf.urls import url
from . import views


urlpatterns = [
    # url(r'^(?P<project_name>[-_: a-zA-Z0-9]*)/$', views.project, name='project'),
    url(r'^', views.index, name='index'),
]
