import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def hello_world(self):
        self.client.get("")

    @task
    def check_url_get(self):
        self.client.get("/data/%22I%20like%20it%22%2C%20%22Wow%2C%20good%20job%21%22")
