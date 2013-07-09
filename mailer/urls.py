from django.conf.urls.defaults import *
from django.conf import settings

import views

urlpatterns = patterns('',
    (r'^t$', views.bug, {}, 'bug'),
    (r'^i$', views.iframe, {}, 'iframe'),
    (r'^c$', views.click, {}, 'click'),
)
