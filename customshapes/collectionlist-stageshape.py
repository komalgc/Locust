from locust import HttpUser, task, between, LoadTestShape

import math

class BuyerBehavior(HttpUser):

    host = "https://api-beta.qalara.com:6080"

    wait_time = between(1, 5)  # Users will wait between 1 and 5 seconds between tasks

    # Define a function to get the bearer token
   
    def get_token(self):
        # Replace 'your_token_here' with your actual bearer token
        return 'eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJic042VnhNOWl3d3ZDRjYwQndkR3VoakF5Snp3QWF6X2ktRDdfR2JlQUNNIn0.eyJleHAiOjE3MTA0MTUzNjIsImlhdCI6MTcxMDQwNDU2MiwianRpIjoiM2Q5M2NlMjctMDE4My00NzliLWEwYzQtNmJiM2NjOTc5NGVhIiwiaXNzIjoiaHR0cHM6Ly9pZGVudGl0eS5xYWxhcmEuY29tL2F1dGgvcmVhbG1zL0dvbGRlbkJpcmQiLCJhdWQiOiJhY2NvdW50Iiwic3ViIjoiYTllNWI5ZWItYWNhNy00MWFlLWFiYTctNmEyZDAyYWY2YzZkIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoibmV4dCIsInNlc3Npb25fc3RhdGUiOiI2MWFmZTgxOC1mZmM0LTRjNDMtOTMyYi00NWU1MTI4ZmM0NDIiLCJhY3IiOiIxIiwiYWxsb3dlZC1vcmlnaW5zIjpbImh0dHBzOi8vd3d3LnF1b3RlYWRtaW4ucWFsYXJhLmNvbS8qIiwiaHR0cHM6Ly93d3cucWFsYXJhLmNvbSIsImh0dHBzOi8vd3d3LmJ1eWVyYWRtaW4ucWFsYXJhLmNvbSIsImh0dHBzOi8vd3d3LnByb21vYWRtaW4ucWFsYXJhLmNvbS8qIiwiaHR0cHM6Ly93d3cucG9hZG1pbi5xYWxhcmEuY29tLyoiLCJodHRwOi8vcWFsYXJhLmNvbS8qIiwiaHR0cHM6Ly93d3cucHJvZHVjdGFkbWluLnFhbGFyYS5jb20iLCJodHRwczovL3d3dy5xYWxhcmEuY29tLyoiLCJodHRwczovL3d3dy5xYWxhcmEuY29tLyIsImh0dHBzOi8vd3d3Lm9yZGVyYWRtaW4ucWFsYXJhLmNvbS8qIiwiaHR0cHM6Ly9xYWxhcmEuY29tLyoiLCJodHRwczovL2Nkbi5xYWxhcmEuY29tIiwiaHR0cHM6Ly93d3cucXVvdGVhZG1pbi5xYWxhcmEuY29tIiwiaHR0cHM6Ly93d3cucHJvZHVjdGFkbWluLnFhbGFyYS5jb20vKiIsImh0dHBzOi8vd3d3LnBvYWRtaW4ucWFsYXJhLmNvbSIsImh0dHBzOi8vd3d3Lm9yZGVyYWRtaW4ucWFsYXJhLmNvbSIsImh0dHBzOi8vd3d3LmJ1eWVyYWRtaW4ucWFsYXJhLmNvbS8qIiwiaHR0cHM6Ly8qLnFhbGFyYS5jb20vKiJdLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsiUFJPRFVDVF9BRE1JTl9VSSIsIlNFTExFUl9BRE1JTl9VSSIsIlZJRVdfU0VMTEVSX0hPTUUiLCJTSElQTUVOVF9NQU5BR0VNRU5UX1VJIiwiUFJPTU9fQURNSU4iLCJCVVlFUl9PUkdfT1dORVIiLCJPUFNfQURNSU4iLCJWSUVXX1BST0ZJTEUiLCJQT19BRE1JTiIsIm9mZmxpbmVfYWNjZXNzIiwiUVVPVEVfQURNSU5fVUkiLCJ1bWFfYXV0aG9yaXphdGlvbiIsIk9SREVSX0FETUlOX1VJIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJwcm9maWxlIiwic2lkIjoiNjFhZmU4MTgtZmZjNC00YzQzLTkzMmItNDVlNTEyOGZjNDQyIn0.KrJeKPnVFeL3CkmuT3Tqx1pqd4Pj73UQKGz7rgLEhKUCQqR2uyKAoXuDIvOIOVZxCUXJ0x6t7637Ac3Zqq6_uWtddrIkYXqBuAaTnB2cSjYF-clJIy9IzqTTIVG4S_OsG4MTAigR0YD8JlMDm728KRkXQD1KIiuLovinU_uNhwiKSQdp8mr7EbMaMBB5vfbVJS2CiBe7p8z1ozb9LUL551VbtgJ2Q6e2h-SmUZJtXSLWsBISxCJLWDOJS-D1GYroyD6l_dHxhGHFny6FUYhYIFtwwvh6GBb2uijG2aGk6APvJnvyGILfuj7oF5x2dpGObT0XAZ2jaHXsN1W3We7YSw'
            
    @task
    def get_buyer_collection(self):

         # Define the headers with the bearer token
        headers = {
            'Authorization': f'Bearer {self.get_token()}'
        }

        # Define the endpoint
        endpoint = "/collections/v5/buyer"


             
        # Parameters to be sent with the request
        params = {
            "buyer_id": "BU18923"
     
        }

           # payload to be sent with the request
        payload = {
                      "currency": "USD",
            "limit": 10,
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