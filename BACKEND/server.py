
import socket
import datetime



# crea un objeto socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# especifica el puerto en el que el servidor escuchará
server_port = 8087

# enlaza el socket a una dirección y puerto
server_socket.bind(('17.10.10.2', server_port))

print(f"Servidor escuchando en el puerto {server_port}")

while True:
    # recibe los datos enviados por el cliente
    d, client_address = server_socket.recvfrom(1024)

    # convierto el evento a un string
    data = str(d)

    # busco donde inicia el evento y donde termina
    start = data.find('[')
    end = len(data)
    # imprimo el evento completo
    event = data[start:end]
    # procesa los datos recibidos
    print(f"command:{data}")
    print(f"Datos recibidos: {event}")
    accountNumber = data[data.find('#')+1:data.find('#')+5]
    print(f'Cuenta: {accountNumber}')
   
    ack = f'\n\ea\e80016"ACK"{accountNumber}R01L01#{accountNumber}[]\r'
    # envía una respuesta al cliente
    server_socket.sendto(ack.encode('utf-8'), client_address)