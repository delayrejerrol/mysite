from django.conf.urls import url
from . import views

app_name = 'polls'


urlpatterns = [
    # /polls/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /polls/<pk>
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # Set a specific URL
    # /polls/specific/<question_id>
    # url(r'^specific/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),

    # /polls/<pk>/results/
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),

    # /polls/<question_id>/vote
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]