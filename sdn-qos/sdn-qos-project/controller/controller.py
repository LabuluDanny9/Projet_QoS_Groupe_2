import requests

ONOS = "http://localhost:8181/onos/v1"
AUTH = ("onos", "rocks")

def get_hosts():
    r = requests.get(f"{ONOS}/hosts", auth=AUTH)
    print(r.json())

def get_devices():
    r = requests.get(f"{ONOS}/devices", auth=AUTH)
    print(r.json())

if __name__ == "__main__":
    print("Devices:")
    get_devices()
    print("Hosts:")
    get_hosts()
