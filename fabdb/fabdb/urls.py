from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.login, name="login"),
    url(r'^notes/', include('notes.urls')),
    url(r'^profiles/', include('contacts.urls')),
    url(r'^results/', views.results),
    url(r'^search/', views.advanced_search),
    url(r'^dashboard/', views.dashboard),
]

urlpatterns += staticfiles_urlpatterns()
