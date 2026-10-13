# Student Result Portal

A Django web application to manage student records and their subject-wise results. Grades are calculated automatically from marks.

## Features
- Add, view, edit and delete students (CRUD)
- Add subject-wise marks for each student
- Grade calculated automatically from marks (A+ to Fail)
- Form validation: unique roll number, marks limited to 0-100
- Django Admin panel for managing data
- Template inheritance for a consistent layout across pages

## Tech Stack
- Python
- Django
- SQLite
- HTML (Django templates)

## Data Models
- **Student:** name, roll number (unique), email
- **Result:** student (ForeignKey), subject, marks

## Grading Scale
| Marks | Grade |
|-------|-------|
| 90 and above | A+ |
| 80 - 89 | A |
| 70 - 79 | B |
| 60 - 69 | C |
| 40 - 59 | D |
| Below 40 | Fail |

## Run Locally
1. Clone the repository
   git clone https://github.com/aditya-encode/student-result-portal.git
   cd student-result-portal
2. Create and activate a virtual environment
   python -m venv venv
   venv\Scripts\activate
3. Install Django
   pip install django
4. Set up the database
   python manage.py migrate
5. Create an admin user
   python manage.py createsuperuser
6. Start the server
   python manage.py runserver
7. Open http://127.0.0.1:8000/ (admin panel at /admin)

## Author
Aditya Patel