from socket import AF_INET, SOCK_DGRAM, socket

def chatClient():
    with socket(AF_INET, SOCK_DGRAM) as s:
        message = 'forne'
        message = message.encode('utf8')
        s.sendto(message,("192.168.95.255",5000))


if __name__ == "__main__":

    chatClient()