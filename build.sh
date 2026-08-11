#!/usr/bin/env bash
set -o errexit

# تثبيت المتطلبات
pip install -r requirements.txt

# تجميع الملفات الثابتة
python manage.py collectstatic --no-input

# تنفيذ الترحيلات
python manage.py migrate

# ==============================================
# 👤 إنشاء المدير (Superuser)
# ==============================================

echo "👤 جاري إنشاء المدير..."

python manage.py shell -c "
from django.contrib.auth.models import User;

# بيانات المدير (مكشوفة هنا)
username = 'admin'
email = 'admin@example.com'
password = 'Admin@123456'  # ← كلمة مرور بسيطة ومكشوفة

# حذف المدير القديم إن وجد
User.objects.filter(username=username).delete();

# إنشاء مدير جديد
User.objects.create_superuser(username, email, password);

print('✅ تم إنشاء المدير بنجاح!')
print(f'👤 اسم المستخدم: {username}')
print(f'🔑 كلمة المرور: {password}')
"

echo "✅ اكتمل إعداد المدير!"