import time
from locust import HttpUser, task, constant

class LoadTest(HttpUser):
    wait_time = constant(0)
    host = "http://api-server:80"

    @task
    def hello_world(self):
        self.client.get("/hello_world")

    @task(3)
    def view_items(self):
        for item_id in range(10):
            self.client.get(f"/item?item_id={item_id}", name="/item")

    def on_start(self):
        # NOTE: api-serverが起動するのを待ってから実施したいので5s待ってる
        time.sleep(5)
        self.client.post("/login", json={"username":"foo", "password":"bar"})
