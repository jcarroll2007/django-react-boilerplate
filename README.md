# Get Started

Ok.. get ready - this is a long and complicated process to create your django development box, but it WILL be worth it!

1. `vagrant up`
2. Wait for a few minutes...
3. Still not done? Ok, keep waiting it shouldn't be much longer.
4. It's done! Create your django super user, migrate your database and you're done! Start django-ing away!
    - `cd /vagrant/backend`
    - `python3.6 manage.py makemigrations`
    - `python3.6 manage.py migrate`
    - `python3.6 manage.py createsuperuser`
        - user: `vagrant` (suggested)
        - password: `password1234`
    - navigate to `localhost:8080` and login with the credentials of the superuser you just created.
    - VOILA!


## Client Side

1. `vagrant ssh`
2. `cd /vagrant/frontend`
3. `npm run start`
4. navigate to `localhost:8888`
