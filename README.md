# 🚀 API Performance Testing using Locust

This project sets up **API performance testing using [Locust](https://locust.io/)**—a scalable, open-source load testing tool that lets you simulate thousands of concurrent users to test the performance of your API endpoints.

---

## 📌 What Is Locust?

Locust is a modern load testing tool that allows you to write test scenarios in **Python**. It's developer-friendly, supports real-time web UI monitoring, and integrates easily with CI/CD pipelines.

---

## 🧪 What You Can Test

- Concurrent user load on REST APIs
- Response time under load
- RPS (Requests Per Second) benchmarking
- Performance regressions
- Load limits and bottlenecks
- Apply Custom Load shapes 

---

## Install Dependencies 
pip install -r requirements.txt





### 1. Create Virtual Environment 

1) Go to project directory and Create a virtual environment using `python -m venv venv`
2) Type `venv\Scripts\activate.bat` and hit enter
3) Create a requirements.txt file and add the required library. For Ex: To install locust, add locust==2.24.0 in the file. (This i have added alerady)
4) Run the command to install the library. `pip install -r requirements.txt`.
5) Run the application `locust -f getorder.py`


### 2. Launch Locust Web UI:

locust -f locustfile.py --host=http://localhost:8000

### 3. Open browser and navigate to:

http://localhost:8089


Enter load parameters:

Number of users (e.g., 100)
Spawn rate (e.g., 10 users/sec)
Click Start Swarming

📈 Using Custom Load Shape
For more control over traffic patterns (e.g., ramp-up, plateau, ramp-down), use a custom load shape defined in customshapes/collectionlist-bellcurve.py

✅ Run with Custom Load Shape
locust -f locustfile.py load_shape.py --host=http://localhost:8000

🛠️ Headless Mode (CI/CD)
locust -f locustfile.py --host=http://localhost:8000 --headless -u 100 -r 10 -t 2m

📊 Metrics Observed
Requests per second (RPS)

Average and percentile response times (p50, p95)

Failure rates

Active users and throughput over time








