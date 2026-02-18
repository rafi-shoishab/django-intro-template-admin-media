# Django Intro Template 🚀

A beginner-friendly Django project to understand the fundamentals of Django web development, including:

* Django project setup
* HTTP response handling
* URL routing
* Template rendering (HTML)
* Basic Django structure

This project is created for learning how Django handles requests and returns responses.

---

# 📌 Project Overview

This project demonstrates how:

* Django processes HTTP requests
* Views return responses
* Templates render HTML pages
* URL routing connects views and templates

---

# 🏗 Project Structure

```
django-intro-template/
│
├── core/                   # Django project configuration (settings, urls, wsgi)
│
├── navigation/             # Django app
│   ├── views.py            # Application views
│   ├── urls.py             # App URL routes
│   ├── models.py
│   └── admin.py
│
├── templates/              # HTML templates
│   └── index.html
│
├── static/                 # Static files (CSS)
│   └── style.css
│
├── manage.py               # Django management script
└── requirements.txt        # Project dependencies
```

---

# ⚡ 1. Setup Django (Run Project)

Follow these steps to run the project locally.

## 🔹 Clone Repository

```
git clone https://github.com/rafi-shoishab/django-intro-template.git
cd django-intro-template
```

---

## 🔹 Create Virtual Environment

### Mac / Linux

```
python3 -m venv .venv
source .venv/bin/activate
```

### Windows

```
python -m venv .venv
.venv\Scripts\activate
```

---

## 🔹 Install Dependencies

```
pip install -r requirements.txt
```

---

## 🔹 Run Development Server

```
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000
```

You should see the homepage.

---

# 🌐 2. HTTP Response in Django

Django handles web requests using **views**.

A view receives a request and returns a response.

## Example: Returning a Simple HTTP Response

File: `navigation/views.py`

```
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello Django")
```

This sends a plain text response to the browser.

---

# 🎨 3. Template Rendering (HTML)

Django uses templates to render dynamic HTML pages.

Templates separate frontend (HTML) from backend logic.

---

## Template Location

```
templates/index.html
```

---

## Rendering Template from View

File: `navigation/views.py`

```
from django.shortcuts import render

def home(request):
    return render(request, "index.html")
```

This renders the HTML file and returns it to the browser.

---

## URL Routing

URL routing connects a URL with a view.

File: `navigation/urls.py`

```
from django.urls import path
from . im
```
