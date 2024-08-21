Create an individual virtual environment

1) Go to project directory and Create a virtual environment using `python -m venv venv`
2) Type `venv\Scripts\activate.bat` and hit enter
3) Create a requirements.txt file and add the required library. For Ex: To install locust, add locust==2.24.0 in the file. (This i have added alerady)
4) Run the command to install the library. `pip install -r requirements.txt`.
5) Run the application `locust -f getorder.py`