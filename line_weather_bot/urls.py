from django.conf.urls import include, url

from line_weather_bot import views

urlpatterns = [
    url('^callback/', views.callback, name='callback'),
]
