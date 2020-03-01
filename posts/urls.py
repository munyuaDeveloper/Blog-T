from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^details/(?P<post_id>\d+)/$', views.details, name='details')
    # THis url takes one parameter which is the post id
]
