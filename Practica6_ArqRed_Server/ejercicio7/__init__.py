from socket import *
from random import *


serverSocket= socket(AF_INET, SOCK_DGRAM)

# Bind the socket to the port
server_address = ('192.168.56.1', 50010)
canal_socket_adress = ('192.168.56.1', 40010)

print('starting up on {} port {}'.format(*server_address))

serverSocket.bind(server_address)

def CheckSum(msg):
    suma = 0
    for i in msg:
        n_ascii = ord(i)
        suma += n_ascii
    ck1 = suma//256
    ck2 = suma%256
    
    ck1_ch = chr(ck1)
    ck2_ch = chr(ck2)
    
    return f'{msg}{ck1_ch}{ck2_ch}'

def ACK():
    
    cadena = []
    
    tp = 'ACK'
    sec = '1' 
    
    return f'{tp}{sec}'

while True:
# Wait for a message
    print('\nwaiting to receive message')
    
    #recibe mensaje por el canal
    mensaje_rx, recv_address= serverSocket.recvfrom(2048)
    
    #si hay mensaje
    if mensaje_rx:
        
        #separ checksum del mensaje recibido
        msg_rx = mensaje_rx.decode()[:-2]
        ck_rx = mensaje_rx.decode()[-2:]
        
        #calcular checksum de msg_rx
        ck_rx_prima = CheckSum(msg_rx)
        
        #si los checksums no coinciden, envia un nak
        if ck_rx != ck_rx_prima[-2:]:
            new_msg = 'NAK'
        else:
            new_msg = CheckSum(ACK())
    
        serverSocket.sendto(new_msg.encode(),canal_socket_adress)
        
        print(recv_address)
        print(msg_rx)
        print(new_msg)
            
# Clean up the connection
serverSocket.close()

