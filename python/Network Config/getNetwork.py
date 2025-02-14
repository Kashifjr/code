import socket
import os

# gets all ip address
def get_ip_address():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)

    print(hostname)
    print(IPAddr)

    print(os.system('ip -4 addr '))

def main():
    get_ip_address()


main()