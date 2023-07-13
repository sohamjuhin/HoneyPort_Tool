import socket
import datetime

# Configuration
HONEYPORT = 9999  # Port to listen on

# Function to log connection details
def log_connection(client_addr):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] Connection from {client_addr[0]}:{client_addr[1]}"
    print(log_entry)
    with open("honeyport.log", "a") as log_file:
        log_file.write(log_entry + "\n")

# Main function to listen for incoming connections
def honeyport():
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Set socket options to reuse address and enable listening
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("", HONEYPORT))
    server_socket.listen(5)
    print(f"Honeyport listening on port {HONEYPORT}...")

    while True:
        # Accept incoming connections
        client_socket, client_addr = server_socket.accept()
        # Log the connection details
        log_connection(client_addr)
        # Close the connection
        client_socket.close()

# Execute the honeyport function
if __name__ == "__main__":
    honeyport()
