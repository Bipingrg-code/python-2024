from django.contrib import admin
from django.urls import path,include
from account.views import UserRegView, UserLoginView,UserProfileView,UserPasswordChangeView,UserSendPasswordRestEmailView,UserPasswordRestView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',UserRegView.as_view(),name='register'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('userProfile/',UserProfileView.as_view(),name='profile'),
    path('changepassword/',UserPasswordChangeView.as_view(), name = 'changepassword'),
    path('send-reset-password-email/',UserSendPasswordRestEmailView.as_view(),name='sent-reset-password-email'),
    path('reset-password/<uid>/<token>/',UserPasswordRestView.as_view(),name='rest-password')
]
