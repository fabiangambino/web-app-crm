from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^about/', views.about),
    url(r'^login/', views.login),
    url(r'^results/', views.results_list),
    url(r'^dashboard/', views.dashboard),
    url(r'^profile/', views.contact_view),
    url(r'^search/', views.advanded_search),
    url(r'^$', views.homepage),
]
