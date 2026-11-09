
from django.contrib import admin
from django.urls import path

from  sokoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('' ,views.index, name='index'),

    path('error/', views.error, name='error'),

    path('details/', views.details, name='details'),

    path('blog/', views.blog, name='blog'),

    path('portfolio/', views.portfolio, name='portfolio'),

    path('services/', views.service, name='services'),
    
    path('starter/', views.starter, name='starter'),




]
