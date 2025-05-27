# [Baytna](https://www.baytna-berlin.de/)

Baytna is a dynamic and modern website built for a community center located in Berlin, Germany.  
It serves as an online hub where visitors can learn about the center's activities, events, and services.

## 🛠 Tech Stack

**Backend**  
- [Django](https://www.djangoproject.com/) (Python)
- [SQLite3](https://www.sqlite.org/index.html) (Database)

**Frontend**  
- HTML5  
- CSS3  
- JavaScript  
- [Bootstrap](https://getbootstrap.com/) (via StartBootstrap templates)  
- [FontAwesome](https://fontawesome.com/) (icons)  
- [Favicon.cc](https://www.favicon.cc/) (custom favicon)

## 🎨 Design

The visual style is clean, elegant, and accessible. The main color palette includes:  
- **White** (#FFFFFF) – Backgrounds and clean spaces  
- **Black** (#000000) – Primary text and accents  
- **Gold** (#99700a) – Highlights and interactive elements  
- **Grey** (#4D5656) – Secondary text and backgrounds  

The design leverages Bootstrap's grid system to ensure a fully responsive experience across devices.

## install
- pip3 install Django
- pip3 install pillow
- pip install python-decouple
- pip install python-dotenv
- pip install whitenoise
- pip install dj-database-url
- pip install psycopg2-binary 
- pip install gunicorn


## 📂 Project Structure

```
baytna/
├── baytna/            # Django project configuration (settings, urls)
├── community/         # Django app for the community center
│   ├── migrations/
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   ├── templates/
│   │   └── community/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── db.sqlite3          # SQLite database "isn't used"
└── manage.py           # Django's management utility
```

## 🚀 Features

- Informational pages about the community center
- Event and activity listings
- Contact form
- Mobile-responsive layout
- Custom favicon
- Clean typography and consistent iconography
- Optimized for performance and accessibility

## 🏡 Local Development Setup

1. **Clone the repository**  
   ```bash
   git clone https://github.com/Christianalamassi/Baytna.git
   cd baytna
   ```

2. **Create and activate a virtual environment**  
   ```bash
   python -m venv env
   source env/bin/activate   # On Windows use `env\Scripts\activate`
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**  
   ```bash
   python manage.py migrate
   ```

5. **Run the development server**  
   ```bash
   python manage.py runserver
   ```

6. **Access the website**  
   Open your browser and go to [Baytna](https://web-production-d37ff.up.railway.app)

## 📜 License

This project is licensed under the [MIT License](LICENSE).  
Feel free to use, modify, and distribute.

## 🙌 Acknowledgements

- [StartBootstrap](https://startbootstrap.com/) – Templates and UI Kits
- [FontAwesome](https://fontawesome.com/) – Icons
- [Bootstrap](https://getbootstrap.com/) – Frontend framework
- [Favicon.cc](https://www.favicon.cc/) – Favicon creation
- Django Documentation – For backend development

---

Would you also like me to generate a sample `requirements.txt` for you, or a fancier version with badges (build passing, license, etc.)? 🚀