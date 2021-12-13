@echo off
echo Master, Clients and Projectors will shut down. Confirm?
echo.
pause
Rem  Projectors shutting down with TCP commands, check the python script for details.
echo ----------------------------------------------------------------
OFF_Prj.py
Rem Shutting Down Remote Servers in the LAN
echo.
shutdown /s /f /m \\SIM-IG1
shutdown /s /f /m \\SIM-IG2
shutdown /s /f /m \\SIM-IG3
Rem Shutting Down Local Master
echo.
shutdown /s /f /t 05
cmd /k
