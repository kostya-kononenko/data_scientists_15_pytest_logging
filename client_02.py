import socket

while True:
    send_data = input('Введіть ваш запит для чат-бота: ')
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 2000))

    client_socket.sendall(send_data.encode())
    data = client_socket.recv(1024).decode()

    print('Відповідь чат-бота: ', data)

client_socket.close()
