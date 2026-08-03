from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from decimal import Decimal

# ==================== نموذج نوع الأرز ====================
class RiceType(models.Model):
    """
    نموذج أنواع الأرز المتوفرة في المطبخ
    """
    name = models.CharField(
        max_length=50, 
        verbose_name="اسم الأرز"
    )
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name="سعر النفر",
        help_text="سعر النفر الواحد بدون الإدام"
    )
    description = models.TextField(
        blank=True, 
        null=True, 
        verbose_name="وصف"
    )

    is_available = models.BooleanField(
        default=True, 
        verbose_name="متوفر"
    )


    def __str__(self):
        return f"{self.name} - {self.price} ريال"

    class Meta:
        verbose_name = "نوع الأرز"
        verbose_name_plural = "أنواع الأرز"
        ordering = ['name']

# ==================== نموذج الإدام ====================
class Protein(models.Model):
    """
    نموذج أنواع الإدام (اللحم/الدجاج/السمك)
    """
    name = models.CharField(
        max_length=50, 
        verbose_name="اسم الإدام"
    )
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name="سعر النفر",
        help_text="سعر النفر الواحد بدون الأرز"
    )
    description = models.TextField(
        blank=True, 
        null=True, 
        verbose_name="وصف"
    )

    is_available = models.BooleanField(
        default=True, 
        verbose_name="متوفر"
    )


    def __str__(self):
        return f"{self.name} - {self.price} ريال"

    class Meta:
        verbose_name = "الإدام"
        verbose_name_plural = "الإدامات"
        ordering = ['name']

# ==================== نموذج الطلب ====================
class Order(models.Model):
    """
    نموذج الطلب الرئيسي
    """
    
    # خيارات الميعاد
    MEAL_TIME_CHOICES = [
        ('غداء', 'غداء'),
        ('عشاء', 'عشاء'),
    ]
    
    # خيارات الحالة
    STATUS_CHOICES = [
        ('جديد', 'جديد'),
        ('قيد التجهيز', 'قيد التجهيز'),
        ('جاهز', 'جاهز'),
        ('مكتمل', 'مكتمل'),
        ('ملغي', 'ملغي'),
    ]
    
    # ===== العلاقات =====
    customer = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='orders',
        verbose_name="الزبون"
    )
    rice_type = models.ForeignKey(
        RiceType, 
        on_delete=models.PROTECT, 
        related_name='orders',
        verbose_name="نوع الأرز"
    )
    protein = models.ForeignKey(
        Protein, 
        on_delete=models.PROTECT, 
        related_name='orders',
        verbose_name="الإدام"
    )
    
    # ===== معلومات الطلب =====
    number_of_people = models.PositiveIntegerField(
        verbose_name="عدد النفار",
        help_text="كم شخص سيتناول الوجبة؟"
    )
    meal_time = models.CharField(
        max_length=10, 
        choices=MEAL_TIME_CHOICES, 
        verbose_name="الميعاد"
    )
    phone = models.CharField(
        max_length=15, 
        verbose_name="رقم الجوال",
        help_text="رقم الجوال للتواصل"
    )
    notes = models.TextField(
        blank=True, 
        null=True, 
        verbose_name="ملاحظات إضافية",
        help_text="مثل: بدون بهارات، زيادة أرز..."
    )
    
    # ===== الأسعار (تحفظ تلقائياً) =====
    rice_price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name="سعر الأرز للنفر",
        editable=False  # لا يمكن تعديله يدوياً
    )
    protein_price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name="سعر الإدام للنفر",
        editable=False  # لا يمكن تعديله يدوياً
    )
    total_price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name="السعر الإجمالي",
        editable=False  # لا يمكن تعديله يدوياً
    )
    
    # ===== الحالة والتواريخ =====
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='جديد', 
        verbose_name="الحالة"
    )
    order_date = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="تاريخ الطلب"
    )
    pickup_time = models.DateField(
        null=True, 
        blank=True, 
        verbose_name="يوم موعد الوجبة",
        help_text="يوم الوجبة  "
    )
    updated_at = models.DateTimeField(
        auto_now=True, 
        verbose_name="آخر تحديث"
    )

    def save(self, *args, **kwargs):
        """
        حفظ الطلب مع حساب الأسعار تلقائياً
        """
        if not self.pk:  # إذا كان الطلب جديداً
            self.rice_price = self.rice_type.price
            self.protein_price = self.protein.price
            self.total_price = (self.rice_price + self.protein_price) * self.number_of_people
        super().save(*args, **kwargs)

    def get_total_price_display(self):
        """عرض السعر الإجمالي مع العملة"""
        return f"{self.total_price:,.2f} ريال"
    get_total_price_display.short_description = "السعر الإجمالي"

    def get_order_summary(self):
        """ملخص الطلب"""
        return f"{self.rice_type.name} + {self.protein.name} - {self.number_of_people} نفر"

    def __str__(self):
        return f"طلب #{self.id} - {self.customer.username} - {self.meal_time}"

    class Meta:
        verbose_name = "طلب"
        verbose_name_plural = "الطلبات"
        ordering = ['-order_date']  # الأحدث أولاً

# ==================== نموذج سجل تغييرات الطلب (اختياري) ====================
class OrderLog(models.Model):
    """
    نموذج لتسجيل تغييرات حالة الطلب
    """
    order = models.ForeignKey(
        Order, 
        on_delete=models.CASCADE, 
        related_name='logs',
        verbose_name="الطلب"
    )
    old_status = models.CharField(
        max_length=20, 
        verbose_name="الحالة السابقة"
    )
    new_status = models.CharField(
        max_length=20, 
        verbose_name="الحالة الجديدة"
    )
    changed_by = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        verbose_name="تم التغيير بواسطة"
    )
    changed_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="تاريخ التغيير"
    )
    notes = models.TextField(
        blank=True, 
        null=True, 
        verbose_name="ملاحظات"
    )

    def __str__(self):
        return f"طلب #{self.order.id} - {self.old_status} → {self.new_status}"

    class Meta:
        verbose_name = "سجل التغيير"
        verbose_name_plural = "سجل التغييرات"
        ordering = ['-changed_at']