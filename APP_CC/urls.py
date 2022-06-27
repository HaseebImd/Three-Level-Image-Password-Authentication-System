
from django.contrib import admin
from django.urls import path
from .views import Index, LoginByEmailPassword, LoginEP, SignUpEP, LoginbyPic, SignUpByEmailPassword, SignUpbyPic, Home

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', Index.as_view()),
    path('login', LoginEP.as_view()),
    path('signup', SignUpEP.as_view()),
    path('loginbyEmailPass', LoginByEmailPassword.as_view()),
    path('signupbyEmailPass', SignUpByEmailPassword.as_view()),
    path('loginbyPic', LoginbyPic.as_view()),
    path('signnbyPic', SignUpbyPic.as_view()),
    path('homepage',Home.as_view())
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
