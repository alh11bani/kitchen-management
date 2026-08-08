#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate

# ✅ حذف المدير القديم وإنشاء جديد
python manage.py shell -c "
from django.contrib.auth.models import User;
User.objects.filter(username='$DJANGO_SUPERUSER_USERNAME').delete();
User.objects.create_superuser('$DJANGO_SUPERUSER_USERNAME', '$DJANGO_SUPERUSER_EMAIL', '$DJANGO_SUPERUSER_PASSWORD')
"
echo "✅ تم إعادة إنشاء المدير!"