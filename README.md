# Testing docker + autotest + django rest API

# 1 for create docker container:
#1.1
docker-compose run web python mixcontent/manage.py migrate
#1.2
docker-compose build
#1.3
docker-compose up


#2 Look on API
#2.1 root directory
http://0.0.0.0:8000/

#2.2 list all pages
http://0.0.0.0:8000/newver2/

#2.3 page 2 if exist
http://0.0.0.0:8000/newver2/?page=2