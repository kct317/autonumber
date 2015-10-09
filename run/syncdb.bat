cd ..
python manage.py check
python manage.py makemigrations
python manage.py migrate > run/migrate.txt
pause