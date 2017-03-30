from django.conf.urls import url
from django.contrib import admin

from mentor001 import views

urlpatterns = [
url(r'^$', views.index, name='home'),
    url(r'^admin/', admin.site.urls),
]
