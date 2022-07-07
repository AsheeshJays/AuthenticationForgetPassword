from django.urls import path 
from mainApp import views

urlpatterns = [
    path('',views.HomePage,name='homepage'),
    path('dashboard/',views.DashBoardPage,name='dashboard'),
    path('signup/',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('logout/' ,views.LogoutPage,name='logout'),
    path('forgetpassword/',views.ForgetPasswordPage,name='forgetpassword'),
    path('enterotp/<str:username>/',views.enterotp,name='enterotp'),
    path('resetpassword/<str:username>/',views.resetPassword,name='resetpassword'),
]
