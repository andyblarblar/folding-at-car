class VehicleStatus:
    def __init__(self, model_name, identifier, plug, batt, long: float, lat: float):
        self.modelName = model_name
        self.Id = identifier
        self.Plug = plug
        self.Batt = batt
        self.Long = long
        self.Lat = lat
