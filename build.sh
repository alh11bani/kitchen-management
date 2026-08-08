#!/usr/bin/env bash
# build.sh - سكريبت البناء لـ Render

set -o errexit

# تثبيت المتطلبات
pip install -r requirements.txt

# تجميع الملفات الثابتة
python manage.py collectstatic --no-input

# تنفيذ ترحيلات قاعدة البيانات
python manage.py migrate