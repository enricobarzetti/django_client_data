from django.conf.urls import patterns, include, url
from django.contrib import admin

from django_client_data.tests.test_app.views import IndexView

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^admin/', include(admin.site.urls)),
)
