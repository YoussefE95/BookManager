# Book Management System
## Install Django
This project requires Django to be installed in order to run it. To install Django on your system, run the following command:
```bash
python3 -m pip install Django
```

## Clone the repository and navigate into its directory
```bash
git clone https://github.com/YoussefE95/BookManager
cd BookManager
```

## Pre-run Setup
The following commands, which setup the project's database, must be executed before running the project for the first time.
```bash
python3 manage.py makemigrations BookMng
python3 manage.py migrate
```

## Run the Project
```bash
python3 manage.py runserver
```
