from locust import HttpUser, task, between, LoadTestShape

import math

class BuyerBehavior(HttpUser):

    host = "https://api-beta.qalara.com:6080"

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


class DoubleWave(LoadTestShape):
    """
    A shape to imitate some specific user behaviour. In this example, midday
    and evening shopping  times. First peak of users appear at time_limit/3 and
    second peak appears at 2*time_limit/3

    Settings:
        min_users -- minimum users
        peak_one_users -- users in first peak
        peak_two_users -- users in second peak
        time_limit -- total length of test
    """

    min_users = 20
    peak_one_users = 60
    peak_two_users = 40
    time_limit = 180

    def tick(self):
        run_time = round(self.get_run_time())

        if run_time < self.time_limit:
            user_count = (
                (self.peak_one_users - self.min_users)
                * math.e ** -(((run_time / (self.time_limit / 10 * 2 / 3)) - 5) ** 2)
                + (self.peak_two_users - self.min_users)
                * math.e ** -(((run_time / (self.time_limit / 10 * 2 / 3)) - 10) ** 2)
                + self.min_users
            )
            return (round(user_count), round(user_count))
        else:
            return None