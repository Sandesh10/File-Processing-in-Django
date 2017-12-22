from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

from django.contrib import admin
from data import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^upload/$', views.home, name='fileupload'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

