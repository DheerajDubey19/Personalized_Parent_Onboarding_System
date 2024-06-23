<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Personalized Parent Onboarding Backend System</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            padding: 20px;
            max-width: 800px;
            margin: 0 auto;
        }

        h1 {
            text-align: center;
            margin-bottom: 20px;
        }

        h2 {
            margin-top: 30px;
            margin-bottom: 10px;
        }

        p {
            margin-bottom: 10px;
        }

        ul {
            margin-bottom: 20px;
        }

        code {
            background-color: #f4f4f4;
            padding: 5px;
            border-radius: 5px;
            font-family: monospace;
        }

        .api-endpoint {
            margin-top: 10px;
            margin-bottom: 10px;
            padding: 10px;
            border: 1px solid #ccc;
            background-color: #f9f9f9;
        }

        .api-description {
            margin-bottom: 15px;
        }

        .installation-steps {
            margin-bottom: 20px;
        }

        .note {
            background-color: #f0f0f0;
            padding: 10px;
            border-left: 4px solid #ccc;
            margin-bottom: 15px;
        }

        .footer {
            margin-top: 50px;
            font-size: 0.8em;
            color: #666;
            text-align: center;
        }
    </style>
</head>

<body>

    <h1>Personalized Parent Onboarding Backend System</h1>

    <div class="api-description">
        <p>This Django-based backend system provides a personalized onboarding experience for parents, focusing on
            collecting essential details about the parent and their child. Based on the child's age, it generates a
            customized home feed consisting of blogs and vlogs. Customization options include the child's age group,
            gender, and the parent's type (e.g., first-time parent, experienced parent). The system also efficiently
            manages and stores blog content.</p>
    </div>

    <h2>Features</h2>
    <ul>
        <li><strong>Parent Management:</strong>
            <ul>
                <li>Register new parents with details such as email, parent names, parent type, contact information, and
                    address.</li>
                <li>Retrieve, update, and delete parent profiles.</li>
            </ul>
        </li>
        <li><strong>Child Management:</strong>
            <ul>
                <li>Add children to parent profiles with attributes like name, age, and gender.</li>
                <li>Manage child profiles within parent accounts.</li>
            </ul>
        </li>
        <li><strong>Content Management:</strong>
            <ul>
                <li>Create, retrieve, update, and delete blog and vlog content.</li>
                <li>Filter content based on child's age group, gender, and parent's type.</li>
                <li>Efficient storage and retrieval of blog and vlog data.</li>
            </ul>
        </li>
        <li><strong>Personalized Home Feed:</strong>
            <ul>
                <li>Generate a tailored feed of blogs and vlogs based on child's age, gender, and parent's type.</li>
                <li>Flexibility in content delivery based on user preferences.</li>
            </ul>
        </li>
    </ul>

    <h2>Technologies Used</h2>
    <ul>
        <li><strong>Backend Framework:</strong> Django</li>
        <li><strong>API Development:</strong> Django REST Framework (DRF)</li>
        <li><strong>Documentation:</strong> Swagger</li>
    </ul>

    <h2>Installation</h2>
    <ol class="installation-steps">
        <li><strong>Clone the Repository:</strong><br>
            <code>git clone &lt;repository-url&gt;<br>
                cd &lt;project-directory&gt;</code></li>
        <li><strong>Set Up Virtual Environment:</strong><br>
            <code>python -m venv venv<br>
                source venv/bin/activate</code> (On Windows use <code>venv\Scripts\activate</code>)</li>
        <li><strong>Install Dependencies:</strong><br>
            <code>pip install -r requirements.txt</code></li>
        <li><strong>Run Migrations:</strong><br>
            <code>python manage.py migrate</code></li>
        <li><strong>Create a Superuser (Admin):</strong><br>
            <code>python manage.py createsuperuser</code></li>
        <li><strong>Start the Development Server:</strong><br>
            <code>python manage.py runserver</code></li>
        <li><strong>Access API Documentation:</strong><br>
            Open your browser and navigate to <code>http://127.0.0.1:8000/api/v1/swagger-ui/</code> for Swagger
            documentation.</li>
    </ol>

    <h2>API Endpoints</h2>

    <div class="api-endpoint">
        <h3>Parent Management</h3>
        <ul>
            <li><strong>GET /api/v1/parent/</strong>: Retrieve all parents.</li>
            <li><strong>POST /api/v1/parent/</strong>: Create a new parent.</li>
            <li><strong>GET /api/v1/parent/{id}/</strong>: Retrieve details of a specific parent.</li>
            <li><strong>PUT /api/v1/parent/{id}/</strong>: Update details of a specific parent.</li>
            <li><strong>DELETE /api/v1/parent/{id}/</strong>: Delete a specific parent.</li>
        </ul>
    </div>

    <div class="api-endpoint">
        <h3>Child Management</h3>
        <ul>
            <li><strong>GET /api/v1/child/</strong>: Retrieve all children.</li>
            <li><strong>POST /api/v1/child/</strong>: Create a new child for a parent.</li>
            <li><strong>GET /api/v1/child/{id}/</strong>: Retrieve details of a specific child.</li>
            <li><strong>PUT /api/v1/child/{id}/</strong>: Update details of a specific child.</li>
            <li><strong>DELETE /api/v1/child/{id}/</strong>: Delete a specific child.</li>
        </ul>
    </div>

    <div class="api-endpoint">
        <h3>Content Management</h3>
        <ul>
            <li><strong>GET /api/v1/content/</strong>: Retrieve all blog and vlog content.</li>
            <li><strong>POST /api/v1/content/</strong>: Create new blog or vlog content.</li>
            <li><strong>GET /api/v1/content/{id}/</strong>: Retrieve details of specific blog or vlog content.</li>
            <li><strong>PUT /api/v1/content/{id}/</strong>: Update details of specific blog or vlog content.</li>
            <li><strong>DELETE /api/v1/content/{id}/</strong>: Delete specific blog or vlog content.</li>
        </ul>
    </div>

    <div class="api-endpoint">
        <h3>Personalized Home Feed</h3>
        <ul>
            <li><strong>GET /api/v1/blog/personalized-feed/{parent_id}/</strong>: Retrieve personalized blog and vlog
                feed based on parent's preferences.</li>
        </ul>
  
    </div>

</body>

</html>
