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
                if(not eth.name in config_interfaces.keys() or (not config_interfaces[eth.name].unit
                    and not config_interfaces[eth.name].etherlag and not config_interfaces[eth.name].gigetherlag)):
                    print("Interface: {}\nSpeed: {}\nOper-status: {}\nAdmin-status: {}\n"\
                          "Description: {}\nLink-mode: {}\nMedia-type: {}\nInt-type: {}\n"\
                          "Mac Addr: {}\n".format(eth.name, eth.speed, eth.oper, eth.admin,
                                                  eth.description, eth.link_mode, eth.media_type,
                                                  eth.int_type, eth.macaddr))
                elif(eth.name in config_interfaces.keys() and config_interfaces[eth.name].unit and
                     config_interfaces[eth.name].phy_disable and config_interfaces[eth.name].unit_disable
                     and config_interfaces[eth.name].vlan == 'badvlan'):
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