# Harry Joseph - Django Lab 7

## Project Metadata
- Author: Harry Joseph
- Student ID: 12345
- Created: 2025-11-09
- Platform: Django 5.2.8
- Database: SQLite
- Python Version: 3.11+

## Overview
Lab 7 demonstrates Django web development fundamentals. The project showcases basic Django concepts including URL routing, view functions, and HTTP responses with simple HTML generation for educational purposes.

## 📥 Quick Download

**Get the complete project instantly:**

[![Download CPAN214-LAB7.ZIP](https://img.shields.io/badge/Download-CPAN214--LAB7.ZIP-blue?style=for-the-badge&logo=download)](https://github.com/hjoseph777/releases/download/v1/CPAN214-LAB7.ZIP)

*Complete Django project ready to run*

## 🌐 Live Demo

**View the application online:**

[![Live Demo](https://img.shields.io/badge/Live-Demo-green?style=for-the-badge&logo=web)](https://your-demo-url.com)

## Important: Where your Django code lives
- The main views are in [`main/views.py`](harry_joseph/main/views.py) with home, greetings, and time display functions
- URL configuration is in [`harry_joseph/urls.py`](harry_joseph/harry_joseph/urls.py) with route mappings
- Django settings are in [`harry_joseph/settings.py`](harry_joseph/harry_joseph/settings.py)

## Project Explorer
An interactive, collapsible view of the codebase. Click file names to explore the Django structure.

<details open>
   <summary><strong>harry_joseph/ – Django Project Root</strong></summary>

   - 📁 <strong>harry_joseph</strong>
      - 📄 [`manage.py`](harry_joseph/manage.py) – Django management script
      - 📄 [`db.sqlite3`](harry_joseph/db.sqlite3) – SQLite database file
      -  <strong>harry_joseph</strong>
         - ⚙️ [`settings.py`](harry_joseph/harry_joseph/settings.py) – **Django configuration**
         - 🧭 [`urls.py`](harry_joseph/harry_joseph/urls.py) – **Main URL routing**
         - 🌐 [`wsgi.py`](harry_joseph/harry_joseph/wsgi.py) – WSGI configuration
         - 🔄 [`asgi.py`](harry_joseph/harry_joseph/asgi.py) – ASGI configuration
      - 📁 <strong>main</strong>
         - 🏠 [`views.py`](harry_joseph/main/views.py) – **Main view functions**
         - 🗂️ [`models.py`](harry_joseph/main/models.py) – Database models
         - ⚡ [`admin.py`](harry_joseph/main/admin.py) – Admin interface config
         - 🧪 [`tests.py`](harry_joseph/main/tests.py) – Unit tests
         - 📁 <strong>migrations</strong>
</details>

<details>
   <summary><strong>Repository Root – Scripts & Configuration</strong></summary>

   - 📁 <strong>CPAN214-Lab7</strong>
      - 📄 [`README.md`](README.md) – **Documentation (this file)**
      - 🚀 [`start_server.sh`](start_server.sh) – **Server startup script**
      - 📦 [`requirements.txt`](requirements.txt) – Python dependencies
      - 🔒 [`.gitignore`](.gitignore) – Git ignore rules
      - 📁 <strong>.github</strong>
         - GitHub Actions workflows
      - 📁 <strong>.qodo</strong>
         - Qodo configuration
</details>
