from fordclient import FordClient
import subprocess
import time


def is_in_range(lat: float, lon: float) -> bool:
    """
    Returns true if we are in the correct area to fold.
    """
    True #TODO make this function


if __name__ == "__main__":
    clients = [FordClient("8a73d4e286cd6daf0186cd6eac160000"), FordClient("8a73d4e286cd6daf0186cd6f30230001")]
    is_runnings = [False, False]

    print("init...")

    while 1:
        print("Polling....")

        for client, is_running in zip(clients, is_runnings):
            vs = client.getVehicle()

            if not is_running and is_in_range(vs.lat, vs.long) and vs.plug:
                print(f"Starting folding on {vs.id}")
                subprocess.run("/bin/bash", "star-fah.bash")
                is_running = True
                #TODO tell backend we exist
            elif is_running and (not is_in_range(vs.lat, vs.long) or not vs.plug):
                print(f"Stopping folding on {vs.id}")
                subprocess.run("/bin/bash", "stop-fah.bash")
                is_running = False
                #TODO delete from backend
        time.sleep(1)
