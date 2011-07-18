from django.contrib.auth import views as auth_views

from django.conf.urls.defaults import patterns, url

from commons import jinja_for_django

from . import views

# So we can use the contrib logic for password resets, etc.
auth_views.render_to_response = jinja_for_django


urlpatterns = patterns('',
    url(r'^login', views.login, name='login'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^register', views.register, name='register'),
)
