from django.conf.urls import include, url


from django.contrib import admin

from auth.views import auth_code, auth_code_html

admin.autodiscover()

urlpatterns = [
# Examples:

    url(r'^admin/', include(admin.site.urls)),

    url(r'^get_auth/$', auth_code),
    url(r'^get_auth_html/$', auth_code_html)
]
