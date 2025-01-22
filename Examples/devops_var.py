#Define Configuration Variables for a Wed Server
server_name = "My_Nginx_Server"
port = 80
is_https_enabled = False
max_connections = 500

#Print the Configuration
print(f"Server Name: {server_name}")
print(f"Port: {port}")
print(f"HTTPs Enabled: {is_https_enabled}")
print(f"Max Connections: {max_connections}")

#Update Configuration Values
port = 443
is_https_enabled = True

#Print the Updated Configuration
print(f"Updated Port: {port}")
print(f"HTTPs Enabled: {is_https_enabled}")