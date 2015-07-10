from django.conf.urls import patterns, include, url

from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('isvat.api.views',
	(r'^(..)/(.*?)/$', 'vat'),
)

urlpatterns += patterns('django.views.generic.simple',
	(r'^terms/', TemplateView.as_view(template_name='terms.html')),
	(r'^privacy/', TemplateView.as_view(template_name='privacy.html')),
	(r'^$', TemplateView.as_view(template_name='index.html')),
)

# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'isvat.views.home', name='home'),
#     # url(r'^isvat/', include('isvat.foo.urls')),

#     # Uncomment the admin/doc line below to enable admin documentation:
#     # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

#     # Uncomment the next line to enable the admin:
#     # url(r'^admin/', include(admin.site.urls)),
# )
