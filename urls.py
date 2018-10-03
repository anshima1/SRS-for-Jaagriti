"""
Definition of urls for DjangoWebProject2.
"""

from django.conf.urls import include, url
from first_app import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [

    url(r'^$',views.index,name='index'),
    url(r'^first_app/',include('first_app.urls')),
    # Examples:
    # url(r'^$', DjangoWebProject2.views.home, name='home'),
    # url(r'^DjangoWebProject2/', include('DjangoWebProject2.DjangoWebProject2.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
