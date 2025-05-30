from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='domashniye_kotleti'),
    path('topic/<nazvaniye_temi>/', views.filtr_po_temam, name='filtr_po_temam'),
    path('topic/<post_title>', views.otkrit_post, name='otkrit_post'),
]