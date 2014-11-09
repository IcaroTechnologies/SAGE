from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import home, agregar, menu, crearEst

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SAGE.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home),
    url(r'^menu', menu ),
    url(r'^agregar',agregar),
    url(r'^crearEst',crearEst),
)
