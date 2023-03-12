from .fordclient import FordClient
from .structs import Location
import subprocess
import time

if __name__== "fordclient":
    isRunningFold = False
    mylist = {"8a73d4e286cd6daf0186cd6eac160000", "8a73d4e286cd6daf0186cd6f30230001" }

    while(1):
        for i in mylist:
           if (FordClient(mylist[i]).getVehicle()[4] == -83.2100190  and FordClient(mylist[i]).getVehicle()[5]==42.3153565 and FordClient(mylist[i]).getVehicle()[2] ):
               subprocess.run("/bin/bash","star-fah.bash")
               isRunningFold = True
           elif (isRunningFold and not(FordClient(mylist[i]).getVehicle()[4] == -83.2100190  and FordClient(mylist[i]).getVehicle()[5]==42.3153565 and FordClient(mylist[i]).getVehicle()[2])) :
                subprocess.run("/bin/bash","stop-fah.bash")


        time.sleep(1)
    


