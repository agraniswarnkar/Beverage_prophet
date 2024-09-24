from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name='index'),
    #path("sections/<int:num>", views.section, name='section'),
    path('service/', views.service, name='service'),
    path('help/', views.help, name='help'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('datapresenting/', views.datapresenting, name='datapresenting'),
    #path('fetch-stock-data', views.fetch_stock_data, name='fetch_stock_data'),
    path('service/', views.service_page, name='service_page')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
