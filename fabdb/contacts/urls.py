from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.contacts),
    url(r'^contact/', views.contact_view),

]
