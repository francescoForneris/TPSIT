from socket import AF_INET, SOCK_DGRAM, socket
from Server import PORT

utente = str(input("Inserire il nome utente:"))
indirizzo = input ("Inserire il tuo indirizzo:")
def chatClient():
    with socket(AF_INET, SOCK_DGRAM) as s:
        mes = input("chat: ")
        message= utente+":"+mes
        message = message.encode('utf8')
        s.sendto(message,(indirizzo,PORT))


if __name__ == "__main__":

    chatClient()