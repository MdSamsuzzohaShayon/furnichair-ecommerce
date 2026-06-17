# 🪑 FurniChair — Modern Furniture E-commerce Platform

🌐 **Live Demo:** [https://furnichair.webdevlab.org](https://furnichair.webdevlab.org)

FurniChair is a full-stack, scalable furniture e-commerce platform built with modern technologies. It focuses on performance, clean UI/UX, and real-world production features like authentication, payments, and admin management.

---

## 🚀 Features

### 🛍️ Customer Experience

* Browse products with category & search support
* Advanced filtering system
* Add to cart & view total cart items in real-time
* Smooth page transitions & animations
* Optimized image rendering on product pages
* SEO optimized pages for better discoverability

### 🔐 Authentication & Security

* JWT-based authentication with refresh tokens
* Login using **email or username**
* Forgot password functionality
* Secure token storage (cookies)
* Custom password validation (Django)

### 🧑‍💼 Admin & Dashboard

* Unified admin panel for **admin + staff**
* Product & category management
* Status control (publish/unpublish)
* Automatic image cleanup on delete ✅
* Customer dashboard (basic)

### ⚙️ Performance & UX

* Lazy loading & preload pages
* API loading indicators
* “Load More” pagination
* Frontend data loaders
* Optimized API handling

---

## 🧱 Tech Stack

| Layer    | Technology                             |
| -------- | -------------------------------------- |
| Backend  | Django + Django REST Framework         |
| Frontend | Nuxt.js (Vue 3)                        |
| Database | SQLite (dev), PostgreSQL (recommended) |
| Storage  | Cloudinary                             |
| Auth     | JWT                                    |
| Payments | SSLCommerz, bKash                      |
| DevOps   | Docker, Nginx                          |

---

## 📦 Project Structure

```
furnichair-ecommerce/
│
├── backend/      # Django REST API
├── frontend/     # Nuxt.js frontend
├── docker/       # Docker configurations
└── README.md
```

---

## ⚡ Getting Started

### 1️⃣ Clone the Repository

```
git clone https://github.com/MdSamsuzzohaShayon/furnichair-ecommerce.git
cd furnichair-ecommerce
```

---

## 🔧 Backend Setup (Django)

### 📌 Environment Variables

Create `.env` file:

```
cp .env.example .env
```

Update all required values.

---

### 🐳 Run with Docker

```
docker compose -f docker-compose.yml -f docker-compose.dev.yml up -d
```

---

### 💻 Run without Docker

```
cd backend

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

📄 API Docs: [http://localhost:8000/api/docs/](http://localhost:8000/api/docs/)

---

## 🎨 Frontend Setup (Nuxt.js)

```
cd frontend

cp .env.example .env
npm install
npm run dev
```

🌐 App: [http://localhost:3000/](http://localhost:3000/)

---

## 💳 Payment Integration

### SSLCommerz

* Sandbox & Production support
* Docs: [https://developer.sslcommerz.com/doc/v4/](https://developer.sslcommerz.com/doc/v4/)
* Python SDK: [https://github.com/sslcommerz/SSLCommerz-Python](https://github.com/sslcommerz/SSLCommerz-Python)

### bKash

* Tokenized checkout support
* Requires merchant account
* Docs: [https://developer.bka.sh/docs](https://developer.bka.sh/docs)

---

## 🐳 Docker Tips

* Copy files from container:

```
docker cp <container>:<path> <destination>
```

* Restart services:

```
docker compose restart nginx
```

* Access container:

```
docker exec -it <container_name> sh
```

---

## 🚀 Deployment Guide

1. Setup Docker environment (dev & prod)
2. Configure environment variables
3. Build & run containers:

```
docker compose up -d --build
```

4. Run migrations:

```
docker compose run backend python manage.py migrate
```

5. Create superuser:

```
docker compose run backend python manage.py createsuperuser
```

6. Setup PostgreSQL
7. Configure CI/CD (GitHub Actions recommended)

---

## 🧪 Testing & Code Quality

```
pip install pytest pytest-django coverage
pytest
pytest --cov
coverage html
```

### Code Standards

* Format: `black`
* Linting: `flake8`

---

## 📚 Learning Resources

* [Django REST Framework Docs](https://www.django-rest-framework.org/)
* [Cloudinary Django Integration](https://cloudinary.com/documentation/django_integration)
* [JWT Customization](https://django-rest-framework-simplejwt.readthedocs.io/)

---

## 🎯 Roadmap / TODO

* Improve refresh token rotation
* Full customer dashboard
* Supabase migration option
* Better analytics & reporting
* Enhanced SEO automation
* Centralized config table (logo, banners, etc.)

---

## 💡 Inspirations

* [https://99grid.com/](https://99grid.com/)
* [https://demo.minimog.co/](https://demo.minimog.co/)
* [https://github.com/thomas545/ecommerce_api](https://github.com/thomas545/ecommerce_api)
* [https://github.com/swellstores/origin-theme](https://github.com/swellstores/origin-theme)

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

---

## 👨‍💻 Author

**Md Samsuzzoha Shayon**
Founder of *Its Sports Time*
Full Stack Developer (Django, React, Nuxt, AWS)

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub — it helps a lot!

---