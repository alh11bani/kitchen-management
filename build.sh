#!/usr/bin/env bash
# build.sh - سكريبت البناء لـ Render

set -o errexit

# تثبيت المتطلبات
pip install -r requirements.txt

# تجميع الملفات الثابتة
python manage.py collectstatic --no-input

# تنفيذ ترحيلات قاعدة البيانات
python manage.py migrate

# ✅ إنشاء المدير تلقائياً (سطر واحد فقط!)
python manage.py createsuperuser --noinput --username $DJANGO_SUPERUSER_USERNAME --email $DJANGO_SUPERUSER_EMAIL

# ملاحظة: كلمة المرور تؤخذ من متغير DJANGO_SUPERUSER_PASSWORD