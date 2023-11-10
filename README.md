# burbles-by-peluqqi

### Changes

> 11/05/2023 Module 1: Linux Privilege Escalation
>
> * Environment enumeration
> * Internals enumeration
> * Services enumeration
> * Credential hunting
>
> 11/10/2023 Windows executable
>
> * Situational awareness
> * Initial enumeration
> * Communication with processes
> * Exploitable permissions

## Cheatsheet

### Linux Privilege Escalation

* [ ] Environment enumeration

  ```bash
  > whoami
  > id
  > hostname
  > ip a
  > sudo -l
  > cat /etc/os-release
  > echo $PATH
  > env
  > uname -a
  > # lscpu
  > cat /etc/shells
  > # cat /etc/fstab | grep -v \"#\" | column -t
  > # route
  > # arp -a
  > cat /etc/passwd
  > cat /etc/shadow
  > cat /etc/group
  > ls /home
  > df -h # Mounted fs
  > find / -type d -name ".*" -ls 2>/dev/null
  > ls -l /tmp /var/tmp /dev/sh
  > ls /var/www/html
  ```
* [ ] Internals enumeration

  ```bash
  > ip a
  > cat /etc/hosts
  > lastlog
  > w
  > history
  > find / -type f \( -name *_hist -o -name *_history \) -exec ls -l {} \; 2>/dev/null
  > ls -R -la /etc/cron*
  > # find /proc -name cmdline -exec cat {} \; 2>/dev/null | tr " " "\n""
  ```
* [ ] Services enumeration

  ```bash
  > apt list --installed | tr "/" " " | cut -d" " -f1,3 | sed 's/[0-9]://g'
  > sudo -V | head -n 1
  > # ls -l /bin /usr/bin/ /usr/sbin/
  > find / -type f \( -name *.conf -o -name *.config \) -exec ls -l {} \; 2>/dev/null
  > find / -type f -name "*.sh" 2>/dev/null | grep -v "src\|snap\|share"
  > ps aux | grep root
  > ss -tulpn" # List tcp/udp listening sockets
  ```
* [ ] Credential hunting

  ```bash
  > ls /var/www/html
  > ls ~/.ssh
  > find / -type f -name *.ssh -exec ls -l {} \; 2>/dev/null
  > find / -type f -name *.bak -exec ls -l {} \; 2>/dev/null
  ```

### Windows Privilege Escalation

* [ ] Situational awareness

  ```bash
  First of all, check 'Program Files' folders
  > ipconfig /all # Interface(s), IP Address(es), DNS Information
  > arp -a
  > route print
  > Get-MpComputerStatus # Windows Defender status
  > Get-AppLockerPolicy -Effective | select -ExpandProperty RuleCollections # AppLocker rules
  > Get-AppLockerPolicy -Local | Test-AppLockerPolicy -path C:\Windows\System32\cmd.exe -User Everyone # Test AppLocker policy
  ```
* [ ] Initial enumeration

  ```bash
  > tasklist /svc
  > set
  > systeminfo
  > wmic qfe # Patches and Updates
  > Get-HotFix | ft -AutoSize # PS Patches and Updates
  > wmic product get name # Installed programs
  > Get-WmiObject -Class Win32_Product |  select Name, Version # PS Installed programs
  > netstat -ano # Display running processes
  > query user # Logged-In users
  > echo %USERNAME% # Current user
  > whoami /priv # Privileges
  > whoami /groups
  > net user # Get all users
  > net localgroup # Get all groups
  > net localgroup administrators # Get group detail
  > net accounts # Get password policy and other account information
  ```
* [ ] Communication with processes

  ```bash
  > netstat -ano
  > pipelist.exe /accepteula # List named pipes with pipelist app
  > gci \\.\pipe\ # PS List named pipes
  > accesschk.exe /accepteula \\.\Pipe\lsass -v # Review LSASS named pipes permissions
  > accesschk.exe -accepteula -w \pipe\<service> -v # Check service named pipe permissions
  ```
* [ ] Exploitable permissions

  > Note: Based on the server's settings, it might be required to spawn an
  > elevated CMD prompt to bypass UAC and have this privilege.

  ```bash
  User privileges:
    > SeImpersonate and SeAssignPrimaryToken
    > SeDebugPrivilege
    > SeTakeOwnershipPrivilege

  Group privileges:
    > SeBackupPrivilege
  ```
