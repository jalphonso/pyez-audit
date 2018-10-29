# Summary
Used to peform audit of configuration specifically to ensure all recognized interfaces are configured.\
*PyEZ is the library used here to perform the work.*

# Details
Using a custom operational table for Ethernet Ports the command "show interfaces media "\[fgxe]\[et]\*" terse" is retrieved and then checked to see if each interface is in the config using a custom config table for Interfaces. The custom ethport table closely mirrors the built in one but excludes ae interfaces from the regex. Also ensured that each interface in the config has a logical unit configured.

### Sample Output

```
jalphonso-mbp:pyez-audit jalphonso$ ansible-playbook -i hosts interface_audit.pb.yml
Enter username: testuser1
Enter password:
confirm Enter password:

PLAY [all] ******************************************************************************************************************************************

TASK [interface_audit] *********************************************************************************************************
ok: [qfx5100-2]
ok: [qfx5100-1]

TASK [debug] ****************************************************************************************************************************************
ok: [qfx5100-1] => {
    "python_output.stdout_lines": [
        "",
        "Conducting configured interface audit of device 192.168.0.15",
        "",
        "################UNCONFIGURED INTERFACES################",
        "Interface: xe-0/0/20",
        "Speed: Auto",
        "Oper-status: down",
        "Admin-status: up",
        "Description: None",
        "Link-mode: Auto",
        "Media-type: Copper",
        "Int-type: Ethernet",
        "Mac Addr: 44:f4:77:6c:53:d7",
        "",
        "Interface: xe-0/0/43",
        "Speed: Auto",
        "Oper-status: down",
        "Admin-status: up",
        "Description: None",
        "Link-mode: Auto",
        "Media-type: Copper",
        "Int-type: Ethernet",
        "Mac Addr: 44:f4:77:6c:53:ee",
        "",
        "##########################END##########################",
        "Finished configured interface audit of device 192.168.0.15"
    ]
}
ok: [qfx5100-2] => {
    "python_output.stdout_lines": [
        "",
        "Conducting configured interface audit of device 192.168.0.16",
        "",
        "################UNCONFIGURED INTERFACES################",
        "Interface: et-0/0/48",
        "Speed: 40Gbps",
        "Oper-status: down",
        "Admin-status: up",
        "Description: None",
        "Link-mode: None",
        "Media-type: Fiber",
        "Int-type: Ethernet",
        "Mac Addr: 54:4b:8c:e9:6d:b3",
        "",
        "Interface: xe-0/0/50:2",
        "Speed: 10Gbps",
        "Oper-status: down",
        "Admin-status: up",
        "Description: None",
        "Link-mode: None",
        "Media-type: Fiber",
        "Int-type: Ethernet",
        "Mac Addr: 54:4b:8c:e9:6d:bd",
        "",
        "Interface: xe-0/0/50:3",
        "Speed: 10Gbps",
        "Oper-status: down",
        "Admin-status: up",
        "Description: testing123",
        "Link-mode: None",
        "Media-type: Fiber",
        "Int-type: Ethernet",
        "Mac Addr: 54:4b:8c:e9:6d:be",
        "",
        "##########################END##########################",
        "Finished configured interface audit of device 192.168.0.16"
    ]
}

PLAY RECAP ******************************************************************************************************************************************
qfx5100-1                  : ok=2    changed=1    unreachable=0    failed=0
qfx5100-2                  : ok=2    changed=1    unreachable=0    failed=0
```
