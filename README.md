# Projection-System-Control
A collection of Python and Batch scripts to control a projection system: power on, shutdown, source switch, remote restart..etc.<br><br>
The setup is based on NORXE P1 projectors and 4x servers, it can be edited by simply switching IPs and TCP string messages.

## How to activate remote shutdown for network servers:
1. Group Policy
- Open Local Group Policy Editor (or run "gpedit.msc") 
- Go Local Policies/User Rights Assignment and open "Force shutdown from a remote system"
- Add a the master user account to the policy, or "everyone" ("jeder" in German OS)

2. Remote Registry
- From Windows Services, locate the Remote Registry service, right-click it and select Properties.
- Set its startup to automatic then save and run it.

