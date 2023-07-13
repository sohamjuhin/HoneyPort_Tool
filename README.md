# HoneyPort_Tool
 honeyport tool written in Python that you can use on Kali Linux. This tool sets up a listening port that acts as a honeypot, capturing any incoming connections and logging them

 In this code, the HONEYPORT variable specifies the port number on which the honeyport will listen for incoming connections. When a connection is made to the honeyport, the log_connection() function logs the connection details, including the client's IP address and the timestamp, both printed to the console and appended to a log file named "honeyport.log".

To use this honeyport tool, save the code to a Python file (e.g., honeyport.py) on your Kali Linux machine. Then, open a terminal and navigate to the directory where the file is saved. Run the tool using the Python interpreter with the command: python honeyport.py

Any connections made to the specified honeyport will be logged. You can customize the logging behavior or extend the functionality based on your specific requirements. Remember to use this tool responsibly and comply with legal and ethical considerations when deploying honeypots
