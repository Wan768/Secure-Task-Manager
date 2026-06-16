# Secure Django Task Manager 
Secure Software Development using Django Python  
It is recommended to run using kali linux in virtual box.
If running in windows, use the incognito tab to run the web app to avoid error.

# Repository Cloning
Run in VSC Terminal:

git clone https://github.com/Wan768/Secure-Task-Manager.git


# Windows
`python -m venv venv ` 
<br>
`venv\Scripts\activate`

# macOS/Linux
`python3 -m venv venv`
<br>
`source venv/bin/activate`

# Install requirements 
`pip install -r requirements.txt`

# Generate django secret key
`python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`

# Create a file named .env directly inside the root folder (where manage.py lives) and copy the following configuration block into it:
Paste the key generated in the .env file
# .env File
`SECRET_KEY=django-insecure-local-dev-token-replace-this-with-a-stochastic-hash`
<br>
`DEBUG=True`

# Generate & apply necessary database schema updates to the local environment by running:
`python manage.py makemigrations`
<br>
`python manage.py migrate`

# If any errors arise when running the last 2 commands, try running these commands first 
`pip uninstall python-magic`
<br>
`pip install python-magic-bin`

- If successful, rerun the commands `python manage.py makemigrations` & `python manage.py migrate`

# Create superuser/admin to create an account as admin to access admin dashboard
`python manage.py createsuperuser`

# Run Server
`python manage.py runserver`

# Access Admin Dashboard
Add `/admin` at the url link

# Run on Kali Linux  
- Install the Native Linux System Dependency

`sudo apt update`
<br>
`sudo apt install libmagic1 -y`

# Clone and Enter the Project Folder  
`git clone https://github.com/Wan768/Secure-Task-Manager.git`
<br>
`cd Secure-Task-Manager`

# Activate Environment  
`python3 -m venv venv`
<br>
`source venv/bin/activate`

# Install packages  
`pip install --upgrade pip`
<br>
`pip install -r requirements.txt`

# Generate Django Secret Key  
`python3 -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"` 

# Create .env file  
`nano .env`  

# Paste the generated key inside .env file    
`SECRET_KEY=your_generated_random_key_here  
DEBUG=True`

- Save and exit the editor

# Setup Database & Admin Account  
`python3 manage.py makemigrations`  
<br>
`python3 manage.py migrate`
<br>
`python3 manage.py createsuperuser`  

# Launch the Application  
`python3 manage.py runserver` 

# Access Admin Dashboard
Add `/admin` at the url link  
