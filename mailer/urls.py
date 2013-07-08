from django.conf.urls.defaults import *
from django.conf import settings

import views

urlpatterns = patterns('',
    (r'^t$', views.bug),
    (r'^i$', views.iframe),
    (r'^c$', views.click),
)
