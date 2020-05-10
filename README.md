# dj-user-profile
# Installation
1. `git clone https://github.com/senya96/dj-user-profile.git`
2. `cd dj-user-profile`
3. `python3.7 -m venv venv`
4. `source venv/bin/activate`
5. `export DATABASE_URL=postgresql://<db_user>:<db_pass>@<db_host>:<db_port>/<db_name>`
6. `./manage.py migrate`
7. `./manage.py collectstatic`
8. `./manage.py runserver 0.0.0.0:8000`
9. Open in browser http://localhost:8000
