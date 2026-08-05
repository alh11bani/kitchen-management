# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    """
    نموذج الملف الشخصي للمستخدم
    يضيف معلومات إضافية لمستخدم Django
    """
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        related_name='profile',
        verbose_name="المستخدم"
    )
    phone = models.CharField(
        max_length=15, 
        verbose_name="رقم الجوال",
        help_text="رقم الجوال للتواصل"
    )
    address = models.TextField(
        blank=True, 
        null=True, 
        verbose_name="العنوان"
    )
    profile_picture = models.ImageField(
        upload_to='profiles/', 
        blank=True, 
        null=True, 
        verbose_name="الصورة الشخصية"
    )
    
    
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="تاريخ الإنشاء"
    )
    updated_at = models.DateTimeField(
        auto_now=True, 
        verbose_name="آخر تحديث"
    )

    def __str__(self):
        return f"{self.user.username} - {self.phone}"

    class Meta:
        verbose_name = "الملف الشخصي"
        verbose_name_plural = "الملفات الشخصية"

# إشارة لإنشاء الملف الشخصي تلقائياً عند إنشاء مستخدم جديد
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()