
![Torob-Watcher](https://github.com/h4mid-hosseini/torob-price-watcher/assets/29615771/ab94e8d1-5adb-4e31-85ca-d71e9c4aa6ea)



This project is a simple Django based application that watchs the Torob.com products to check price decrease below the certian price you want!

**Running The App:**

To run the app follow these step:
1. create a venv using python -m venv .venv
2. install requred packages using pip install -r requrements.txt
3. change directory to main folder using cd TorobWatcher
4. run project with python manage.py runserver

after login, you can add a product with your own desire. 
by making a get request to /watch-dog/update/ the updating process will start.

**Consideration:**

1. You will need to create a superuser to login to admin panel

2. Add your own email information to enable emailing feature
