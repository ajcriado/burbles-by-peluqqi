import sys
import os
import time

class bcolors:
    DEFAULT="\033[0;0m"
    DARKORANGE="\033[38;5;208m"
    SOFTORANGE="\033[38;5;180m"
    DARKBLUE="\033[38;5;68m"
    REDWARNING="\033[38;5;167m"
    GREY="\033[38;5;234m"

class commands:
    PRIVESC_ENVENUM=[
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
        "ls -l /tmp /var/tmp /dev/shm"
    ]
    PRIVESC_INTENUM=[
        "ip a",
        "cat /etc/hosts",
        "lastlog",
        "w",
        "history",
        "find / -type f \( -name *_hist -o -name *_history \) -exec ls -l {} \; 2>/dev/null",
        "ls -R -la /etc/cron*"
        #"find /proc -name cmdline -exec cat {} \; 2>/dev/null | tr \" \" \"\\n\""
    ]
    PRIVESC_SERVENUM=[
        "apt list --installed | tr \"/\" \" \" | cut -d\" \" -f1,3 | sed 's/[0-9]://g'",
        "sudo -V | head -n 1",
        # "ls -l /bin /usr/bin/ /usr/sbin/"
        "find / -type f \( -name *.conf -o -name *.config \) -exec ls -l {} \; 2>/dev/null",
        "find / -type f -name \"*.sh\" 2>/dev/null | grep -v \"src\|snap\|share\"",
        "ps aux | grep root",
        "ss -tulpn" # List tcp/udp listening sockets
    ]
    PRIVESC_CREDHUNTING=[
        "ls /var",
        "ls ~/.ssh",
        "find / -type f -name *.ssh -exec ls -l {} \; 2>/dev/null",
        "find / -type f -name *.bak -exec ls -l {} \; 2>/dev/null",
    ]

def color(str, code):
    return f"{code}{str}{bcolors.DEFAULT}"

def processCommand(cmd):
    choice = input("\n"+color("[>] "+cmd,bcolors.SOFTORANGE)+" ")
    if choice == "":
        os.system(cmd)

def printBanner():
    print("======================================================================================");
    print("                                                                                      ");
    print("▀█████████▄  ███    █▄     ▄████████ ▀█████████▄   ▄█          ▄████████    ▄████████ ");
    print("  ███    ███ ███    ███   ███    ███   ███    ███ ███         ███    ███   ███    ███ ");
    print("  ███    ███ ███    ███   ███    ███   ███    ███ ███         ███    █▀    ███    █▀  ");
    print(" ▄███▄▄▄██▀  ███    ███  ▄███▄▄▄▄██▀  ▄███▄▄▄██▀  ███        ▄███▄▄▄       ███        ");
    print("▀▀███▀▀▀██▄  ███    ███ ▀▀███▀▀▀▀▀   ▀▀███▀▀▀██▄  ███       ▀▀███▀▀▀     ▀███████████ ");
    print("  ███    ██▄ ███    ███ ▀███████████   ███    ██▄ ███         ███    █▄           ███ ");
    print("  ███    ███ ███    ███   ███    ███   ███    ███ ███▌    ▄   ███    ███    ▄█    ███ ");
    print("▄█████████▀  ████████▀    ███    ███ ▄█████████▀  █████▄▄██   ██████████  ▄████████▀  ");
    print("                          ███    ███                                                  ");
    print("                                                                           by peluqqi ");
    print("======================================================================================");

def mainMenu():
    print("\nMain menu:");
    print("1) Linux Privilege Escalation");
    print("2) Exit");
    choice = input("\n[>] ");
    if choice == "1":
        linPrivescMenu()
    elif choice == "2":
        sys.exit()
    else:
        mainMenu()

def linPrivescMenu():
    print("\nLinux Privilege Escalation:");
    print("1) Environment enumeration");
    print("2) Internals enumeration");
    print("3) Services enumeration");
    print("4) Credential hunting");
    print("5) Back to main menu");

    choice = input("\n[>] ");
    if choice == "1":
        envEnumeration()
    elif choice == "2":
        intEnumeration()
    elif choice == "3":
        servEnumeration()
    elif choice == "4":
        credHunting()
    elif choice == "5":
        mainMenu()
    else:
        linPrivescMenu()

def envEnumeration():
    user = os.popen('whoami').read()
    print(color("\n===== ENVIRONMENT ENUMERATION ================================================================\n",bcolors.DARKBLUE));
    print("Press enter to execute")
    
    for cmd in commands.PRIVESC_ENVENUM:
        processCommand(cmd)

    processCommand("find / -type f -name \".*\" -exec ls -l {} \; 2>/dev/null | grep "+user)
    print(color("\n===== END OF ENVIRONMENT ENUMERATION =========================================================",bcolors.DARKBLUE));
    mainMenu()

def intEnumeration():
    print(color("\n===== INTERNALS ENUMERATION ==================================================================\n",bcolors.DARKBLUE));
    print("Press enter to execute")
    
    for cmd in commands.PRIVESC_INTENUM:
        processCommand(cmd)

    print(color("\n===== END OF INTERNALS ENUMERATION ===========================================================",bcolors.DARKBLUE));
    mainMenu()

def servEnumeration():
    print(color("\n===== SERVICES ===============================================================================",bcolors.DARKBLUE)+"\n");
    print("Press enter to execute")
    
    for cmd in commands.PRIVESC_SERVENUM:
        processCommand(cmd)

    print(color("\nDo not forget to run pspy to check all processes",bcolors.REDWARNING));
    print(color("\n===== END OF SERVICES ENUMERATION ============================================================",bcolors.DARKBLUE));
    mainMenu()


def credHunting():
    print(color("\n===== CREDENTIAL HUNTING =====================================================================",bcolors.DARKBLUE)+"\n");
    print("Press enter to execute")
    
    for cmd in commands.PRIVESC_CREDHUNTING:
        processCommand(cmd)

    print(color("\n===== END OF CREDENTIAL HUNTING ==============================================================",bcolors.DARKBLUE));
    mainMenu()

if __name__ == "__main__":
    try:
        printBanner()
        mainMenu()
    except KeyboardInterrupt:
        print(" Finishing up...\r"),
        time.sleep(0.25)
