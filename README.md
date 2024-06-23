Personalized Parent Onboarding Backend System
Overview
This Django-based backend system provides a personalized onboarding experience for parents, focusing on collecting essential details about the parent and their child. Based on the child's age, it generates a customized home feed consisting of blogs and vlogs. Customization options include the child's age group, gender, and the parent's type (e.g., first-time parent, experienced parent). The system also efficiently manages and stores blog content.

Features
Parent Management:

Register new parents with details such as email, parent names, parent type, contact information, and address.
Retrieve, update, and delete parent profiles.
Child Management:

Add children to parent profiles with attributes like name, age, and gender.
Manage child profiles within parent accounts.
Content Management:

Create, retrieve, update, and delete blog and vlog content.
Filter content based on child's age group, gender, and parent's type.
Efficient storage and retrieval of blog and vlog data.
Personalized Home Feed:

Generate a tailored feed of blogs and vlogs based on child's age, gender, and parent's type.
Flexibility in content delivery based on user preferences.
Technologies Used
Backend Framework: Django
API Development: Django REST Framework (DRF)
Documentation: Swagger
Installation
Clone the Repository:

bash
Copy code
git clone <repository-url>
cd <project-directory>
Set Up Virtual Environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Run Migrations:

bash
Copy code
python manage.py migrate
Create a Superuser (Admin):

bash
Copy code
python manage.py createsuperuser
Start the Development Server:

bash
Copy code
python manage.py runserver
Access API Documentation:

Open your browser and navigate to http://127.0.0.1:8000/api/v1/swagger-ui/ for Swagger documentation.
API Endpoints
Parent Management
GET /api/v1/parent/: Retrieve all parents.
POST /api/v1/parent/: Create a new parent.
GET /api/v1/parent/{id}/: Retrieve details of a specific parent.
PUT /api/v1/parent/{id}/: Update details of a specific parent.
DELETE /api/v1/parent/{id}/: Delete a specific parent.
Child Management
GET /api/v1/child/: Retrieve all children.
POST /api/v1/child/: Create a new child for a parent.
GET /api/v1/child/{id}/: Retrieve details of a specific child.
PUT /api/v1/child/{id}/: Update details of a specific child.
DELETE /api/v1/child/{id}/: Delete a specific child.
Content Management
GET /api/v1/content/: Retrieve all blog and vlog content.
POST /api/v1/content/: Create new blog or vlog content.
GET /api/v1/content/{id}/: Retrieve details of specific blog or vlog content.
PUT /api/v1/content/{id}/: Update details of specific blog or vlog content.
DELETE /api/v1/content/{id}/: Delete specific blog or vlog content.
Personalized Home Feed
GET /api/v1/blog/personalized-feed/{parent_id}/: Retrieve personalized blog and vlog feed based on parent's preferences.
