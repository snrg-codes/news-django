from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns = [
    path('', views.home, name='domashniye_kotleti'),
    path('topic/<nazvaniye_temi>/', views.filtr_po_temam, name='filtr_po_temam'),
    path('topic/<post_slug>', views.otkrit_post, name='otkrit_post'),
]

