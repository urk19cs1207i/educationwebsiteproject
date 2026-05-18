# educationwebsiteproject
# Educational Website

A full-stack **Educational Website** built with **Python**, **Django**, **HTML/CSS**, and **SQLite3**. Designed to manage and deliver online courses, lessons, and student information through a clean, responsive interface.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Pages & URLs](#pages--urls)
- [Admin Panel](#admin-panel)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

This Educational Website allows admins to manage courses, lessons, and student enrollments. Students can browse available courses, register, and access learning materials — all through a user-friendly Django-powered web interface.

---

## Features

- Home page with featured courses
- Course listing and detail pages
- Lesson management per course
- Student registration and login
- User authentication (Login / Logout / Register)
- Student dashboard to track enrolled courses
- Admin panel to manage courses, lessons, and students
- SQLite3 database — no setup required
- Responsive design with HTML & CSS

---

## Tech Stack

| Layer          | Technology              |
|----------------|-------------------------|
| Backend        | Python 3.x, Django      |
| Frontend       | HTML5, CSS3             |
| Database       | SQLite3                 |
| Authentication | Django Built-in Auth    |
| Admin          | Django Admin Panel      |
| Templating     | Django Template Engine  |

---

## Project Structure

```
educational-website/
├── edu_site/                    # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── courses/                     # Courses app
│   ├── migrations/
│   ├── templates/
│   │   └── courses/
│   │       ├── course_list.html
│   │       ├── course_detail.html
│   │       └── lesson_detail.html
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── students/                    # Students app
│   ├── migrations/
│   ├── templates/
│   │   └── students/
│   │       ├── register.html
│   │       ├── login.html
│   │       └── dashboard.html
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── templates/
│   └── base.html                # Shared base template
├── static/
│   └── css/
│       └── style.css
├── db.sqlite3
├── manage.py
└── requirements.txt
```

---

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/educational-website.git
   cd educational-website
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv

   # On Windows
   venv\Scripts\activate

   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser** (for admin access)
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. Open your browser and visit: `http://127.0.0.1:8000`

---

## Authentication

This project uses **Django's built-in authentication system**.

| Action   | URL               |
|----------|-------------------|
| Register | `/register/`      |
| Login    | `/login/`         |
| Logout   | `/logout/`        |
| Dashboard| `/dashboard/`     |

- Students must register and log in to access course materials
- Unauthenticated users are redirected to the login page
- Admins manage all data through the Django Admin panel

---

## Pages & URLs

| URL                          | Description                    |
|------------------------------|--------------------------------|
| `/`                          | Home page with featured courses|
| `/courses/`                  | All courses listing            |
| `/courses/<id>/`             | Course detail page             |
| `/courses/<id>/lessons/<id>/`| Lesson detail page             |
| `/register/`                 | Student registration           |
| `/login/`                    | Student login                  |
| `/logout/`                   | Logout                         |
| `/dashboard/`                | Student dashboard              |
| `/admin/`                    | Django admin panel             |

---

## Admin Panel

Django's built-in admin panel is used to manage:

- **Courses** — Add, edit, delete courses
- **Lessons** — Add lessons under each course
- **Students** — View and manage registered users
- **Enrollments** — Track which students are enrolled in which courses

Access the admin panel at: `http://127.0.0.1:8000/admin/`
Login with your superuser credentials.

---

## Requirements

Generate your `requirements.txt` by running:

```bash
pip freeze > requirements.txt
```

Typical dependencies for this project:

```
Django>=4.2
```

---

## Screenshots

<img width="941" height="409" alt="image" src="https://github.com/user-attachments/assets/9a7ef196-a1f6-46ab-a38d-667ccaab8fe4" />

<img width="928" height="437" alt="image" src="https://github.com/user-attachments/assets/cffcff89-66d6-466e-9b19-78ec38633d98" />

<img width="899" height="430" alt="image" src="https://github.com/user-attachments/assets/b3291abb-963c-4218-a52f-d1cf19928bf7" />

<img width="622" height="437" alt="image" src="https://github.com/user-attachments/assets/da1b1fab-f8bb-4cce-bfae-21cdfd216a6a" />

<img width="371" height="432" alt="image" src="https://github.com/user-attachments/assets/7dce36e0-eceb-47f6-b093-b5ba4f3b849e" />

<img width="541" height="391" alt="image" src="https://github.com/user-attachments/assets/8316172c-bc41-44f2-bb34-05c0a87878b3" />

<img width="481" height="173" alt="image" src="https://github.com/user-attachments/assets/e029b184-9432-4e16-8e6d-d26f2b6da186" />

<img width="727" height="395" alt="image" src="https://github.com/user-attachments/assets/5577af21-5e97-4e62-988b-064bfafa36d3" />
<img width="950" height="353" alt="image" src="https://github.com/user-attachments/assets/522f968f-6805-474f-afff-af1bc74f897c" />


## Contributing

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Author

- GitHub: [urk19cs1207i](https://github.com/urk19cs1207i)
- LinkedIn: [Jonnalagadda Akshaya](linkedin.com/in/jonnalagadda-akshaya)
