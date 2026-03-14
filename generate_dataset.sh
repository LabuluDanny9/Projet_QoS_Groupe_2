h2 iperf3 -s &
h1 iperf3 -c 10.0.0.2 -b 50M -J > dataset/research.json
h1 iperf3 -c 10.0.0.2 -b 30M -J > dataset/video.json
h1 ping -c 20 10.0.0.2 > dataset/latency.txt
