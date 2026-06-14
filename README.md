# Secure Django Task Manager 
Secure Software Development using Django Python  
It is recommended to run using kali linux in virtual box.


- Repository Cloning
- Fetch the repository codebase down to your localized development space:
Run in VSC Terminal:

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

# Run on Kali Linux  
- Install the Native Linux System Dependency

sudo apt update  
sudo apt install libmagic1 -y

# Clone and Enter the Project Folder  
git clone https://github.com/Wan768/Secure-Task-Manager.git  
cd Secure-Task-Manager  

# Activate Environment  
python3 -m venv venv  
source venv/bin/activate

# Install packages  
pip install --upgrade pip  
pip install -r requirements.txt

# Generate Django Secret Key  
python3 -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"  

# Create .env file  
nano .env  

# Paste the generated key inside .env file    
SECRET_KEY=your_generated_random_key_here  
DEBUG=True

- Save and exit the editor

# Setup Database & Admin Account  
python3 manage.py makemigrations  
python3 manage.py migrate  
python3 manage.py createsuperuser  

# Launch the Application  
python3 manage.py runserver  

# Access Admin Dashboard
Add /admin at the url link
