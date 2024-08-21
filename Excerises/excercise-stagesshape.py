from locust import HttpUser, task, between, LoadTestShape

import math

class Endpointfunctionality(HttpUser):

    host = "https://example.com:6080"

    wait_time = between(1, 5)  # Users will wait between 1 and 5 seconds between tasks

    # Define a function to get the bearer token
   
    def get_token(self):
        # Replace 'your_token_here' with your actual bearer token
        return 'eby'
    @task
    def postrequestAPI(self):

         # Define the headers with the bearer token
        headers = {
            'Authorization': f'Bearer {self.get_token()}'
        }

        # Define the endpoint
        endpoint = "/example/v5/buyer"


             
        # Parameters to be sent with the request
        params = {
            "param1": "123"
     
        }

           # payload to be sent with the request
        payload = {
                      "payload1": "123",
            "payload2": 10,
            "offset": 0
        }
        

     

        # Making the GET request with the specified parameters
        response = self.client.post(endpoint, params=params,json=payload,headers=headers)

       # Print the response status code and content if needed
        print(f"Response Status Code: {response.status_code}")
        # print(response.text)  # Uncomment to print response content


class StagesShape(LoadTestShape):
    """
    A simply load test shape class that has different user and spawn_rate at
    different stages.

    Keyword arguments:

        stages -- A list of dicts, each representing a stage with the following keys:
            duration -- When this many seconds pass the test is advanced to the next stage
            users -- Total user count
            spawn_rate -- Number of users to start/stop per second
            stop -- A boolean that can stop that test at a specific stage

        stop_at_end -- Can be set to stop once all stages have run.
    """

    stages = [
        {"duration": 60, "users": 10, "spawn_rate": 10},
        {"duration": 100, "users": 50, "spawn_rate": 10},
        {"duration": 180, "users": 100, "spawn_rate": 10},
        {"duration": 220, "users": 30, "spawn_rate": 10},
        {"duration": 230, "users": 10, "spawn_rate": 10},
        {"duration": 240, "users": 1, "spawn_rate": 1},
    ]

    def tick(self):
        run_time = self.get_run_time()

        for stage in self.stages:
            if run_time < stage["duration"]:
                tick_data = (stage["users"], stage["spawn_rate"])
                return tick_data

        return None