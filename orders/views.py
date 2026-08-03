from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse
from .models import Order, RiceType, Protein, OrderLog
from .forms import OrderForm  # ← تأكد من هذا السطر

def home(request):
    """الصفحة الرئيسية"""
    recent_orders = Order.objects.all().order_by('-order_date')[:6] if request.user.is_staff else []
    
    context = {
        'recent_orders': recent_orders,
        'is_kitchen_owner': request.user.is_staff,
    }
    return render(request, 'orders/home.html', context)

def menu(request):
    """عرض قائمة الأرز والإدام"""
    rice_types = RiceType.objects.filter(is_available=True)
    proteins = Protein.objects.filter(is_available=True)
    
    context = {
        'rice_types': rice_types,
        'proteins': proteins,
    }
    return render(request, 'orders/menu.html', context)

@login_required
def create_order(request):
    """تقديم طلب جديد"""
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer = request.user
            order.save()
            
            messages.success(request, '🎉 تم تقديم طلبك بنجاح! سنتواصل معك قريباً.')
            return redirect('orders:order_detail', order_id=order.id)
    else:
        form = OrderForm()
    
    context = {
        'form': form,
        'rice_types': RiceType.objects.filter(is_available=True),
        'proteins': Protein.objects.filter(is_available=True),
    }
    return render(request, 'orders/create_order.html', context)

@login_required
def my_orders(request):
    """عرض طلبات المستخدم الحالي"""
    orders = Order.objects.filter(customer=request.user).order_by('-order_date')
    
    context = {
        'orders': orders,
    }
    return render(request, 'orders/my_orders.html', context)

@login_required
def order_detail(request, order_id):
    """عرض تفاصيل طلب محدد"""
    order = get_object_or_404(Order, id=order_id)
    
    if order.customer != request.user and not request.user.is_staff:
        messages.error(request, 'ليس لديك صلاحية لعرض هذا الطلب.')
        return redirect('orders:my_orders')
    
    context = {
        'order': order,
    }
    return render(request, 'orders/order_detail.html', context)

@login_required
def cancel_order(request, order_id):
    """إلغاء طلب (فقط إذا كان جديداً)"""
    order = get_object_or_404(Order, id=order_id, customer=request.user)
    
    if order.status == 'جديد':
        order.status = 'ملغي'
        order.save()
        messages.success(request, 'تم إلغاء الطلب بنجاح.')
    else:
        messages.error(request, 'لا يمكن إلغاء هذا الطلب لأنه قيد التجهيز أو جاهز.')
    
    return redirect('orders:my_orders')

# ===================== واجهة المطبخ =====================

@staff_member_required
def kitchen_dashboard(request):
    """لوحة تحكم المطبخ"""
    from django.utils import timezone
    
    total_orders = Order.objects.count()
    new_orders = Order.objects.filter(status='جديد').count()
    preparing_orders = Order.objects.filter(status='قيد التجهيز').count()
    ready_orders = Order.objects.filter(status='جاهز').count()
    completed_orders = Order.objects.filter(status='مكتمل').count()
    cancelled_orders = Order.objects.filter(status='ملغي').count()
    
    active_orders = Order.objects.filter(
        status__in=['جديد', 'قيد التجهيز', 'جاهز']
    ).order_by('-order_date')
    
    all_orders = Order.objects.all().order_by('-order_date')
    
    today = timezone.now().date()
    today_orders = Order.objects.filter(order_date__date=today).count()
    
    context = {
        'active_orders': active_orders,
        'all_orders': all_orders,
        'total_orders': total_orders,
        'new_orders': new_orders,
        'preparing_orders': preparing_orders,
        'ready_orders': ready_orders,
        'completed_orders': completed_orders,
        'cancelled_orders': cancelled_orders,
        'today_orders': today_orders,
    }
    return render(request, 'orders/kitchen_dashboard.html', context)

@staff_member_required
def update_order_status(request, order_id):
    """تحديث حالة الطلب (Ajax)"""
    if request.method == 'POST':
        order = get_object_or_404(Order, id=order_id)
        new_status = request.POST.get('status')
        
        if new_status in dict(Order.STATUS_CHOICES):
            old_status = order.status
            order.status = new_status
            order.save()
            
            # تسجيل التغيير
            OrderLog.objects.create(
                order=order,
                old_status=old_status,
                new_status=new_status,
                changed_by=request.user
            )
            
            return JsonResponse({'success': True, 'status': order.status})
    
    return JsonResponse({'success': False}, status=400)

@staff_member_required
def all_orders(request):
    """عرض جميع الطلبات"""
    orders = Order.objects.all().order_by('-order_date')
    
    status_filter = request.GET.get('status')
    if status_filter:
        orders = orders.filter(status=status_filter)
    
    meal_time_filter = request.GET.get('meal_time')
    if meal_time_filter:
        orders = orders.filter(meal_time=meal_time_filter)
    
    context = {
        'orders': orders,
        'status_choices': Order.STATUS_CHOICES,
        'meal_time_choices': Order.MEAL_TIME_CHOICES,
        'current_status': status_filter,
        'current_meal_time': meal_time_filter,
    }
    return render(request, 'orders/all_orders.html', context)