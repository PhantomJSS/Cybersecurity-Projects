import socket

def whois(domain: str):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("whois.verisign-grs.com", 43))

    s.send(f"{domain}\r\n".encode())
    response = s.recv(4096).decode()
    s.close()

    return response

domain = input("Please input the domain that you would like to know more about: ")
print(whois(domain))