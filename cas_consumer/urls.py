from django.conf.urls import *

from cas_consumer.views import *

urlpatterns = [
    url(r'^login/', login, name="cas_login"),
    url(r'^logout/', logout, name="cas_logout"),
]
