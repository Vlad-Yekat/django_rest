# testing docker+autotest+django rest

#1 main view root
http://127.0.0.1:8000/

#1.1 first page
http://127.0.0.1:8000/newver2/

#1.2 second page
http://127.0.0.1:8000/newver2/?page=2

#1.3 detail page
http://127.0.0.1:8000/newver2/1/

#1.4 query

#2. migration
for initial migration example you can use
insidepages/for_migration

#3. sample test.py
python manage.py test

#4. Celery
TODO soon

#5 for create docker container:
#5.1
docker-compose run web python mixcontent/manage.py migrate
#5.2
docker-compose build
#5.3
docker-compose up
 