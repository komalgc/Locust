from locust import HttpUser, task, between

class MyUser(HttpUser):
    host = "https://example.com:1160"

    # You can set the wait time between tasks if needed
    wait_time = between(5, 9)

    # Define a function to get the bearer token
    def get_token(self):
        # Replace 'your_token_here' with your actual bearer token
        return 'eyJ'

    # Decorate the task with the @task decorator
    @task
    def getAPIrequest(self):
    
        headers = {
            'Authorization': f'Bearer {self.get_token()}'
        }

        # Define the endpoint URL
        endpoint = "/endpoint/"
        
        # Make the GET request with the specified headers
        response = self.client.get(endpoint, headers=headers)

        # Print the response status code and content if needed
        print(f"Response Status Code: {response.status_code}")
        # print(response.text)  # Uncomment to print response content

