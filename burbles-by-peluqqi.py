#!/usr/bin/env python3
import sys
import os
import time

class B_Colors:
    _DEFAULT = "\033[0;0m"
    _DARK_ORANGE = "\033[38;5;208m"
    _SOFT_ORANGE = "\033[38;5;180m"
    _DARK_BLUE = "\033[38;5;68m"
    _RED_WARNING = "\033[38;5;167m"
    _GREY = "\033[38;5;234m"

class Commands:
    _PRIVESC_ENVENUM = [
        "whoami",
        "id",
        "hostname",
        "ip a",
        "sudo -l",
        "cat /etc/os-release",
        "echo $PATH",
        "env",
        "uname -a",
        # "lscpu",
        "cat /etc/shells",
        # "cat /etc/fstab | grep -v \"#\" | column -t",
        # "route",
        # "arp -a",
        "cat /etc/passwd",
        "cat /etc/shadow",
        "cat /etc/group",
        "ls /home",
        "df -h", # Mounted fs
        "find / -type d -name \".*\" -ls 2>/dev/null",
        "ls -l /tmp /var/tmp /dev/shm",
        "ls -l /var/www/html",
        "ls -l /opt",
        "ls -l /srv"
    ]
    _PRIVESC_INTENUM = [
        "ip a",
        "find / -perm -4000 2>/dev/null", # Check binaries in GTFO Bins
        "cat /etc/hosts",
        "lastlog",
        "w",
        "history",
        "find / -type f \( -name *_hist -o -name *_history \) -exec ls -l {} \; 2>/dev/null",
        "ls -R -la /etc/cron*"
        #"find /proc -name cmdline -exec cat {} \; 2>/dev/null | tr \" \" \"\\n\""
    ]
    _PRIVESC_SERVENUM = [
        "apt list --installed | tr \"/\" \" \" | cut -d\" \" -f1,3 | sed 's/[0-9]://g'",
        "sudo -V | head -n 1",
        # "ls -l /bin /usr/bin/ /usr/sbin/"
        "find / -type f \( -name *.conf -o -name *.config \) -exec ls -l {} \; 2>/dev/null",
        "find / -type f -name \"*.sh\" 2>/dev/null | grep -v \"src\|snap\|share\"",
        "ps aux | grep root",
        "ss -tulpn" # List tcp/udp listening sockets
    ]
    _PRIVESC_CREDHUNTING = [
        "ls /var/www/html",
        "ls ~/.ssh",
        "find / -type f -name *.ssh -exec ls -l {} \; 2>/dev/null",
        "find / -type f -name *.bak -exec ls -l {} \; 2>/dev/null",
    ]

def color(str, code):
    return code + str + B_Colors._DEFAULT

def process_command(cmd):
    choice = input("\n" + color("[>] " + cmd, B_Colors._SOFT_ORANGE) + " ")

    if choice == "":
        os.system(cmd)

def print_banner():
    print("======================================================================================");
    print("|                          _                _     _                                  |");
    print("|                         | |              | |   | |                                 |");
    print("|                         | |__  _   _ _ __| |__ | | ___  ___                        |");
    print("|                         | '_ \| | | | '__| '_ \| |/ _ \/ __|                       |");
    print("|                         | |_) | |_| | |  | |_) | |  __/\__ \                       |");
    print("|                         |_.__/ \__,_|_|  |_.__/|_|\___||___/                       |");
    print("|                                                                                    |");
    print("|                                                 by peluqqi                         |");
    print("======================================================================================");

def main_menu():
    print("\nMain menu:");
    print("1) Linux Privilege Escalation");
    print("2) Exit");
    choice = input("\n[>] ");

    if choice == "1":
        lin_privesc_menu()
    elif choice == "2":
        sys.exit()
    else:
        main_menu()

def lin_privesc_menu():
    print("\nLinux Privilege Escalation:");
    print("1) Environment enumeration");
    print("2) Internals enumeration");
    print("3) Services enumeration");
    print("4) Credential hunting");
    print("5) Back to main menu");
    choice = input("\n[>] ");

    if choice == "1":
        env_enumeration()
    elif choice == "2":
        int_enumeration()
    elif choice == "3":
        serv_enumeration()
    elif choice == "4":
        cred_hunting()
    elif choice == "5":
        main_menu()
    else:
        lin_privesc_menu()

def env_enumeration():
    user = os.popen('whoami').read()
    print(color("\n===== ENVIRONMENT ENUMERATION ================================================================\n", B_Colors._DARK_BLUE));
    print("Press enter to execute, type N to skip")
    
    for cmd in Commands._PRIVESC_ENVENUM:
        process_command(cmd)

    process_command("find / -type f -name \".*\" -exec ls -l {} \; 2>/dev/null | grep " + user)
    print(color("\n===== END OF ENVIRONMENT ENUMERATION =========================================================", B_Colors._DARK_BLUE));
    main_menu()

def int_enumeration():
    print(color("\n===== INTERNALS ENUMERATION ==================================================================\n", B_Colors._DARK_BLUE));
    print("Press enter to execute, type N to skip")
    
    for cmd in Commands._PRIVESC_INTENUM:
        process_command(cmd)

    print(color("\n===== END OF INTERNALS ENUMERATION ===========================================================", B_Colors._DARK_BLUE));
    main_menu()

def serv_enumeration():
    print(color("\n===== SERVICES ===============================================================================", B_Colors._DARK_BLUE)+"\n");
    print("Press enter to execute, type N to skip")
    
    for cmd in Commands._PRIVESC_SERVENUM:
        process_command(cmd)

    print(color("\nDo not forget to run pspy to check all processes", B_Colors._RED_WARNING));
    print(color("\n===== END OF SERVICES ENUMERATION ============================================================", B_Colors._DARK_BLUE));
    main_menu()

def cred_hunting():
    print(color("\n===== CREDENTIAL HUNTING =====================================================================", B_Colors._DARK_BLUE)+"\n");
    print("Press enter to execute, type N to skip")
    
    for cmd in Commands._PRIVESC_CREDHUNTING:
        process_command(cmd)

    print(color("\n===== END OF CREDENTIAL HUNTING ==============================================================", B_Colors._DARK_BLUE));
    main_menu()

if __name__ == "__main__":
    try:
        print_banner()
        main_menu()
    except KeyboardInterrupt:
        print(" Finishing up...\r"),
        time.sleep(0.25)