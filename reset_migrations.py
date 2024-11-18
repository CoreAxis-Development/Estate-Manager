import os
import shutil
import subprocess

# Define the base directory of your project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define the apps for which you want to delete migrations
apps = ['CheckList', 'AssetManager', 'UserManagement', 'ContactManager', 'Base']

# Delete migration files
for app in apps:
    migrations_dir = os.path.join(BASE_DIR, app, 'migrations')
    if os.path.exists(migrations_dir):
        for filename in os.listdir(migrations_dir):
            file_path = os.path.join(migrations_dir, filename)
            if filename != '__init__.py':
                if os.path.isdir(file_path):
                    shutil.rmtree(file_path)
                else:
                    os.remove(file_path)
        print(f"Deleted migrations for {app}")

# Run makemigrations and migrate
subprocess.run(['python', 'manage.py', 'makemigrations'])
subprocess.run(['python', 'manage.py', 'migrate'])

# Run populate
subprocess.run(['python', 'manage.py', 'populate'])