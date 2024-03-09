import http.server
import socketserver
import os

# Set the folder you want to share
folder_to_share = r""

# Set the port for the server
port = 1234

# Change to the specified folder
os.chdir(folder_to_share)

# Create a simple server without authentication
class SimpleHandler(http.server.SimpleHTTPRequestHandler):
    pass

# Create the server with the custom handler
with socketserver.TCPServer(("", port), SimpleHandler) as httpd:
    print(f"Serving {folder_to_share} at http://localhost:{port}")
    try:
        # Start the server
        httpd.serve_forever()
    except KeyboardInterrupt:
        # Handle keyboard interrupt to stop the server
        print("\nServer stopped.")
