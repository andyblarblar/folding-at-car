# Backend API

Contains a list of all currently charging compute nodes.

## Structure
- Vehicle
  - vid: String
  - charging_status: Float
  - model: String

## Endpoints

### /vehicle/{VID}
- Get - Returns an individual vehicles state if avail. Retruns HTTP not avial otherwise
- Post (body Vehicle) - Sets the vehicles state, or updates it if it exists
- Delete - Removes vehicle, to be called when car stops computing

### /vehicles
- Get - Returns a list of Vehicle structs (this is all currently computing vehicles)