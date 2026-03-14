from mininet.topo import Topo

class FederationTopo(Topo):

    def build(self):

        # Hosts
        h_unikin = self.addHost('h_unikin')
        h_unilu = self.addHost('h_unilu')
        h_ucb = self.addHost('h_ucb')

        # Switches universités
        sw_unikin = self.addSwitch('sw_unikin', dpid='0000000000000001')
        sw_unilu = self.addSwitch('sw_unilu', dpid='0000000000000002')
        sw_ucb = self.addSwitch('sw_ucb', dpid='0000000000000003')

        # Switches core
        sw_core1 = self.addSwitch('sw_core1', dpid='0000000000000004')
        sw_core2 = self.addSwitch('sw_core2', dpid='0000000000000005')
        sw_core3 = self.addSwitch('sw_core3', dpid='0000000000000006')

        # Connexions hosts
        self.addLink(h_unikin, sw_unikin)
        self.addLink(h_unilu, sw_unilu)
        self.addLink(h_ucb, sw_ucb)

        # Connexions universités vers core
        self.addLink(sw_unikin, sw_core1)
        self.addLink(sw_unilu, sw_core1)
        self.addLink(sw_ucb, sw_core3)

        # Backbone
        self.addLink(sw_core1, sw_core2)
        self.addLink(sw_core2, sw_core3)

topos = {'federation': FederationTopo}
