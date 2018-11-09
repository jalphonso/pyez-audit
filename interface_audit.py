import re
import sys
from jnpr.junos import Device
from jnpr.junos.exception import ConnectError
from myTables.ConfigTables import InterfaceTable
from myTables.OpTables import EthPortTable


def main():
    hostname = sys.argv[1]
    port = sys.argv[2]
    username = sys.argv[3]
    password = sys.argv[4]
    try:
        print("\nConducting configured interface audit of device {hostname}\n".format(hostname=hostname))
        with Device(host=hostname, port=port, user=username, passwd=password) as dev:
            config_interfaces = InterfaceTable(dev).get()
            eths = EthPortTable(dev).get()
            print("################UNCONFIGURED INTERFACES################")
            for eth in eths:
                interface = unit = ae = ae_config = None
                interface = config_interfaces[eth.name]
                if(interface):
                    unit = interface.unit
                    ae = interface.ae
                if(ae):
                    ae_config = config_interfaces[ae]
                if(not(interface and unit)):
                    if(ae_config and not ae_config.unit):
                        print("Interface: {} is part of {} bundle but {} is not configured with a unit".\
                              format(eth.name, ae, ae))
                    elif(ae_config):
                        continue
                    print("Interface: {}\nSpeed: {}\nOper-status: {}\nAdmin-status: {}\n"\
                          "Description: {}\nLink-mode: {}\nMedia-type: {}\nInt-type: {}\n"\
                          "Mac Addr: {}\n".format(eth.name, eth.speed, eth.oper, eth.admin,
                                                  eth.description, eth.link_mode, eth.media_type,
                                                  eth.int_type, eth.macaddr))
                elif(interface and interface.unit and interface.phy_disable and interface.unit_disable and interface.vlan == 'badvlan'):
                    print(eth.name + " was probably disabled by a script")
        print("##########################END##########################")
        print("Finished configured interface audit of device {hostname}".format(hostname=hostname))
    except ConnectError as err:
        print("Cannot connect to device: {0}".format(err))
        sys.exit(1)
    except Exception as err:
        print(err)
        sys.exit(1)

if __name__ == "__main__":
    main()
