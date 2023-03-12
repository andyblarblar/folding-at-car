import requests



class backendClient:

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
            print("Data posted successfully.")
        else:
            print(f"Error: {response.status_code}")

    def delete(self, vid, charging_status, model):
        data = {
            "vid": vid,
            "charging_status": charging_status,
            "model": model
        }

        response = requests.delete(self.url, json=data)

        if response.status_code == 202 or response.status_code == 201 or response.status_code == 200:
            print("Data deleted successfully.")
        else:
            print(f"Error: {response.status_code}")


v1 = backendClient()
v1.delete("125", 0.23, "F150")