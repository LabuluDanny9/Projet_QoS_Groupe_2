#!/bin/bash

echo "======================================"
echo " DEMO SDN QoS AVANCEE - FEDERATION RDC"
echo "======================================"

# 1. Démarrer ONOS
echo "[1] Démarrage du contrôleur ONOS..."
docker start onos >/dev/null 2>&1
sleep 5

# 2. Ouvrir l'interface ONOS
echo "[2] Ouverture de l'interface ONOS..."
xdg-open http://localhost:8181/onos/ui >/dev/null 2>&1 &
echo "Connecte-toi avec: onos / rocks"
sleep 3

# 3. Nettoyer Mininet
echo "[3] Nettoyage Mininet..."
sudo mn -c >/dev/null 2>&1
sleep 2

# 4. Lancer la topologie et exécuter les tests
echo "[4] Lancement topologie SDN + tests..."
sudo mn --custom federation_sdn.py \
--topo federation \
--controller remote,ip=127.0.0.1,port=6653 \
--switch ovsk,protocols=OpenFlow13 << 'EOF'

echo ">>> Vérification des noeuds"
nodes

echo ">>> Test de connectivité (animation dans ONOS)"
pingall

echo ">>> Configuration IPv6"
h1 ifconfig h1-eth0 inet6 add 2001:1::1/64
h2 ifconfig h2-eth0 inet6 add 2001:2::1/64
h3 ifconfig h3-eth0 inet6 add 2001:3::1/64

echo ">>> Test IPv6"
h1 ping6 -c 3 2001:2::1

echo ">>> Démarrage serveur iperf3"
h2 iperf3 -s &

sleep 2

echo ">>> Trafic normal (prioritaire)"
h1 iperf3 -c 10.0.0.2 -b 20M -t 5 &

sleep 2

echo ">>> Simulation congestion réseau"
h3 iperf3 -c 10.0.0.2 -b 80M -t 10 &

sleep 3

echo ">>> Observation latence sous congestion"
h1 ping -c 5 h2

sleep 2

echo ">>> Simulation panne de lien inter-universités"
link s2 s3 down
sleep 3
pingall

sleep 2

echo ">>> Rétablissement du lien"
link s2 s3 up
sleep 3
pingall

echo ">>> Fin de la démonstration"
EOF
