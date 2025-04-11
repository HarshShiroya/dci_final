from flask import Flask
import socket

app = Flask(__name__)
hostname = socket.gethostname()
try:
    ip_address = socket.gethostbyname(hostname)
    print(f"Successfully resolved hostname '{hostname}' to IP: {ip_address}")
except socket.gaierror:
    print(f"socket.gethostbyname failed for hostname '{hostname}', trying fallback...")
    ip_address = "No ip found in the host"

@app.route('/')
def hello_cloud():
  return 'Welcome to Harsh Final Test API Server'

  
@app.route('/host')
def host_name():
  return hostname

@app.route('/ip')
def host_ip():
  return ip_address

app.run(host='0.0.0.0')