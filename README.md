# 🎬 Movie REST API

A Django REST Framework project that provides APIs to manage movie data categorized by genre (e.g., Action, Comedy, Romantic). It also supports uploading and serving movie images.

---

## 📁 Project Structure

Movie_REST_API/
│
├── media/Images/ # Stores uploaded movie images
├── movies/ # Django app with models, views, serializers
│ ├── migrations/
│ ├── admin.py
│ ├── apps.py
│ ├── models.py # Movie model
│ ├── serializers.py # Serializers for movie model
│ ├── views.py # ViewSets for each genre
│ └── tests.py
│
├── mysite/ # Main Django project settings
│ ├── settings.py # Project settings including media setup
│ ├── urls.py # URL routing using SimpleRouter
│ └── wsgi.py / asgi.py
│
├── db.sqlite3 # SQLite DB
├── manage.py # Django management script
└── README.md # Project documentation


---

## 🌟 Features

- 📂 Movie CRUD (Create, Read, Update, Delete) operations
- 🎭 Categorized views: Action, Comedy, Romantic
- 📸 Upload & serve movie images
- ⚙️ RESTful endpoints using Django REST Framework

---

## 🔧 Installation & Setup

### 1. Clone the repository
- git clone https://github.com/AnjaliYadav-04/Movie_REST_API.git
- cd Movie_REST_API
  
### 2. Create a virtual environment
- python -m venv venv
- source venv/bin/activate      # For Windows: venv\Scripts\activate
  
### 3. Install dependencies
- pip install django djangorestframework
- Or use requirements.txt if available:
- pip install -r requirements.txt
- 
### 4. Run migrations
- python manage.py migrate

### 5. Start the development server
- python manage.py runserver

---

## 🚀 API Endpoints
**Endpoint	Description**
/movies/	All movies
/action/	Action movies
/comedy/	Comedy movies
/romantic/	Romantic movies
/media/Images/...	Access uploaded images

---

## ⚙️ Serving Media Files
**Ensure the following lines are in your urls.py:**
- from django.conf import settings
- from django.conf.urls.static import static
- urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  
---

## 🧑‍💻 Author
**👩‍💻 Anjali Yadav**
