
# Smart Shop
## Installation
Just follow this steps to run locally

Clone this project in your directory

```bash
git clone https://github.com/supsa-ak/smart-shop.git
```
    
Go to "smart-shop" folder
```bash
cd .\smart-shop\
```

Create Virtual Environment
```bash
virtualenv env
```

Activate Virtual Environment
```bash
.\env\Scripts\activate
```

Install neccessary libraries and packages
```bash
pip install -r requirements.txt
```

Create migrations of Database
```bash
python manage.py makemigrations
python manage.py makemigrations core
```

Migrate Database
```bash
python manage.py migrate
```

Create Super Admin User
```bash
python manage.py createsuperuser
```

Run Django Project
```bash
python manage.py runserver
```



Development server will start at http://127.0.0.1:8000/
