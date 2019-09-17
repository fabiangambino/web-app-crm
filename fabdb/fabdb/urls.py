from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^profiles/', include('contacts.urls')),
    url(r'^results/', views.results_list),
    url(r'^dashboard/', views.dashboard),
    url(r'^search/', views.advanded_search),
    url(r'^$', views.login),
]

urlpatterns += staticfiles_urlpatterns()
