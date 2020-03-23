Important Note: I'm using pyhton version == 3.7.3 in this project.
------------------------------------------------------------------

Follow below instruction carefully step-by-step :
-------------------------------------------------

1. Create virtual environment and activate it
2. Install all the requirements present in requirements.txt file by using below command

pip install -r requirements.txt

3. Run below command to migrate models into database (sqlite3)
---------------------------------------------------------------
python manage.py migrate

4. create superuser by using following command :
--------------------------------------------------

python manage.py createsuperuser


5. Run the server by using following command :
-----------------------------------------------
python manage.py runserver

7. Go to browser and open following url : 

http://localhost:8000

6.  Read and follow further instructions carefully step-by-step on Home page of the website to use the website.
------------------------------------------------------------------------------------------------------

[Note : I'm using bootstrap4 CDN for UI so please make sure You are connected with internet while running the project on browser for best view]



