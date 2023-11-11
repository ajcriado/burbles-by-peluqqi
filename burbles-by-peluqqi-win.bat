@echo off

echo "=================================================================="
echo "|                _                _     _                        |"
echo "|               | |              | |   | |                       |"
echo "|               | |__  _   _ _ __| |__ | | ___  ___              |"
echo "|               | '_ \| | | | '__| '_ \| |/ _ \/ __|             |"
echo "|               | |_) | |_| | |  | |_) | |  __/\__ \             |"
echo "|               |_.__/ \__,_|_|  |_.__/|_|\___||___/             |"
echo "|                                                                |"
echo "|                                       by peluqqi               |"
echo "=================================================================="
echo "                      Situational Awareness                       "
echo "=================================================================="
echo "Press enter to execute, type N to skip"
echo.
call :executeCommand "ipconfig /all"
call :executeCommand "arp -a"
call :executeCommand "route print"
call :executeCommand "Get-MpComputerStatus"
call :executeCommand "Get-AppLockerPolicy -Effective | select -ExpandProperty RuleCollections"
call :executeCommand "Get-AppLockerPolicy -Local | Test-AppLockerPolicy -path C:\Windows\System32\cmd.exe -User Everyone"
echo.

echo "=================================================================="
echo "                      Initial enumeration                         "
echo "=================================================================="
echo.
call :executeCommand "tasklist /svc"
call :executeCommand "set"
call :executeCommand "systeminfo"
call :executeCommand "wmic qfe"
call :executeCommand "Get-HotFix | ft -AutoSize"
call :executeCommand "wmic product get name"
call :executeCommand "Get-WmiObject -Class Win32_Product |  select Name, Version"
call :executeCommand "netstat -ano"
call :executeCommand "query user"
call :executeCommand "echo %USERNAME%"
call :executeCommand "whoami /priv"
call :executeCommand "whoami /groups"
call :executeCommand "net user"
call :executeCommand "net localgroup"
call :executeCommand "net localgroup administrators"
call :executeCommand "net accounts"
echo.

echo "=================================================================="
echo "                      Communication with processes                "
echo "=================================================================="
echo.
call :executeCommand "netstat -ano"
call :executeCommand "pipelist.exe /accepteula"
call :executeCommand "gci \\.\pipe\"
call :executeCommand "accesschk.exe /accepteula \\.\Pipe\lsass -v"
call :executeCommand "accesschk.exe -accepteula -w \pipe\<service> -v"
echo.

echo "=================================================================="
echo "                      Exploitable permissions                     "
echo "=================================================================="
echo.
echo "User privileges:"
echo "  > SeImpersonate and SeAssignPrimaryToken"
echo "  > SeDebugPrivilege"
echo "  > SeTakeOwnershipPrivilege"
echo "Group privileges:"
echo "  > SeBackupPrivilege"
echo.

pause
exit

:executeCommand
setlocal enabledelayedexpansion
set /p userCmd="[>] %~1 "
if "!userCmd!"=="" (
    %~1
)
endlocal
echo.
goto :eof