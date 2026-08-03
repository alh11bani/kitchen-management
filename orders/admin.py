from django.contrib import admin

# Register your models here.

from .models import RiceType, Protein, Order, OrderLog

@admin.register(RiceType)
class RiceTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_available')
    list_filter = ('is_available',)
    search_fields = ('name', 'description')
   # readonly_fields = ('created_at', 'updated_at')
    list_editable = ('price', 'is_available')

@admin.register(Protein)
class ProteinAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_available')
    list_filter = ('is_available',)
    search_fields = ('name', 'description')
   # readonly_fields = ('created_at', 'updated_at')
    list_editable = ('price', 'is_available')

class OrderLogInline(admin.TabularInline):
    model = OrderLog
    extra = 0
    readonly_fields = ('old_status', 'new_status', 'changed_by', 'changed_at')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'customer', 'rice_type', 'protein', 
        'number_of_people', 'meal_time', 'total_price', 
        'status', 'order_date'
    )
    list_filter = ('status', 'meal_time', 'order_date', 'rice_type', 'protein')
    search_fields = ('customer__username', 'customer__email', 'phone', 'notes')
    readonly_fields = (
        'rice_price', 'protein_price', 'total_price', 
        'order_date', 'updated_at'
    )
    list_editable = ('status',)
    inlines = [OrderLogInline]
    fieldsets = (
        ('معلومات الزبون', {
            'fields': ('customer', 'phone')
        }),
        ('تفاصيل الطلب', {
            'fields': ('rice_type', 'protein', 'number_of_people', 'meal_time', 'notes')
        }),
        ('الأسعار', {
            'fields': ('rice_price', 'protein_price', 'total_price'),
            'classes': ('collapse',)
        }),
        ('الحالة والمواعيد', {
            'fields': ('status', 'pickup_time', 'order_date', 'updated_at')
        }),
    )

@admin.register(OrderLog)
class OrderLogAdmin(admin.ModelAdmin):
    list_display = ('order', 'old_status', 'new_status', 'changed_by', 'changed_at')
    list_filter = ('old_status', 'new_status', 'changed_at')
    search_fields = ('order__id', 'notes')
    readonly_fields = ('order', 'old_status', 'new_status', 'changed_by', 'changed_at')