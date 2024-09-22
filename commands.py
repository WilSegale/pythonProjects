# List of diagnostic commands for mac
MacOs_diagnostic_commands = {
    "ping google.com -t 3",
    "traceroute google.com",
    "csrutil status",
    "sudo pfctl -s info",
    "system_profiler SPSoftwareDataType",
    "networksetup -listallnetworkservices",
    "networksetup -listallhardwareports",
    "df -h",
    "mount",
    "ps aux",
    "ps -ef | grep -v grep | awk '{print $2}'",
    "dscl . -list /Users",
    "cat /var/log/system.log",
    "nslookup google.com",
    "sudo pfctl -sa",
    "vm_stat",
    '''log show --predicate 'process == "ssh"' --info''',
    '''log show --predicate 'process == "sshd"' --info''',
    "last reboot"
}


# list of diagnostic commands for windows
Windows_diagnostic_commands = [
    "ping google.com -n 3",
    "ipconfig /all",
    "tracert google.com",
    "nslookup google.com",
    "sfc /scannow",
    "netstat -ano",
    "wmic qfe list",
    "robocopy source destination /E /COPYALL",
    "schtasks /query",
    "systeminfo",
    "cleanmgr",
    "resmon",
    "perfmon",
    "eventvwr.msc",
    "chkdsk",
    "DISM /Online /Cleanup-Image /RestoreHealth",
    "Reliability Monitor",
    "xperf",
    "Test-WsMan",
    "Test-NetConnection",
    "Get-EventLog",
    '''systeminfo | find "System Boot Time"''',
    '''net statistics workstation | find "Statistics since"'''
]