from django.conf.urls import patterns, include, url
from django.contrib import admin
from SAGE.views import home, agregar, menu, crearEst, cliente, solicitar,\
                  reservar, pagar, estacionamientos_registrados, datos_estacionamiento,\
                  confirmarPago, reservas_registradas, datos_pago

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SAGE.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home),
    url(r'^menu', menu ),
    url(r'^agregar',agregar),
    url(r'^crearEst',crearEst),
    url(r'^estacionamientos_registrados',estacionamientos_registrados),
    url(r'^datos_estacionamiento/(?P<id>[0-9]+)',datos_estacionamiento),
    url(r'^cliente',cliente),
    url(r'^solicitar',solicitar),
    url(r'^reservar',reservar),
    url(r'^pagar',pagar),
    url(r'^confirmarPago',confirmarPago),
    url(r'^reservas_registradas',reservas_registradas),
    url(r'^datos_pago/(?P<id>[0-9]+)',datos_pago)
)
