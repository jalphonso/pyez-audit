import re
import sys
from jnpr.junos import Device
from jnpr.junos.exception import ConnectError
from jnpr.junos.op.xcvr import XcvrTable
from myTables.ConfigTables import InterfaceTable


def main():
    hostname = sys.argv[1]
    username = sys.argv[2]
    password = sys.argv[3]
    try:
        print("Conducting configured interface audit of device {hostname}".format(hostname=hostname))
        with Device(host=hostname, user=username, passwd=password) as dev:

            config_interfaces = InterfaceTable(dev).get()
            xcvrs = XcvrTable(dev).get()
            for xcvr in xcvrs:
                xcvr_fpc = xcvr.name[0].split()[1]
                xcvr_pic = xcvr.name[1].split()[1]
                xcvr_port = xcvr.name[2].split()[1]
                xcvr_name = xcvr_fpc + "/" + xcvr_pic + "/" + xcvr_port
                xcvr_regex = xcvr_name + "($|:[\d])"
                xcvr_compiled_regex = re.compile(xcvr_regex)
                if not any(xcvr_compiled_regex.search(interface.name) for interface in config_interfaces):
                    print("Xcvr {xcvr} is not configured".format(xcvr=xcvr_name))
        print("Finished configured interface audit of device {hostname}".format(hostname=hostname))
    except ConnectError as err:
        print ("Cannot connect to device: {0}".format(err))
        sys.exit(1)
    except Exception as err:
        print (err)
        sys.exit(1)

if __name__ == "__main__":
    main()
