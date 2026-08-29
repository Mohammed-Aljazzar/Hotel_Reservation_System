# Airbnb Reservations

> منصة حجوزات سفر مبنية بـ Django، تتيح استكشاف العقارات وإدارتها، تنفيذ الحجوزات، كتابة التقييمات، وإثراء تجربة المستخدم عبر مدونة ومحتوى تعريفي.

![Python](https://img.shields.io/badge/Python-3.13-3776AB?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.2-092E20?logo=django&logoColor=white)
![Database](https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite&logoColor=white)
![API](https://img.shields.io/badge/API-Django%20REST%20Framework-ff1709)

## الفكرة

**Airbnb Reservations** هو تطبيق ويب لإدارة واستعراض خيارات الإقامة والسفر، مثل الفنادق والمطاعم والأماكن. يستطيع الزوار البحث والتصفية واستعراض التفاصيل، بينما يستطيع المستخدم المسجّل إدارة ملفه الشخصي، نشر عقاراته، إجراء الحجوزات، وإضافة تقييماته. كما يوفر المشروع مدونة قابلة للبحث والتصنيف، ولوحة إدارة Django لإدارة المحتوى بالكامل.

## المزايا

### العقارات والحجوزات

- عرض العقارات مع pagination وخيارات التصفية حسب الاسم والوصف والتصنيف والمكان.
- صفحات تفصيلية للعقار تشمل الصور والسعر والوصف والحالة ومتوسط التقييمات وعقارات مشابهة.
- إنشاء العقارات وتعديلها وحذفها، مع ضمان أن المالك فقط يستطيع إدارة عقاره.
- الحجز من صفحة العقار باختيار تاريخ الوصول والمغادرة وعدد الضيوف والأطفال.
- صفحة حجوزاتي وصفحة عقاراتي للمستخدم.
- تقييمات وملاحظات المستخدمين للعقارات، مع إمكانية تعديل التقييم الموجود.

### الحسابات والمحتوى

- إنشاء حساب وتسجيل الدخول وتسجيل الخروج.
- تعديل بيانات المستخدم والصورة الشخصية ورقم الهاتف والعنوان.
- مسارات Django الجاهزة لتغيير كلمة المرور واستعادتها.
- مدونة تشمل البحث، التصنيفات، الوسوم، المقالات الحديثة، وصفحات التفاصيل.
- صفحة «من نحن» وأسئلة شائعة قابلة للإدارة.
- إعدادات موقع ديناميكية في التذييل: الشعار، وسائل التواصل، بيانات الاتصال والوصف.

### الإدارة وواجهة البرمجة

- لوحة Django Admin لإدارة المستخدمين والعقارات والحجوزات والتقييمات والمدونة والإعدادات.
- محرر **Django Summernote** للمحتوى الغني من لوحة الإدارة.
- REST API محمية بالمصادقة عبر Token، مع Swagger وReDoc لتوثيق الـAPI.

## التقنيات المستخدمة

| الجانب | التقنيات |
| --- | --- |
| Backend | Python 3.13، Django 5.2 |
| قاعدة البيانات | SQLite افتراضياً |
| API | Django REST Framework، Token Authentication، drf-spectacular |
| المصادقة | Django Authentication، django-allauth، dj-rest-auth |
| البحث والتصفية | django-filter، Django ORM و`Q` queries |
| المحتوى | django-taggit، django-summernote |
| الواجهة | Django Templates، Bootstrap 4، jQuery |
| تجربة الواجهة | Owl Carousel، AOS، Magnific Popup، Bootstrap Datepicker، Ionicons وOpen Iconic |
| الصور والملفات | Pillow وDjango Media Files |
| النشر | Gunicorn، Procfile؛ تتوفر WhiteNoise ضمن الاعتمادات للملفات الثابتة |

## بنية المشروع

```text
.
├── accounts/       # الحسابات والملف الشخصي
├── property/       # العقارات والصور والحجوزات والتقييمات وAPI الخاصة بها
├── blog/           # المقالات والتصنيفات والوسوم وAPI الخاصة بها
├── about/          # صفحة من نحن والأسئلة الشائعة
├── settings/       # الصفحة الرئيسية والبحث وإعدادات الموقع والتذييل
├── project/        # إعدادات Django والمسارات الرئيسية وWSGI/ASGI
├── templates/      # القالب الأساسي المشترك
├── static/         # ملفات CSS وJavaScript والصور الثابتة
├── media/          # الملفات التي يرفعها المستخدمون والمحتوى
├── requirements.txt
├── Procfile
└── manage.py
```

## التشغيل محلياً

### المتطلبات

- Python 3.13 (أو إصدار متوافق مع Django 5.2)
- `pip`
- Git

### الخطوات

```bash
git clone https://github.com/Mohammed-Aljazzar/Airbnb-Reservations.git
cd Airbnb-Reservations

# Linux / macOS
python3 -m venv .venv
source .venv/bin/activate

# Windows (PowerShell)
# .venv\Scripts\Activate.ps1

pip install --upgrade pip
pip install -r requirements.txt

# الحزم المطلوبة في إعدادات المشروع إن لم تكن متوفرة في بيئتك
pip install django-allauth dj-rest-auth drf-spectacular

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

بعد التشغيل، افتح [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

### أوامر مفيدة

```bash
# التحقق من إعدادات Django
python manage.py check

# تشغيل الاختبارات
python manage.py test

# تجهيز الملفات الثابتة للنشر
python manage.py collectstatic --noinput
```

## المسارات المهمة

| المسار | الوصف |
| --- | --- |
| `/` | الصفحة الرئيسية، الفئات، الأماكن والمحتوى المميز |
| `/property/` | قائمة العقارات مع التصفية |
| `/property/create/` | إضافة عقار (يتطلب تسجيل الدخول) |
| `/accounts/signup` | إنشاء حساب |
| `/accounts/profile/` | الملف الشخصي |
| `/blog/` | المدونة والبحث في المقالات |
| `/about/` | من نحن والأسئلة الشائعة |
| `/admin/` | لوحة الإدارة |

## REST API والتوثيق

تستخدم واجهات الـAPI مصادقة Token؛ أرسل الترويسة التالية إلى المسارات المحمية:

```http
Authorization: Token <your-token>
```

| المسار | الوظيفة |
| --- | --- |
| `/property/api/list/` | عرض/إنشاء العقارات |
| `/property/api/list/<id>` | عرض/تعديل/حذف عقار |
| `/blog/api/list/` | عرض المقالات |
| `/blog/api/list/<id>/` | عرض مقال |
| `/blog/api/list/filter/<query>/` | البحث في المقالات |
| `/api/schema/` | مخطط OpenAPI |
| `/api/docs/` | Swagger UI |
| `/api/redoc/` | ReDoc |
| `/rest-auth/` | مسارات المصادقة عبر REST |
| `/rest-auth/registration/` | تسجيل حساب عبر REST |

## الإعداد للنشر والإنتاج

قبل النشر، لا تستخدم قيم التطوير الموجودة في `project/settings.py`. على الأقل:

1. انقل `SECRET_KEY` إلى متغير بيئة جديد وآمن.
2. اجعل `DEBUG = False`.
3. حدّد `ALLOWED_HOSTS` لنطاقات مشروعك.
4. استبدل SQLite بقاعدة بيانات إنتاج مناسبة مثل PostgreSQL.
5. اضبط تخزين `STATIC_ROOT` و`MEDIA_ROOT`، وفعل WhiteNoise أو CDN للملفات الثابتة.
6. لا ترفع كلمات مرور أو مفاتيح API أو بيانات إنتاج إلى GitHub.

يتوفر `Procfile` لتشغيل التطبيق عبر Gunicorn:

```bash
gunicorn project.wsgi --log-file -
```

## المساهمة

المساهمات مرحّب بها:

1. اعمل Fork للمستودع.
2. أنشئ فرعاً جديداً: `git checkout -b feature/feature-name`.
3. نفّذ التعديلات واختبرها.
4. أرسل Pull Request يوضح التغيير.

## ملاحظات المستودع

- لا يحتوي المستودع حالياً على ملف `LICENSE`؛ أضف ترخيصاً (مثل MIT) قبل إعادة استخدام المشروع أو توزيعه بشروط واضحة.
- يفضّل إضافة `.gitignore` قبل النشر العام لاستبعاد `.venv/` و`__pycache__/` و`db.sqlite3` والملفات المرفوعة في `media/` وملفات النظام مثل `.DS_Store`.

## المطوّر

**Mohammed Aljazzar**<br>
للتواصل: [m.i.aljazzar19@gmail.com](mailto:m.i.aljazzar19@gmail.com)
