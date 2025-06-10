# Xurshid's Blog

A personal blog built with Django, featuring essays, projects, books, and more.

## Features

- Clean, minimalist design
- Responsive layout
- Secure admin interface with subdomain protection
- Static file optimization with WhiteNoise
- SSL/HTTPS enabled
- Automated backups
- Performance optimized for production

## Tech Stack

- **Backend**: Django 4.2
- **Server**: Gunicorn
- **Web Server**: Nginx
- **Static Files**: WhiteNoise
- **Database**: SQLite3
- **Environment**: Python 3.8+

## Project Structure

```
blogsite/
├── blog/                 # Main blog application
├── static/              # Static files (CSS, images, etc.)
├── templates/           # HTML templates
├── media/              # User-uploaded files
├── staticfiles/        # Collected static files
├── logs/               # Application logs
└── xurshidbrouz/       # Project configuration
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Xurshidbek079/blogsite.git
cd blogsite
```

2. Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
# Create .env file with:
DJANGO_SECRET_KEY=your_secret_key
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Create superuser:
```bash
python manage.py createsuperuser
```

7. Collect static files:
```bash
python manage.py collectstatic
```

## Development

Run the development server:
```bash
python manage.py runserver
```

## Production Deployment

1. Configure Nginx:
   - Main domain: xurshidbro.uz
   - Admin subdomain: admin.xurshidbro.uz
   - SSL certificates from Let's Encrypt

2. Set up Gunicorn:
   - Configured for optimal performance
   - Automatic worker management
   - Logging enabled

3. Security Features:
   - HTTPS enforced
   - Admin interface restricted to subdomain
   - Secure headers configured
   - CSRF protection
   - XSS protection

4. Backup System:
   - Automated database backups
   - Media files backup
   - 7-day retention policy

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

- Website: [xurshidbro.uz](https://xurshidbro.uz)
- Telegram: [@xurshidbro_blog](https://t.me/xurshidbro_blog) 