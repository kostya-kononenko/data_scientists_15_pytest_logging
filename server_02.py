import socket
import logging

logging.basicConfig(level=logging.INFO, filename='Client_error.log',
                    format='server %(asctime)s - %(levelname)s - %(message)s')

listening_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listening_socket.bind(('127.0.0.1', 2000))
listening_socket.listen(4)

while True:
    socket_for_communication, addr = listening_socket.accept()
    print('Приєднався до: ', addr)
    data = socket_for_communication.recv(1024).decode()
    if data == 'Рубрика_1':
        logging.info("Обрана інформаційна рубрика")
        answer = 'Інформаційна рубрика'
        socket_for_communication.sendall(answer.encode())
    elif data == 'Рубрика_2':
        logging.warning("Обрана заборонена рубрика")
        answer = 'Заборонена рубрика'
        socket_for_communication.sendall(answer.encode())
    else:
        logging.error("Така рубрика відсутня, повторіть будь ласка")
        error = 'Така рубрика відсутня, повторіть будь ласка'
        socket_for_communication.sendall(error.encode())
    socket_for_communication.close()

listening_socket.close()

