# Mercy Works — Django Web Application

A full-featured charity/NGO web application for **Mercy Works Organization**, built with Python Django, Bootstrap 5, and a Swagger REST API. Ready for deployment on **Railway**.

---

## 🚀 Quick Start (Local)

```bash
cd mercy_works
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Visit: **http://127.0.0.1:8000/**

---

## 👤 Demo Accounts

| Role   | Username  | Password      |
|--------|-----------|---------------|


| Admin  | `admin`   | `Admin1234!`  |
| Editor | `editor1` | `Editor1234!` |
| Donor  | `donor1`  | `Donor1234!`  |

---

## 📁 Project Structure

```
mercy_works/
├── core/               # Settings, main URLs
├── accounts/           # Auth, roles, dashboards
├── causes/             # Charity causes management
├── events/             # Events management
├── blog/               # Blog/news posts
├── donations/          # Donation forms, contact messages
├── volunteers/         # Volunteer opportunities & applications
├── templates/          # Bootstrap 5 HTML templates
├── static/             # CSS and static assets
├── requirements.txt
├── Procfile
├── railway.json
└── runtime.txt
```

---

## ✨ Features

### Roles
- **Admin** — full access: manage all content, users, donations, messages
- **Editor** — manage causes, events, blog posts
- **Donor/Volunteer** — personal dashboard, donation history, applications

### Causes
- Create causes with fundraising goals and progress tracking
- Donate directly to specific causes
- Progress bar showing % raised

### Events
- Create and manage upcoming events
- Public events listing page

### Blog
- Write and publish blog posts with categories
- Public blog with recent posts on homepage

### Donations
- Donate to any cause or make general donations
- Anonymous donation option
- Admin can view all donations

### Volunteers
- Post volunteer opportunities
- Users can apply directly
- Admin approves/rejects applications

### Contact
- Public contact form
- Admin marks messages as read

### REST API + Swagger
- Full REST API for all resources
- Swagger UI at `/swagger/`
- ReDoc at `/redoc/`

---

## 🌐 Deploy to Railway

1. Push to GitHub
2. Go to [railway.app](https://railway.app) → New Project → Deploy from GitHub
3. Add PostgreSQL database service
4. Add environment variables:
   ```
   SECRET_KEY=your-strong-secret-key
   DEBUG=False
   DATABASE_URL=<auto-linked from Postgres>
   CLOUDINARY_CLOUD_NAME=your_cloud_name
   CLOUDINARY_API_KEY=your_api_key
   CLOUDINARY_API_SECRET=your_api_secret
   ```
5. Set Pre-deploy Command:
   ```
   python manage.py migrate && python manage.py collectstatic --noinput
   ```

---

## 🔗 Key URLs

| URL | Description |
|-----|-------------|
| `/` | Homepage |
| `/about/` | About page |
| `/causes/` | All causes |
| `/events/` | Events listing |
| `/blog/` | Blog |
| `/volunteers/` | Volunteer opportunities |
| `/donations/donate/` | Donate |
| `/donations/contact/` | Contact form |
| `/accounts/login/` | Login |
| `/accounts/dashboard/` | Role dashboard |
| `/admin/` | Django admin |
| `/swagger/` | API documentation |

---

## 🛠 Tech Stack

| Component | Technology |
|-----------|-----------|
| Backend | Python Django 4.2 |
| Database | SQLite (local) / PostgreSQL (Railway) |
| Frontend | Django Templates + Bootstrap 5 |
| REST API | Django REST Framework + drf-yasg |
| Images | Cloudinary |
| Static Files | WhiteNoise |
| Deployment | Railway + Gunicorn |
