# Purpose
This tool was created to automate the command execution process on routers. Rather than logging into each router and running a command by hand manually, this tool will allow for multiple commands to be executed on multiple devices sequentially. 

# Features
1. Log into each router sequentially and execute commands.
2. Outputs the command session and output to a text file in the output directory.

# Limitations 
- Cannot execute on more than one router at a time
- No validation of commands being executed
- Can only execute the same commands on each router
- Can only execute on Nokia SR-Linux or one vendor at a time. 

# Roadmap
No priority here, just things that are wanted/needed. 
1. Be able to execute different commands on different routers.
2. Be able to execute commands on multiple vendors of routers.
3. Be able to connect and execute commands on multiple routers at the same time.
4. Be able to send the output directory via email to a distro.
5. Be able to SFTP config files to devices. 

# Requirements
1. Nemiko
2. Python3
3. Lab routers/switches

# Notes
This is an entry level development project being written by a Network engineer. This goal for this is for me to learn and build a functioning tool without using AI to actually write the tool. Suggestions are welcome, however, I will not be accepting changes to the codebase as I want to write this myself. Please feel free to fork the repo and develop independently. 
