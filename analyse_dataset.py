import json
import matplotlib.pyplot as plt

files = {
    "Recherche": "dataset/research.json",
    "Vidéo": "dataset/video.json",
    "Admin": "dataset/admin.json",
    "Backup": "dataset/backup.json"
}

services = []
debits = []

for service, file in files.items():
    with open(file) as f:
        data = json.load(f)
        bps = data["end"]["sum_received"]["bits_per_second"]
        mbps = bps / 1000000
        services.append(service)
        debits.append(mbps)

plt.figure()
plt.bar(services, debits)
plt.title("Débit mesuré par type de trafic (données réelles)")
plt.xlabel("Service")
plt.ylabel("Débit (Mbps)")
plt.savefig("graph_debit_dataset.png")

plt.show()
