from locust import HttpLocust, TaskSet, task
import json


class UserBehavior(TaskSet):
    # runs one time for each user
    def on_start(self):
        self.client.get("")

    @task(2)  # chance to run 2/3
    def room(self):
        self.client.get("room/1")

    @task(3)
    def create_room(self):
        self.client.post("create", data=json.dumps({
            "id": 7,
	        "number": 8,
	        "price": 5000,
	        "description": "Suite"
        }),
            name="Create a new room")

    @task(4)
    def update_room(self):
        self.client.put("update/1", data=json.dumps({
            "id": 55,
	        "number": 10,
	        "price": 50000,
            "description": "Luxury"
        }),
            name="Update a room")

    @task(5)  # chance to run 2/3
    def delete(self):
        self.client.delete('delete/2')


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(1, 2)
