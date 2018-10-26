import re
import sys
from jnpr.junos import Device
from jnpr.junos.exception import ConnectError
from myTables.ConfigTables import InterfaceTable
from myTables.OpTables import EthPortTable


def main():
    hostname = sys.argv[1]
    username = sys.argv[2]
    password = sys.argv[3]
    try:
        print("\nConducting configured interface audit of device {hostname}\n".format(hostname=hostname))
        with Device(host=hostname, user=username, passwd=password) as dev:
            config_interfaces = InterfaceTable(dev).get()
            eths = EthPortTable(dev).get()
            print("################UNCONFIGURED INTERFACES################")
            for eth in eths:
                if (not eth.name in config_interfaces.keys() or not config_interfaces[eth.name].unit):
                    print("Interface: {}\nSpeed: {}\nOper-status: {}\nAdmin-status: {}\n"\
                          "Description: {}\nLink-mode: {}\nMedia-type: {}\nInt-type: {}\n"\
                          "Mac Addr: {}\n".format(eth.name, eth.speed, eth.oper, eth.admin,
                                                  eth.description, eth.link_mode, eth.media_type,
                                                  eth.int_type, eth.macaddr))
        print("##########################END##########################")
        print("Finished configured interface audit of device {hostname}".format(hostname=hostname))
    except ConnectError as err:
        print ("Cannot connect to device: {0}".format(err))
        sys.exit(1)
    except Exception as err:
        print (err)
        sys.exit(1)

if __name__ == "__main__":
    main()
