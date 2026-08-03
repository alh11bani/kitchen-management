from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    # الصفحة الرئيسية
    path('', views.home, name='home'),
    
    # عرض قائمة الأرز والإدام
    path('menu/', views.menu, name='menu'),
    
    # تقديم طلب جديد
    path('order/new/', views.create_order, name='create_order'),
    
    # عرض طلبات المستخدم
    path('my-orders/', views.my_orders, name='my_orders'),
    
    # تفاصيل طلب محدد
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),
    
    # إلغاء طلب
    path('order/<int:order_id>/cancel/', views.cancel_order, name='cancel_order'),
    
    # ===== واجهة المطبخ (لصاحب المطبخ) =====
    path('kitchen/dashboard/', views.kitchen_dashboard, name='kitchen_dashboard'),
    
    # تغيير حالة الطلب
    path('kitchen/order/<int:order_id>/status/', views.update_order_status, name='update_order_status'),
    
    # عرض جميع الطلبات (لصاحب المطبخ)
    path('kitchen/all-orders/', views.all_orders, name='all_orders'),
]