from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "accounts"
urlpatterns = [
    path('verification', views.verification_page, name='verify_page'),
    path('verify_user/<int:id>/', views.verify_user, name='verify_user'),

    path('register', views.register_view, name='register'),

    path('login', views.login_view, name='login'),
    path('dashboard',views.logged_in_dashboard,name='dashboard')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
