# User Registration and Dash Board

This project is a combination of a Django backend and a React frontend.
Prerequisites
- Python 3.x installed
- Node.js and npm installed
- MySQL or another database server installed

Getting Started
1. Clone the Repository: https://github.com/rightaswanth/Section-1.git (push)
    ```bash
    git clone https://github.com/your-username/your-project.git
    cd UserRegistration
    ```
2. Backend Setup:

    ```bash
    cd UserRegistration
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3. Database Setup:
   Create a MySQL database (or another database of your choice).
   Update the database configuration in `UserRegistration/UserRegistration/settings.py`:

        ```python
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'your_database_name',
                'USER': 'your_database_user',
                'PASSWORD': 'your_database_password',
                'HOST': 'localhost',
                'PORT': '3306',
            }
        }
        ```

    - Apply migrations:

        ```bash
        python manage.py makemigrations
        python manage.py migrate
        ```
4. Frontend Setup:

    ```bash
    cd ../myreactapp
    npm install
    ```

5. Run the Application:
In one terminal, start the Django development server:
        ```bash
        cd UserRegistration
        python manage.py runserver
        ```
In another terminal, start the React development server:
        ```bash
        cd myreactapp
        npm start
        ```
7. Access the Application:

    Open your web browser and go to http://localhost:3000/. You should see your application running.

## Additional Notes

- If you encounter any issues, check the respective `README` files in the `UserRegistration` and `myreactapp` directories for troubleshooting steps.

- This is a basic setup. Depending on your project's complexity, you might need additional configurations and steps.

Happy coding!
