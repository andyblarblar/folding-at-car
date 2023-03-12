import requests


class BackendClient:

    def __init__(self):
        self.url = "http://localhost/vehicle"

    def post(self, vid, charging_status, model):
        data = {
            "vid": vid,
            "charging_status": charging_status,
            "model": model
        }
        response = requests.post(self.url, json=data)

        if response.status_code == 202 or response.status_code == 201:
            print("Backend posted successfully.")
        else:
            print(f"Error: {response.status_code}")

    def delete(self, vid):
        data = {
            "vid": vid,
            "charging_status": 0.0,
            "model": "dead"
        }

        response = requests.delete(self.url, json=data)

        if response.status_code == 202 or response.status_code == 201 or response.status_code == 200:
            print("Backend deleted successfully.")
        else:
            print(f"Error: {response.status_code}")
