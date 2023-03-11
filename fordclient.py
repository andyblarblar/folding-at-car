import requests

class FordClient():

    def __init__(self, Id):
        self.url = url = "https://fcon-simulatedvehicle.apps.pd01e.edc1.cf.ford.com"
        self.Token = Token = "eyJhbGciOiJSUzI1NiIsImtpZCI6ImtleS0xIiwidHlwIjoiSldUIn0iwidHlwIjoiSldUIn0iwidHlwIjoiSldUIn0iwidHlwIjoiSldg.eyJhenAiOiJBWlAiLCJtdG1JZCI6Im10bUlkIiwic2NwIjoic2NwIiwidXNlckd1aWQiOiJlbmNvZGVkLWd1aWQtdmFsdWUuLiJ9eyJhenAiOiJBWlAiLCJtdG1JZCI6Im10bUlkIiwic2NwIjoic2NwIiwidXNlckd1aWQiOiJlbmNvZGVkLWd1aWQtdmFsdWUuLiJ9eyJhenAiOiJBWlAiLCJtdG1JZCI6Im10bUlkIiwic2NwIjoic2NwIiwidXNlckd1aWQiOiJlbmNvZGVkLWd1aWQtdmFsdWUuLiJ9eyJhenAiOiJBWlAiLCJtdG1JZCI6Im10bUlkIiwic2NwIjoic2NwIiwidXNlckd1aWQiOiJlbmNvZGVkLWd1aWQtdmFsdWUuLiJ9eyJhenAiOiJBWlAiLCJtdG1JZCI6Im10bUlkIiwic2NwIjoic2NwIiwidXNlckd1aWQiOiJlbmNvZGVkLWd1aWQtdmFsdWUuLiJ9eyJhenAiOiJBWlAiLCJtdG1JZCI6Im10bUlkIiwic2NwIjoic2NwIiwidXNlckd1aWQiOiJlbmNvZGVkLWd1aWQtdmFsdWUuLiJ9eyJhenAiOiJBWlAiLCJtdG1JZCI6Im10bUlkIiwic2NwIjoic2NwIiwidXNlckd1aWQiOiJlbmNvZGVkLWd1aWQtdmFsdWUuLiJ9.mSHjHPoduQ2UG4mv5jMj9LeVdbmCG7lTYvzFeUKDUgaArdBFwH2gvjPELgUYU1_Hmx90yS3A3YykGDqEI-c1v0d717wLQzhce8q_G5cqIgLKiIMUZgjyOsSCxIVP0OiaizrBNW9MtVdpOJJksry3Le1jv--Bf_MKGg9LDpGWs8HqO9YxLmmKqMLmHbXq3ukR8fHelyeNAJyOTiWGTq4lWm5ErNGpfWwZcTbds11dwAZjjcfd35wpOYkcg4LFANqr8XapvgN3EilBoWfVrajOz6ac8bf5z6t2F1lpIcVKMDQH4rzVSfsWBLkuvvhQBvZMQZDPz9yVKU9Zetd-AhHn9n"
        self.AppID = AppID = "afdc085b-377a-4351-b23e-5e1d35fb3700"
        self.Id = Id
        

    def getVehicleId(self):
        r = requests.get(url=self.url + "/api/fordconnect/v2/vehicles", headers={
                         'Authorization': 'Bearer ' + self.Token, 'Application-Id': self.AppID, 'Accept': 'application/json', 'Content-Type': 'application/json'})
        for i in range(len(r.json().get("vehicles"))):
            print(i,"VehicleId", r.json().get("vehicles")[i].get("vehicleId"))


    def getBattery(self, Id):
        r = requests.get(url=self.url + "/api/fordconnect/v2/vehicles", headers={
                         'Authorization': 'Bearer ' + self.Token, 'Application-Id': self.AppID, 'Accept': 'application/json', 'Content-Type': 'application/json'})
        print(r)