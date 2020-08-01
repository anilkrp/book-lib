from django.urls import path

from .views import HomePageView,AboutBookView,SayBookView,Form,Img,Wellcome
urlpatterns = [
    path('home',HomePageView.as_view(),name='home'),
    path('about',AboutBookView.as_view(),name='about'),
    path('info',SayBookView.as_view(),name='info'),
    path('form',Form.as_view(),name='form'),
    path('img',Img.as_view(),name='img'),
    path('',Wellcome.as_view(),name='wellcome')
]
