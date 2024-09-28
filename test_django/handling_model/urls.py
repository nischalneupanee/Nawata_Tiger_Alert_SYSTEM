from django.urls import path
from . import views
urlpatterns = [
    path('live',views.live_view,name='live'),
    path('log',views.log_view,name='log')
]