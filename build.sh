#!/usr/bin/env bash
set -o errexit

# تثبيت المتطلبات
pip install -r requirements.txt

# تجميع الملفات الثابتة
python manage.py collectstatic --no-input

# تنفيذ الترحيلات
python manage.py migrate

echo "✅ Build completed successfully!"