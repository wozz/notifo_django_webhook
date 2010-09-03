from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'^notifo$', '<SITENAME>.<APPNAME>.views.notifo_webhook'),
)

