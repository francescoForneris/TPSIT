from socket import AF_INET, SOCK_DGRAM, socket

BUFFER_SIZE = 1024
HOST = "0.0.0.0"
PORT = int(input("Inserisci la porta:"))


exit = True
# possibilità
# localhost 127.0.0.1 
def chatServer():
    with socket(AF_INET, SOCK_DGRAM) as s:  #Apriamo una risorsa
        s.bind((HOST, PORT))
        while exit:
            message = s.recvfrom(BUFFER_SIZE)
            message = message[0].decode()
            print(message)

if __name__ == "__main__":
    chatServer()