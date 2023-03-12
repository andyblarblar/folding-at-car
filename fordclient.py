import requests
from structs import VehicleStatus


class FordClient():

    def __init__(self, Id):
        self.url = url = "https://fcon-simulatedvehicle.apps.pd01e.edc1.cf.ford.com/api/fordconnect/v2/vehicles/"
        self.Token = Token = "eyJhbGciOiJSUzI1NiIsImtpZCI6ImtleS0xIiwidHlwIjoiSldUIn0iwidHlwIjoiSldUIn0iwidHlwIjoiSldUIn0iwidHlwIjoiSldg.eyJhenAiOiJBWlAiLCJtdG1JZCI6Im10bUlkIiwic2NwIjoic2NwIiwidXNlckd1aWQiOiJlbmNvZGVkLWd1aWQtdmFsdWUuLiJ9eyJhenAiOiJBWlAiLCJtdG1JZCI6Im10bUlkIiwic2NwIjoic2NwIiwidXNlckd1aWQiOiJlbmNvZGVkLWd1aWQtdmFsdWUuLiJ9eyJhenAiOiJBWlAiLCJtdG1JZCI6Im10bUlkIiwic2NwIjoic2NwIiwidXNlckd1aWQiOiJlbmNvZGVkLWd1aWQtdmFsdWUuLiJ9eyJhenAiOiJBWlAiLCJtdG1JZCI6Im10bUlkIiwic2NwIjoic2NwIiwidXNlckd1aWQiOiJlbmNvZGVkLWd1aWQtdmFsdWUuLiJ9eyJhenAiOiJBWlAiLCJtdG1JZCI6Im10bUlkIiwic2NwIjoic2NwIiwidXNlckd1aWQiOiJlbmNvZGVkLWd1aWQtdmFsdWUuLiJ9eyJhenAiOiJBWlAiLCJtdG1JZCI6Im10bUlkIiwic2NwIjoic2NwIiwidXNlckd1aWQiOiJlbmNvZGVkLWd1aWQtdmFsdWUuLiJ9eyJhenAiOiJBWlAiLCJtdG1JZCI6Im10bUlkIiwic2NwIjoic2NwIiwidXNlckd1aWQiOiJlbmNvZGVkLWd1aWQtdmFsdWUuLiJ9.mSHjHPoduQ2UG4mv5jMj9LeVdbmCG7lTYvzFeUKDUgaArdBFwH2gvjPELgUYU1_Hmx90yS3A3YykGDqEI-c1v0d717wLQzhce8q_G5cqIgLKiIMUZgjyOsSCxIVP0OiaizrBNW9MtVdpOJJksry3Le1jv--Bf_MKGg9LDpGWs8HqO9YxLmmKqMLmHbXq3ukR8fHelyeNAJyOTiWGTq4lWm5ErNGpfWwZcTbds11dwAZjjcfd35wpOYkcg4LFANqr8XapvgN3EilBoWfVrajOz6ac8bf5z6t2F1lpIcVKMDQH4rzVSfsWBLkuvvhQBvZMQZDPz9yVKU9Zetd-AhHn9n"
        self.AppID = AppID = "afdc085b-377a-4351-b23e-5e1d35fb3700"
        self.Id = Id

    def getVehicle(self, Id):
        r = requests.get(url=self.url + self.Id, headers={
                         'Authorization': 'Bearer ' + self.Token, 'Application-Id': self.AppID, 'Accept': 'application/json', 'Content-Type': 'application/json'})
        
        print("\n")
        print("modelName", r.json().get("vehicle").get("modelName"))
        print("Id", r.json().get("vehicle").get("vehicleId"))
        print("Plug", r.json().get("vehicle").get("vehicleStatus").get("plugStatus").get("value"))
        print("Batt", r.json().get("vehicle").get("vehicleDetails").get("batteryChargeLevel").get("value"))
        print("Long", r.json().get("vehicle").get("vehicleLocation").get("longitude"))
        print("Lat:", r.json().get("vehicle").get("vehicleLocation").get("latitude"))

        print("\n")

        modelName = r.json().get("vehicle").get("modelName")
        Id = r.json().get("vehicle").get("vehicleId")
        Plug = bool(r.json().get("vehicle").get("vehicleStatus").get("plugStatus").get("value"))
        Batt = float(r.json().get("vehicle").get("vehicleDetails").get("batteryChargeLevel").get("value"))
        Long = float(r.json().get("vehicle").get("vehicleLocation").get("longitude"))
        Lat = float(r.json().get("vehicle").get("vehicleLocation").get("latitude"))

        return modelName, Id, Plug, Batt, Long, Lat



Id = "8a7fe1eb86cea8750186d23fc39a0013"

v1 = FordClient(Id)
v1.getVehicle(Id)