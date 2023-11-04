import sys
import os
import time

class bcolors:
    DARKORANGE="\033[38;5;208m"
    SOFTORANGE="\033[38;5;180m"
    DEFAULT="\033[0;0m"
    DARKBLUE="\033[38;5;68m"
    GREY="\033[38;5;234m"

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
    print("2) Services and internals enumeration");
    print("3) Back to main menu");
    choice = input("\n[>] ");
    if choice == "1":
        envEnumeration()
    elif choice == "2":
        servEnumeration()
    elif choice == "3":
        mainMenu()
    else:
        linPrivescMenu()

def envEnumeration():
    user = os.popen('whoami').read()
    print(color("\n===== ENVIRONMENT ENUMERATION ========================================================\n",bcolors.DARKBLUE));
    print(color("[>] whoami",bcolors.SOFTORANGE))
    print(f"{user}")
    print(color("[>] id",bcolors.SOFTORANGE))
    os.system("id")
    print(color("\n[>] hostname",bcolors.SOFTORANGE))
    os.system("hostname")
    print(color("\n[>] ip a",bcolors.SOFTORANGE))
    os.system("ip a")
    print(color("\n[>] sudo -l",bcolors.SOFTORANGE))
    choice = input("You may need to introduce a password, do you want to continue? (y/N) ");
    if choice == "y" or choice == "Y" or choice == "YES" or choice == "yes":
        os.system("sudo -l")
    print(color("\n[>] cat /etc/os-release",bcolors.SOFTORANGE))
    os.system("cat /etc/os-release")
    print(color("\n[>] echo $PATH",bcolors.SOFTORANGE))
    os.system("echo $PATH")
    print(color("\n[>] env",bcolors.SOFTORANGE))
    os.system("env")
    print(color("\n[>] uname -a",bcolors.SOFTORANGE))
    os.system("uname -a")
    print(color("\n[>] lscpu",bcolors.SOFTORANGE))
    os.system("lscpu")
    print(color("\n[>] cat /etc/shells",bcolors.SOFTORANGE))
    os.system("cat /etc/shells")
    print(color("\n[>] cat /etc/fstab | grep -v \"#\" | column -t",bcolors.SOFTORANGE))
    os.system("cat /etc/fstab | grep -v \"#\" | column -t")
    print(color("\n[>] route",bcolors.SOFTORANGE))
    os.system("route")
    print(color("\n[>] arp -a",bcolors.SOFTORANGE))
    os.system("arp -a")
    print(color("\n[>] cat /etc/passwd",bcolors.SOFTORANGE))
    os.system("cat /etc/passwd")
    print(color("\n[>] cat /etc/shadow",bcolors.SOFTORANGE))
    os.system("cat /etc/shadow")
    print(color("\n[>] cat /etc/group",bcolors.SOFTORANGE))
    os.system("cat /etc/group")
    print(color("\n[>] ls /home",bcolors.SOFTORANGE))
    os.system("ls /home")
    print(color("\n[>] df -h",bcolors.SOFTORANGE))
    os.system("df -h")
    print(color("\n[>] find / -type f -name \".*\" -exec ls -l {} \; 2>/dev/null | grep "+user,bcolors.SOFTORANGE))
    os.system("find / -type f -name \".*\" -exec ls -l {} \; 2>/dev/null | grep "+user)
    print(color("\n[>] find / -type d -name \".*\" -ls 2>/dev/null",bcolors.SOFTORANGE))
    os.system("find / -type d -name \".*\" -ls 2>/dev/null")
    print(color("\n[>] ls -l /tmp /var/tmp /dev/shm",bcolors.SOFTORANGE))
    os.system("ls -l /tmp /var/tmp /dev/shm")    

    print(color("\n===== END OF ENVIRONMENT ENUMERATION =================================================",bcolors.DARKBLUE));
    mainMenu()

def servEnumeration():
    print(""+color("\n===== SERVICES AND INTERNALS ENUMERATION =============================================",bcolors.DARKBLUE)+"\n");
    print(color("\n[>] ip a",bcolors.SOFTORANGE))
    os.system("ip a")
    print(color("\n[>] cat /etc/hosts",bcolors.SOFTORANGE))
    os.system("cat /etc/hosts")
    print(color("\n[>] lastlog",bcolors.SOFTORANGE))
    os.system("lastlog")
    print(color("\n[>] w",bcolors.SOFTORANGE))
    os.system("w")
    print(color("\n[>] history",bcolors.SOFTORANGE))
    os.system("history")
    print(color("\n[>] find / -type f \( -name *_hist -o -name *_history \) -exec ls -l {} \; 2>/dev/null",bcolors.SOFTORANGE))
    os.system("find / -type f \( -name *_hist -o -name *_history \) -exec ls -l {} \; 2>/dev/null")
    print(color("\n[>] ls -R -la /etc/cron*",bcolors.SOFTORANGE))
    os.system("ls -R -la /etc/cron*")
    """print(color("\n[>] ip a",bcolors.SOFTORANGE))
    os.system("ip a")
    print(color("\n[>] ip a",bcolors.SOFTORANGE))
    os.system("ip a")"""

def color(str, code):
    return f"{code}{str}{bcolors.DEFAULT}"

if __name__ == "__main__":
    try:
        printBanner()
        mainMenu()
    except KeyboardInterrupt:
        print(" Finishing up...\r"),
        time.sleep(0.25)