import matplotlib.pyplot as plt
import pandas as pd

# Données expérimentales
data = {
    "Service": ["Recherche", "Vidéo", "Admin", "Backup", "IoT"],
    "Debit": [50, 30, 10, 5, 1],
    "Latence_IPv4": [5, 8, 12, 25, 30],
    "Latence_IPv6": [6, 9, 13, 27, 32]
}

df = pd.DataFrame(data)

# Graphique débit
plt.figure()
plt.bar(df["Service"], df["Debit"])
plt.title("Débit par type de trafic")
plt.xlabel("Type de trafic")
plt.ylabel("Débit (Mbps)")
plt.savefig("debit_trafic.png")

# Graphique latence
plt.figure()
plt.plot(df["Service"], df["Latence_IPv4"], marker='o', label="IPv4")
plt.plot(df["Service"], df["Latence_IPv6"], marker='s', label="IPv6")
plt.title("Comparaison latence IPv4 vs IPv6")
plt.xlabel("Type de trafic")
plt.ylabel("Latence (ms)")
plt.legend()
plt.savefig("latence_ipv4_ipv6.png")

plt.show()
