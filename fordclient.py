import requests
from structs import VehicleStatus


class FordClient:

    def __init__(self, identifier):
        self.url = url = "https://fcon-simulatedvehicle.apps.pd01e.edc1.cf.ford.com/api/fordconnect/v2/vehicles/"
        self.Token = Token = "eyJhbGciOiJSUzI1NiIsImtpZCI6ImtleS0xIiwidHlwIjoiSldUIn0iwidHlwIjoiSldUIn0iwidHlwIjoiSldUIn0iwidHlwIjoiSldg.eyJhenAiOiJBWlAiLCJtdG1JZCI6Im10bUlkIiwic2NwIjoic2NwIiwidXNlckd1aWQiOiJlbmNvZGVkLWd1aWQtdmFsdWUuLiJ9eyJhenAiOiJBWlAiLCJtdG1JZCI6Im10bUlkIiwic2NwIjoic2NwIiwidXNlckd1aWQiOiJlbmNvZGVkLWd1aWQtdmFsdWUuLiJ9eyJhenAiOiJBWlAiLCJtdG1JZCI6Im10bUlkIiwic2NwIjoic2NwIiwidXNlckd1aWQiOiJlbmNvZGVkLWd1aWQtdmFsdWUuLiJ9eyJhenAiOiJBWlAiLCJtdG1JZCI6Im10bUlkIiwic2NwIjoic2NwIiwidXNlckd1aWQiOiJlbmNvZGVkLWd1aWQtdmFsdWUuLiJ9eyJhenAiOiJBWlAiLCJtdG1JZCI6Im10bUlkIiwic2NwIjoic2NwIiwidXNlckd1aWQiOiJlbmNvZGVkLWd1aWQtdmFsdWUuLiJ9eyJhenAiOiJBWlAiLCJtdG1JZCI6Im10bUlkIiwic2NwIjoic2NwIiwidXNlckd1aWQiOiJlbmNvZGVkLWd1aWQtdmFsdWUuLiJ9eyJhenAiOiJBWlAiLCJtdG1JZCI6Im10bUlkIiwic2NwIjoic2NwIiwidXNlckd1aWQiOiJlbmNvZGVkLWd1aWQtdmFsdWUuLiJ9.mSHjHPoduQ2UG4mv5jMj9LeVdbmCG7lTYvzFeUKDUgaArdBFwH2gvjPELgUYU1_Hmx90yS3A3YykGDqEI-c1v0d717wLQzhce8q_G5cqIgLKiIMUZgjyOsSCxIVP0OiaizrBNW9MtVdpOJJksry3Le1jv--Bf_MKGg9LDpGWs8HqO9YxLmmKqMLmHbXq3ukR8fHelyeNAJyOTiWGTq4lWm5ErNGpfWwZcTbds11dwAZjjcfd35wpOYkcg4LFANqr8XapvgN3EilBoWfVrajOz6ac8bf5z6t2F1lpIcVKMDQH4rzVSfsWBLkuvvhQBvZMQZDPz9yVKU9Zetd-AhHn9n"
        self.AppID = AppID = "afdc085b-377a-4351-b23e-5e1d35fb3700"
        self.Id = identifier

    def getVehicle(self):
        r = requests.get(url=self.url + self.Id, headers={
            'Authorization': 'Bearer ' + self.Token, 'Application-Id': self.AppID, 'Accept': 'application/json',
            'Content-Type': 'application/json'})

        model_name = r.json().get("vehicle").get("modelName")
        identifier = r.json().get("vehicle").get("vehicleId")
        plug = bool(r.json().get("vehicle").get("vehicleStatus").get("plugStatus").get("value"))
        batt = float(r.json().get("vehicle").get("vehicleDetails").get("batteryChargeLevel").get("value"))
        long = float(r.json().get("vehicle").get("vehicleLocation").get("longitude"))
        lat = float(r.json().get("vehicle").get("vehicleLocation").get("latitude"))

        return VehicleStatus(model_name, identifier, plug, batt, long, lat)
