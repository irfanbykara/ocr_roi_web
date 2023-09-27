from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
path('convert_to_text/', views.convert_to_text, name='convert_to_text'),

]

