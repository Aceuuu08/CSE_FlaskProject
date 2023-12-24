# GAMING ROSTER MANAGEMENT

### LOTA, ARVIN CLARK T. 
BSCS3 - B1

### You need the following to run the program:
### 1. MySQL
### 2. Flask
### 3. Flask-MySQL
### 4. Postman

## CRUD
- Create
- Read
- Update
- Delete

## Security
- Username = admin
- Password = admin12345

## Steps
- Activate/Create a Virtual Environment.
  - Execute this command (python venv MyVenv) on your terminal to create a Virtual Env.
  - Execute this command (../venv/Scripts/activate.bat) on your terminal to activate the Virtual Env.
- Execute the API.py "python API.py"
- Open your browser and enter "http://127.0.0.1:5000"
- Log in using the given credentials "admin" for the username, and "admin12345" for the password
- Open your POSTMAN then paste the URL
- Select the method you want to do. [POST, GET, PUT, DELETE]
- Go to the Headers tab, and add "Content-type" on the Key column. then "application/json" on the Value column
- Go to the Body tab, write/put the fields and values that you want to insert or to update. (This is not necessary when you use the DELETE method.)
- Lastly, click SEND to execute. and wait for the message if it is successful or not.

## URLS or API END POINTS
- http://127.0.0.1:5000/login # login page
- http://127.0.0.1:5000/logout # to logout
- GET http://127.0.0.1:5000/player # to view all the Player profile
- POST http://127.0.0.1:5000/player # to add another Player profile
- PUT http://127.0.0.1:5000/player/int:id # input the ID of the player you want to UPDATE 
- DELETE http://127.0.0.1:5000/player/int:id # input the ID of the player you want to DELETE

## Video Explainer
https://drive.google.com/file/d/1UhTE7lOI_MGFNJtTkcyB2kWaXG4J3lFf/view?usp=sharing
