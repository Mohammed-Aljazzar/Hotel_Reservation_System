# Hotel Reservations

> A Django-powered travel booking platform for exploring and managing properties, making reservations, sharing reviews, and discovering travel content through a blog.

![Python](https://img.shields.io/badge/Python-3.13-3776AB?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.2-092E20?logo=django&logoColor=white)
![Database](https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite&logoColor=white)
![API](https://img.shields.io/badge/API-Django%20REST%20Framework-ff1709)

## Overview

**Airbnb Reservations** is a web application for discovering and managing travel properties, including hotels, restaurants, and places. Visitors can search, filter, and view property details, while authenticated users can manage their profiles, publish properties, create reservations, and submit reviews. The project also includes a searchable blog, an About page, FAQs, and a Django admin panel for managing the platform.

## Website at a glance

The platform is organized around the complete visitor journey—from discovering a destination to making a reservation and leaving feedback.

| Website area | What visitors and users can do |
| --- | --- |
| **Home** | Discover locations, property categories, featured hotels, restaurants, places, and recent blog posts. |
| **Search** | Search for properties by name and place directly from the home page. |
| **Properties** | Browse the catalog, apply filters, inspect listing details, availability, ratings, images, and related listings. |
| **Reservations** | Select dates and guest details to reserve a property, then review reservations from the profile area. |
| **Accounts** | Register, log in, recover a password, and maintain profile information. |
| **My Listings** | Let property owners create, update, and remove their own listings. |
| **Reviews** | Enable users to rate a booked property and provide written feedback. |
| **Blog** | Read destination and travel content, search posts, and browse by category or tag. |
| **About & FAQ** | Present the platform's mission, goals, services, and frequently asked questions. |
| **Admin** | Give administrators one place to manage all platform data and editorial content. |

## User journeys

### Guest journey

1. Open the home page and browse destinations, categories, and highlighted listings.
2. Search or filter the property catalog.
3. Open a property to check its description, photos, price, availability, rating, and related options.
4. Create an account or sign in to make a reservation.
5. Access the profile area to review reservations and leave feedback.

### Property owner journey

1. Sign in to the platform.
2. Create a new property with its image, price, location, category, and description.
3. Open **My Listings** to manage owned properties.
4. Update property information or remove a listing when needed.

### Administrator journey

1. Sign in at `/admin/` with a superuser account.
2. Manage places, categories, properties, property images, reservations, and reviews.
3. Publish blog posts, assign categories and tags, and edit rich text with Summernote.
4. Update site branding, contact information, social links, About content, and FAQs.

## Features

### Properties and reservations

- Browse paginated property listings and filter them by name, description, category, or place.
- View detailed property pages with images, price, description, availability status, average ratings, and related properties.
- Create, update, and delete property listings; only the listing owner can manage their properties.
- Book a property by choosing check-in/out dates and the number of guests and children.
- View personal reservations and personal property listings.
- Create and update property ratings and feedback.

### Accounts and content

- Sign up, sign in, and sign out.
- Update profile details, profile image, phone number, and address.
- Use Django's built-in password change and password reset flows.
- Browse, search, categorize, and tag blog posts.
- Read recent articles and post details.
- Manage an About page and frequently asked questions.
- Display dynamic site information in the footer: logo, social links, contact details, and site description.

### Admin and API

- Django Admin for managing users, properties, reservations, reviews, blog posts, and site settings.
- **Django Summernote** rich-text editor in the admin panel.
- Token-protected REST API with Swagger and ReDoc documentation.

## Technology stack

| Area | Technologies |
| --- | --- |
| Backend | Python 3.13, Django 5.2 |
| Database | SQLite by default |
| API | Django REST Framework, Token Authentication, drf-spectacular |
| Authentication | Django Authentication, django-allauth, dj-rest-auth |
| Search and filtering | django-filter, Django ORM, `Q` queries |
| Content | django-taggit, django-summernote |
| Frontend | Django Templates, Bootstrap 4, jQuery |
| UI enhancements | Owl Carousel, AOS, Magnific Popup, Bootstrap Datepicker, Ionicons, Open Iconic |
| Images and uploads | Pillow, Django media files |
| Deployment | Gunicorn, Procfile; WhiteNoise is included as a dependency for static files |

## Core data model

The application uses Django's built-in `User` model as the center of the platform.

```text
User
 ├── Profile (photo, phone number, address)
 ├── Property (owner)
 │    ├── PropertyImages
 │    ├── PropertyBook (reservation)
 │    └── PropertyReview (rating and feedback)
 └── Post (blog author)

Property → Place
Property → Category
Post     → Category + Tags
```

Key entities include:

| Entity | Purpose |
| --- | --- |
| `Profile` | Extends a Django user with contact details and an optional profile image. |
| `Property` | Represents a bookable hotel, restaurant, or place, owned by a user. |
| `Place` | Represents a destination or location for properties. |
| `Category` | Groups properties, for example Hotel, Restaurant, or Places. |
| `PropertyBook` | Stores a reservation's property, guest, date range, and party size. |
| `PropertyReview` | Stores a user's rating and feedback for a property. |
| `Post` | Stores a blog article with an image, category, tags, author, and slug. |
| `Settings` | Stores the site identity and footer contact/social information. |
| `About` and `FAQ` | Store editable platform information and common questions. |

## Project structure

```text
.
├── accounts/       # Accounts and user profiles
├── property/       # Properties, images, reservations, reviews, and property API
├── blog/           # Posts, categories, tags, and blog API
├── about/          # About page and FAQs
├── settings/       # Home page, search, site settings, and footer context
├── project/        # Django settings, root URLs, WSGI, and ASGI
├── templates/      # Shared base template
├── static/         # CSS, JavaScript, and static images
├── media/          # User-uploaded files and content images
├── requirements.txt
├── Procfile
└── manage.py
```

## Local setup

### Prerequisites

- Python 3.13, or a Python version compatible with Django 5.2
- `pip`
- Git

### Installation

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

# Install these if they are not already available in your environment.
# They are enabled in the Django project settings.
pip install django-allauth dj-rest-auth drf-spectacular

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) after starting the server.

### Useful commands

```bash
# Validate the Django project configuration
python manage.py check

# Run tests
python manage.py test

# Collect static files for deployment
python manage.py collectstatic --noinput
```

## Main routes

| Route | Description |
| --- | --- |
| `/` | Home page with featured categories, places, properties, and posts |
| `/property/` | Filterable property list |
| `/property/create/` | Create a property listing; authentication required |
| `/accounts/signup` | Create an account |
| `/accounts/profile/` | View and manage the user profile |
| `/blog/` | Blog and post search |
| `/about/` | About page and FAQs |
| `/admin/` | Django administration panel |

## REST API and documentation

The API uses Token Authentication. Send the following header with protected requests:

```http
Authorization: Token <your-token>
```

| Route | Purpose |
| --- | --- |
| `/property/api/list/` | List and create properties |
| `/property/api/list/<id>` | Retrieve, update, or delete a property |
| `/blog/api/list/` | List posts |
| `/blog/api/list/<id>/` | Retrieve a post |
| `/blog/api/list/filter/<query>/` | Search posts |
| `/api/schema/` | OpenAPI schema |
| `/api/docs/` | Swagger UI |
| `/api/redoc/` | ReDoc |
| `/rest-auth/` | REST authentication endpoints |
| `/rest-auth/registration/` | REST registration endpoints |

## Production checklist

Do not deploy the development configuration from `project/settings.py` as-is. Before production deployment:

1. Move `SECRET_KEY` to a secure environment variable.
2. Set `DEBUG = False`.
3. Configure `ALLOWED_HOSTS` with your application domains.
4. Replace SQLite with a production-ready database such as PostgreSQL.
5. Configure `STATIC_ROOT` and `MEDIA_ROOT`, and enable WhiteNoise or a CDN for static assets.
6. Never commit passwords, API keys, or production data to GitHub.

The repository contains a `Procfile` for serving the Django application with Gunicorn:

```bash
gunicorn project.wsgi --log-file -
```

## Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a branch: `git checkout -b feature/feature-name`.
3. Make and test your changes.
4. Open a pull request with a clear description of the change.

## Repository notes

- The repository currently has no `LICENSE` file. Add a license, such as MIT, before distributing or reusing the project under defined terms.
- Before making the repository public, add a `.gitignore` to exclude `.venv/`, `__pycache__/`, `db.sqlite3`, uploaded files in `media/`, and system files such as `.DS_Store`.

## Author

**Mohammed Aljazzar**<br>
Contact: [m.i.aljazzar19@gmail.com](mailto:m.i.aljazzar19@gmail.com)
