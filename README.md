# Summary
Used to peform audit of configuration specifically to ensure all recognized interfaces are configured.\
*PyEZ is the library used here to peform the work.*

# Details
Using a custom operational table for Ethernet Ports the command "show interfaces media "\[fgxe]\[et]\*" terse" is retrieved and then checked to see if each interface is in the config using a custom config table for Interfaces.

### Sample Output

```bash
ansible-playbook -i hosts check_if_transceivers_are_configured.pb.yml
Enter username: testuser
Enter password:
confirm Enter password:

PLAY [all] ******************************************************************************************************************

TASK [check_if_transceivers_are_configured] *********************************************************************************
ok: [mx240-1]
ok: [qfx5100-2]
ok: [qfx5100-1]

TASK [debug] ****************************************************************************************************************
ok: [qfx5100-1] => {
    "python_output.stdout_lines": [
        "Conducting configured interface audit of device 192.168.0.15",
        "xe-0/0/20 is not configured",
        "xe-0/0/43 is not configured",
        "Finished configured interface audit of device 192.168.0.15"
    ]
}
ok: [qfx5100-2] => {
    "python_output.stdout_lines": [
        "Conducting configured interface audit of device 192.168.0.16",
        "et-0/0/48 is not configured",
        "xe-0/0/50:2 is not configured",
        "Finished configured interface audit of device 192.168.0.16"
    ]
}
ok: [mx240-1] => {
    "python_output.stdout_lines": [
        "Conducting configured interface audit of device 192.168.0.23",
        "xe-2/0/0 is not configured",
        "xe-2/0/2 is not configured",
        "xe-2/0/3 is not configured",
        "xe-2/0/4 is not configured",
        "xe-2/0/5 is not configured",
        "xe-2/0/6 is not configured",
        "xe-2/0/7 is not configured",
        "xe-2/0/8 is not configured",
        "xe-2/0/9 is not configured",
        "xe-2/0/10 is not configured",
        "xe-2/0/11 is not configured",
        "xe-2/0/12 is not configured",
        "xe-2/0/13 is not configured",
        "xe-2/0/14 is not configured",
        "xe-2/0/15 is not configured",
        "xe-2/0/16 is not configured",
        "xe-2/0/17 is not configured",
        "xe-2/1/0 is not configured",
        "xe-2/1/2 is not configured",
        "xe-2/1/3 is not configured",
        "xe-2/1/4 is not configured",
        "xe-2/1/5 is not configured",
        "xe-2/1/6 is not configured",
        "xe-2/1/7 is not configured",
        "xe-2/1/8 is not configured",
        "xe-2/1/9 is not configured",
        "xe-2/1/10 is not configured",
        "xe-2/1/11 is not configured",
        "xe-2/1/12 is not configured",
        "xe-2/1/13 is not configured",
        "xe-2/1/14 is not configured",
        "xe-2/1/15 is not configured",
        "xe-2/1/16 is not configured",
        "xe-2/1/17 is not configured",
        "xe-2/1/18 is not configured",
        "Finished configured interface audit of device 192.168.0.23"
    ]
}

PLAY RECAP ******************************************************************************************************************
mx240-1                    : ok=2    changed=1    unreachable=0    failed=0
qfx5100-1                  : ok=2    changed=1    unreachable=0    failed=0
qfx5100-2                  : ok=2    changed=1    unreachable=0    failed=0
```
