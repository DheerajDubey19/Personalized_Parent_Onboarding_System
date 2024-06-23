# Personalized Parent Onboarding Backend System

## Overview

The **Personalized Parent Onboarding Backend System** is a Django-based API service designed to facilitate a tailored onboarding experience for parents. It enables the collection of essential details about parents and their children, generating a personalized home feed comprising blogs and vlogs based on the child's age, gender, and the parent's type (e.g., first-time parent, experienced parent). The system also provides efficient management and storage of blog content.

## Features

- **Parent Management:**
  - Register new parents with details such as email, parent names, parent type, contact information, and address.
  - Retrieve, update, and delete parent profiles.

- **Child Management:**
  - Add children to parent profiles with attributes like name, age, and gender.
  - Manage child profiles within parent accounts.

- **Content Management:**
  - Create, retrieve, update, and delete blog and vlog content.
  - Filter content based on child's age group, gender, and parent's type.
  - Efficient storage and retrieval of blog and vlog data.

- **Personalized Home Feed:**
  - Generate a tailored feed of blogs and vlogs based on child's age, gender, and parent's type.
  - Flexibility in content delivery based on user preferences.

## Technologies Used

- **Backend Framework:** Django
- **API Development:** Django REST Framework (DRF)
- **Documentation:** Swagger

## Installation

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. **Set Up Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a Superuser (Admin):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the Development Server:**
   ```bash
   python manage.py runserver
   ```

7. **Access API Documentation:**
   - Open your browser and navigate to `http://127.0.0.1:8000/api/v1/swagger-ui/` for Swagger documentation.

## API Endpoints

### Parent Management

- **GET /api/v1/parent/**: Retrieve all parents.
- **POST /api/v1/parent/**: Create a new parent.
- **GET /api/v1/parent/{id}/**: Retrieve details of a specific parent.
- **PUT /api/v1/parent/{id}/**: Update details of a specific parent.
- **DELETE /api/v1/parent/{id}/**: Delete a specific parent.

### Child Management

- **GET /api/v1/child/**: Retrieve all children.
- **POST /api/v1/child/**: Create a new child for a parent.
- **GET /api/v1/child/{id}/**: Retrieve details of a specific child.
- **PUT /api/v1/child/{id}/**: Update details of a specific child.
- **DELETE /api/v1/child/{id}/**: Delete a specific child.

### Content Management

- **GET /api/v1/content/**: Retrieve all blog and vlog content.
- **POST /api/v1/content/**: Create new blog or vlog content.
- **GET /api/v1/content/{id}/**: Retrieve details of specific blog or vlog content.
- **PUT /api/v1/content/{id}/**: Update details of specific blog or vlog content.
- **DELETE /api/v1/content/{id}/**: Delete specific blog or vlog content.

### Personalized Home Feed

- **GET /api/v1/blog/personalized-feed/{parent_id}/**: Retrieve personalized blog and vlog feed based on parent's preferences.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and create a pull request. Follow the project's coding standards and conventions.

## License

This project is licensed under the [MIT License](LICENSE).

---

This README template provides a clear and concise overview of your project, including setup instructions, API endpoints, technologies used, and guidelines for contributing. Feel free to customize it further to include additional details specific to your project's requirements and context.
