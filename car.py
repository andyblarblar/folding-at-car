from fordclient import FordClient
from backendClient import BackendClient
import subprocess
import time


def is_in_range(lat: float, lon: float) -> bool:
    """
    Returns true if we are in the correct area to fold.
    """
    return True  # TODO make this function


if __name__ == "__main__":
    clients = [FordClient("8a73d4e286cd6daf0186cd6eac160000"), FordClient("8a73d4e286cd6daf0186cd6f30230001")]
    is_runnings = [False, False]

    backend_client = BackendClient()

    print("init...")

    while 1:
        print("Polling....", flush=True)

        for (i, (client, is_running)) in enumerate(zip(clients, is_runnings), start=0):
            vs = client.getVehicle()

            if not is_running and is_in_range(vs.lat, vs.long) and vs.plug:
                print(f"Starting folding on {vs.id}", flush=True)
                subprocess.call(["/bin/bash", "/start-fah.bash"])
                is_runnings[i] = True
                backend_client.post(vs.id, vs.batt, vs.modelName)

            elif is_running and (not is_in_range(vs.lat, vs.long) or not vs.plug):
                print(f"Stopping folding on {vs.id}", flush=True)
                subprocess.call(["/bin/bash", "/stop-fah.bash"])
                is_runnings[i] = False
                backend_client.delete(vs.id)
        time.sleep(1)
