from mininet.topo import Topo
from mininet.link import TCLink

class FederationTopo(Topo):
    def build(self):

        # ===== Switches =====
        s0 = self.addSwitch('s0')
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')

        # ===== Hosts =====
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')

        # ===== Core links (20 Mbps) =====
        self.addLink(s0, s1, cls=TCLink, bw=20)
        self.addLink(s0, s2, cls=TCLink, bw=20)
        self.addLink(s0, s3, cls=TCLink, bw=20)

        # ===== Host links (20 Mbps) =====
        self.addLink(h1, s1, cls=TCLink, bw=20)
        self.addLink(h2, s2, cls=TCLink, bw=20)
        self.addLink(h3, s3, cls=TCLink, bw=20)

topos = {'federation': FederationTopo}
