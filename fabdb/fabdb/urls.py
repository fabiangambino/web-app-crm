from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^profiles/', include('contacts.urls')),
    url(r'^about/', views.about),
    url(r'^login/', views.login),
    url(r'^results/', views.results_list),
    url(r'^dashboard/', views.dashboard),
    url(r'^search/', views.advanded_search),
    url(r'^$', views.homepage),
]
