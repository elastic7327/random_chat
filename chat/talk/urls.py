
from django.conf.urls import url
from talk.views import log_out, log_in,sign_up,user_list


urlpatterns = [

    url(r'^log_in/$', log_in, name='log_in'),
    url(r'^log_out/$', log_out, name='log_out'),
    url(r'^sign_up/$', sign_up, name='sign_up'),
    url(r'^$', user_list, name='user_list')


]
