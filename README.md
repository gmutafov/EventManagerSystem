# EventManagerSystem
_A project for my Django Advanced Course at SoftUni._

- Deployed at: https://eventmanager-d5hwhfepdrb9h8a7.italynorth-01.azurewebsites.net

# Project Setup

**1. Clone the repository:**
```bash
git clone https://github.com/gmutafov/EventManagerSystem.git
```
**2. Open the project**

**3. Install dependencies**
  ```bash

  pip install -r requirements.txt
```
**4. Change DB settings in settings.py**
```bash

     DATABASES = {
      "default": {
          "ENGINE": "django.db.backends.postgresql",
          "NAME": "your_db_name",
          "USER": "your_username",
          "PASSWORD": "your_pass",
          "HOST": "127.0.0.1",
          "PORT": "5432",
      }
  }
  ```

**5. Run the migration**
 ```bash

  python manage.py migrate
```
**6. Run the project**
  ```bash

  python manage.py runserver
```

# 📖 Overview
The Event Management System is a Django-based web application designed to simplify the creation, organization, and management of events. It enables users to register for events, staff to create events, book venues, and collaborate with organizers, all through a user-friendly interface.

# 🛠 Features
User Management:

- Custom user model (CustomUser).
- Profile pages with editable profile details and profile picture upload.
- Secure login/logout functionality.

Event Management:

- Create, edit, and delete events.
- Assign venues and organizers to events.
- View event details and lists.

Venue and Organizer Models:

- Manage venues (name, location, capacity).
- Organizer profiles linked to user accounts.

Responsive Design:

Fully responsive UI powered by Bootstrap.

🧑‍💻 Tech Stack
- Backend: Django, Python
- Database: PostgreSQL
- Frontend: HTML, CSS, Bootstrap
- Tools: Django Class-Based Views (CBVs), Custom Validators
