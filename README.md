# Secure Django Task Manager 
Secure Software Development using Django Python


- Repository Cloning
- Fetch the repository codebase down to your localized development space:
Run in VSC Terminal:
bash
git clone https://github.com/Wan768/Secure-Task-Manager.git


# Windows
python -m venv venv  
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv  
source venv/bin/activate

# Install requirements 
pip install -r requirements.txt

# Generate django secret key
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

# Create a file named .env directly inside the root folder (where manage.py lives) and copy the following configuration block into it:
Paste the key generated in the .env file
# .env File
SECRET_KEY=django-insecure-local-dev-token-replace-this-with-a-stochastic-hash  
DEBUG=True

python manage.py makemigrations  
python manage.py migrate

# Create superuser/admin; It wil be used when login as admin to access admin dashboard
python manage.py createsuperuser

# Run Server
python manage.py runserver

# Access Admin Dashboard
Add /admin at the url link
