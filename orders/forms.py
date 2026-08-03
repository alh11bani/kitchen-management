from django import forms
from .models import Order, RiceType, Protein

class OrderForm(forms.ModelForm):
    """نموذج تقديم طلب جديد"""
    
    class Meta:
        model = Order
        fields = ['rice_type', 'protein', 'number_of_people', 'meal_time', 'phone', 'notes']
        widgets = {
            'rice_type': forms.Select(attrs={'class': 'form-control'}),
            'protein': forms.Select(attrs={'class': 'form-control'}),
            'number_of_people': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'meal_time': forms.Select(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '05xxxxxxxx'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'أي ملاحظات إضافية...'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # عرض فقط الخيارات المتوفرة
        self.fields['rice_type'].queryset = RiceType.objects.filter(is_available=True)
        self.fields['protein'].queryset = Protein.objects.filter(is_available=True)
        self.fields['rice_type'].empty_label = 'اختر نوع الأرز'
        self.fields['protein'].empty_label = 'اختر الإدام'
        
        # إضافة label مخصص
        self.fields['rice_type'].label = 'نوع الأرز'
        self.fields['protein'].label = 'الإدام'
        self.fields['number_of_people'].label = 'عدد النفار'
        self.fields['meal_time'].label = 'الميعاد'
        self.fields['phone'].label = 'رقم الجوال'
        self.fields['notes'].label = 'ملاحظات إضافية'