echo "BUILD START"
python3.9 -m pip install django
python3.9 -m pip install djangorestframework
python3.9 -m pip install pyyaml
python3.9 -m pip install requests
python3.9 -m pip install django-cors-headers
python3.9 -m pip install pymongo==3.12.3
python3.9 -m pip install djongo==1.3.6
python3.9 manage.py collectstatic --noinput --clear
python3.9 manage.py runserver 0.0.0.0:8000
echo "BUILD END"