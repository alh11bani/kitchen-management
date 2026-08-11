# 🍽️ نظام إدارة المطبخ (Kitchen Management System)

نظام متكامل مبني باستخدام إطار عمل **Django** لإدارة طلبات المطبخ بشكل إلكتروني سلس. يتيح النظام للزبائن استعراض قائمة الطعام وتقديم الطلبات، بينما يوفر للمشرفين (طاقم المطبخ) لوحة تحكم متقدمة لإدارة الطلبات وتحديث حالتها في الوقت الفعلي.

---

## ✨ المميزات (Features)

### 👥 للزبائن:
* **التسجيل والمصادقة**: نظام حسابات كامل (تسجيل، تسجيل دخول، إدارة الملف الشخصي مع رفع صورة شخصية).
* **قائمة الطعام**: استعراض أنواع الأرز (Rice) والإدامات (Protein) المتوفرة وأسعارها.
* **تقديم الطلبات**: واجهة سهلة لاختيار الوجبات، تحديد عدد الأشخاص، وموعد الوجبة (غداء/عشاء)، مع حساب السعر الإجمالي تلقائياً.
* **إدارة الطلبات**: يمكن للزبون متابعة حالة طلباته السابقة، وإلغاء الطلبات الجديدة قبل بدء تحضيرها.

### 👨‍🍳 لطاقم المطبخ (الإدارة):
* **لوحة تحكم (Dashboard)**: عرض إحصائيات سريعة للطلبات (الجديدة، قيد التجهيز، الجاهزة، المكتملة).
* **تحديث الحالة الفوري**: إمكانية تغيير حالة الطلب بضغطة زر باستخدام تقنية Ajax (بدون إعادة تحميل الصفحة).
* **سجل الطلبات**: صفحة شاملة لعرض جميع الطلبات مع فلاتر للبحث حسب الحالة أو موعد الوجبة.
* **سجل التغييرات (Logs)**: تتبع كامل لمن قام بتغيير حالة الطلب ومتى تم ذلك.

---

## 🛠️ التقنيات المستخدمة (Tech Stack)

* **Backend**: Python 3.11, Django 6.0
* **Frontend**: HTML5, CSS3, Bootstrap 5, Vanilla JavaScript
* **Database**: SQLite (مُعد مسبقاً لدعم PostgreSQL في بيئة الإنتاج)
* **Deployment**: جاهز للرفع على منصة Render (يحتوي على إعدادات WhiteNoise, Gunicorn, و dj-database-url)

---

## 🚀 كيفية تشغيل المشروع محلياً (Local Setup)

1. **استنساخ المستودع (Clone the repository)**
   ```bash
   git clone https://github.com/your-username/kitchen-management.git
   cd kitchen-management
   ```

2. **إنشاء وتفعيل البيئة الوهمية (Virtual Environment)**
   ```bash
   python -m venv venv
   # في الويندوز:
   venv\Scripts\activate
   # في الماك/لينكس:
   source venv/bin/activate
   ```

3. **تثبيت الحزم المطلوبة (Install dependencies)**
   ```bash
   pip install -r requirements.txt
   ```

4. **تطبيق ترحيلات قاعدة البيانات (Run Migrations)**
   ```bash
   python manage.py migrate
   ```

5. **إنشاء حساب مدير (Create Superuser)**
   ```bash
   python manage.py createsuperuser
   ```

6. **تشغيل السيرفر (Run Development Server)**
   ```bash
   python manage.py runserver
   ```
   *المشروع سيعمل الآن على الرابط: `http://127.0.0.1:8000/`*

---

## ☁️ الرفع على الإنتاج (Deployment - Render)

المشروع جاهز تماماً للرفع المجاني على منصة [Render](https://render.com/).
1. اربط حسابك بـ GitHub واختر المستودع.
2. استخدم الإعدادات التالية:
   * **Build Command**: `bash build.sh`
   * **Start Command**: `gunicorn kitchen_project.wsgi:application`
3. أضف الـ Environment Variables المطلوبة:
   * `SECRET_KEY`: (ضع مفتاح سري قوي)
   * `PYTHON_VERSION`: `3.11.0`
   * `DATABASE_URL`: (اختياري - إذا أردت استخدام قاعدة بيانات PostgreSQL لضمان عدم مسح البيانات عند إعادة التشغيل).

---

## 📸 لقطات الشاشة (Screenshots)
*(يمكنك إضافة صور للمشروع هنا بعد رفعه على GitHub من خلال سحب وإفلات الصور)*

---

## 📄 الترخيص (License)
هذا المشروع مفتوح المصدر لأغراض تعليمية.
