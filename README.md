 step-by-step instructions to set up and run the Python Django project locally.

### Prerequisites
Ensure you have the following installed on your local system:
- Python (Latest stable version)
- Virtual Environment


1. Clone the Repository
   
 ``` git clone https://github.com/Ajmal-AJ/jobapplicationportal-API.git ```

  ``` cd jobapplicationportal ```

2. Create and Activate a Virtual Environment
   
     ```python -m venv env```
   
     ```env\Scripts\activate```
   
4. Install Dependencies
   
   ```pip install -r requirements.txt```
   
5. Apply Migrations
   
     ``` python manage.py makemigrations ```
   
     ``` python manage.py migrate ```
   
7. Run the Server

 ``` python manage.py runserver ```
 
6. Open the Application

  [ http://127.0.0.1:8000/api ]
