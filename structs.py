class VehicleStatus:
    def __init__(self, model_name: str, identifier: str, plug: bool, batt: float, long: float, lat: float):
        self.modelName = model_name
        self.id = identifier
        self.plug = plug
        self.batt = batt
        self.long = long
        self.lat = lat
