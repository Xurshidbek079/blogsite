# Xurshidbro.uz - Shaxsiy Blog

O'zbek tilidagi shaxsiy blog loyihasi.

## Texnologiyalar

- Python 3.8+
- Django 5.0.2
- Gunicorn
- Nginx
- SQLite3

## O'rnatish

1. Loyihani klonlash:
```bash
git clone https://github.com/yourusername/xurshidbrouz.git
cd xurshidbrouz
```

2. Virtual muhit yaratish va faollashtirish:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# yoki
.\venv\Scripts\activate  # Windows
```

3. Kerakli paketlarni o'rnatish:
```bash
pip install -r requirements.txt
```

4. Muhit o'zgaruvchilarini sozlash:
```bash
cp .env.example .env
# .env faylini tahrirlang
```

5. Ma'lumotlar bazasini yaratish:
```bash
python manage.py migrate
```

6. Admin foydalanuvchini yaratish:
```bash
python manage.py createsuperuser
```

## Ishga tushirish

### Rivojlanish muhitida

```bash
python manage.py runserver
```

### Ishlab chiqarish muhitida

1. Gunicorn konfiguratsiyasini sozlash
2. Nginx konfiguratsiyasini sozlash
3. SSL sertifikatlarini o'rnatish
4. Static fayllarni yig'ish:
```bash
python manage.py collectstatic
```

## Domenlar

- Asosiy sayt: https://xurshidbro.uz
- Admin panel: https://admin.xurshidbro.uz

## Xavfsizlik

- Admin panel faqat maxsus subdomen orqali kirish mumkin
- SSL sertifikatlari orqali himoyalangan
- robots.txt admin panelni qidiruvdan yashiradi

## Litsenziya

MIT 