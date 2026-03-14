#!/bin/bash
sudo mn -c
sudo mn --custom topology/topo.py --topo federation \
--switch ovs,protocols=OpenFlow13 \
--controller remote,ip=127.0.0.1,port=6653
