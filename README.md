# Summary
Used to peform audit of configuration specifically to ensure all transceivers are configured.\
*PyEZ is the library used here to peform the work.*

# Details
The "show chassis hardware" representative table in PyEZ (jnpr.junos.op.xcvr import XcvrTable)
is retrieved and then checked to see if each transceiver is in the config using a custom Interface Config Table.

### Sample Output

```
ansible-playbook -i hosts check_if_transceivers_are_configured.pb.yml
Enter username: Lab
Enter password:
confirm Enter password:

PLAY [all] ****************************************************************************************************************************************************************************************************************************************

TASK [check_if_transceivers_are_configured] ********************************************************************************************************************************************************************************************************
changed: [mx240-1]
changed: [qfx5100-1]
changed: [qfx5100-2]

TASK [debug] **************************************************************************************************************************************************************************************************************************************
ok: [qfx5100-1] => {
    "python_output.stdout_lines": [
        "Conducting configured interface audit of device 192.168.253.15",
        "Finished configured interface audit of device 192.168.253.15"
    ]
}
ok: [qfx5100-2] => {
    "python_output.stdout_lines": [
        "Conducting configured interface audit of device 192.168.253.16",
        "Xcvr 0/0/50 is not configured",
        "Finished configured interface audit of device 192.168.253.16"
    ]
}
ok: [mx240-1] => {
    "python_output.stdout_lines": [
        "Conducting configured interface audit of device 192.168.253.23",
        "Xcvr 2/0/3 is not configured",
        "Xcvr 2/0/5 is not configured",
        "Xcvr 2/0/7 is not configured",
        "Finished configured interface audit of device 192.168.253.23"
    ]
}

PLAY RECAP ****************************************************************************************************************************************************************************************************************************************
mx240-1                    : ok=2    changed=1    unreachable=0    failed=0
qfx5100-1                  : ok=2    changed=1    unreachable=0    failed=0
qfx5100-2                  : ok=2    changed=1    unreachable=0    failed=0
```
