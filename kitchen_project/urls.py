
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
     path('reset-password/', reset_admin_password, name='reset_password')
    path('', include('orders.urls')),      # الصفحة الرئيسية والطلبات
    path('accounts/', include('accounts.urls')),  # المصادقة
]

# إضافة مسارات الملفات الثابتة في وضع التطوير
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)