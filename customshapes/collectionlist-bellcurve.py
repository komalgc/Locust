from locust import HttpUser, task, between, LoadTestShape

import math

class BuyerBehavior(HttpUser):

    host = "https://api-beta.app.com:6080"

    wait_time = between(1, 5)  # Users will wait between 1 and 5 seconds between tasks

    # Define a function to get the bearer token
   
    def get_token(self):
        # Replace 'your_token_here' with your actual bearer token
        return 'token'
        
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

class BellShapeLoadTest(LoadTestShape):
    """
    The "bell shape" load test pattern increases the number of users gradually to a peak and then decreases them, resembling a bell curve
    """
    time_limit = 60  # Total test time in seconds
    peak_time = 180  # Time to reach peak in seconds
    peak_users = 100  # Maximum number of users

    def tick(self):
        run_time = self.get_run_time()

        if run_time > self.time_limit:
            return None

        user_count = (self.peak_users * (1 - ((run_time - self.peak_time) / self.peak_time) ** 2))

        # Ensure user count is non-negative
        user_count = max(0, round(user_count))

        return user_count, user_count  # User count, spawn rate