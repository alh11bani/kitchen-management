from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    # صفحة تسجيل الدخول
    path('login/', auth_views.LoginView.as_view(
        template_name='accounts/login.html',
        redirect_authenticated_user=True
    ), name='login'),
    
    # صفحة تسجيل الخروج
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # صفحة التسجيل (إنشاء حساب جديد)
    path('register/', views.register, name='register'),
    
    # الملف الشخصي
    path('profile/', views.profile, name='profile'),
    
    # تعديل الملف الشخصي
    path('profile/edit/', views.edit_profile, name='edit_profile'),
]