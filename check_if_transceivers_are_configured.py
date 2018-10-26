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
        print("Conducting configured interface audit of device {hostname}".format(hostname=hostname))
        with Device(host=hostname, user=username, passwd=password) as dev:

            config_interfaces = InterfaceTable(dev).get()
            eths = EthPortTable(dev).get()
            for eth in eths:
                if not any(eth.name == interface.name for interface in config_interfaces):
                    print("{eth} is not configured".format(eth=eth.name))
        print("Finished configured interface audit of device {hostname}".format(hostname=hostname))
    except ConnectError as err:
        print ("Cannot connect to device: {0}".format(err))
        sys.exit(1)
    except Exception as err:
        print (err)
        sys.exit(1)

if __name__ == "__main__":
    main()
