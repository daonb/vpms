from django.conf.urls import patterns, include, url
#import volunteers.views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'vpms.views.home', name='home'),
	# url(r'^vpms/', include('vpms.foo.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^', include('volunteers.urls')),
	# Uncomment the admin/doc line below to enable admin documentation:
	# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
)
