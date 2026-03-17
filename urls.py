from django.contrib import admin
from django.urls import path
from django.urls import include

from End_user_web import views

urlpatterns = [
    path('',views.s_log,name='s_log'),

    path('stud_home/',views.stud_home,name='stud_home'),
    path('stud_reg/',views.stud_reg,name='stud_reg'),
    path('attend/',views.attend, name='attend'),
    path('att_conf/',views.att_conf, name='att_conf'),
    path('camera_feed', views.camera_feed, name='camera_feed'),
    path('detect_barcodes', views.detect, name='detect_barcodes'),
    path('qrPage/',views.attend, name='qrPage'),
]
