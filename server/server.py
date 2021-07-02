import socket
import json
from random import randint

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

host = '192.168.188.1'
port = 9090

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def login_check(request):
    with open("userbase.json", "r", encoding="UTF-8") as database:
        data = json.loads(database.read())
        username = request[1]['login']
        if data[username]:
            return 0 if data[username] == request[1]['password'] else 1
        else:
            return 2  # incorrect username


def email_check(request):
    to_email = request[1]['email']
    from_email = "leucist@yandex.by"
    password = "Ijrjkflrf2004"
    key = randint(100000000000, 999999999999)

    msg = MIMEMultipart()
    # ---!!!---------------->
    # App name required
    # ---!!!---------------->
    message = 'Здравствуйте, ' + request[1]['username'] + '.\nВаш код подтверждения регистрации: ' + str(
        key) + '\nКод действителен в течение двух часов, введите его в приложении\n\n*В приложении «App» был создан запрос на регистрацию новой учетной записи с указанием Вашего адреса электронной почты. Если это были не Вы, просто проигнорируйте данное сообщение.'
    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com: 465')
    server.starttls()
    server.login(from_email, password)
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()

    return key


def registration(request, client_socket):
    with open("userbase.json", "r", encoding="UTF-8") as database:
        data = json.loads(database.read())
        for user in data:
            if user == request[1]['username']:
                return 2  # username already taken
        else:
            key = email_check(request)
            user = {'password': request[1]['password'], 'email': request[1]['email']}
            response = 0
            client_socket.sendall(response)
            request = client_socket.recv(1024)
            request = request.decode('UTF-8')
            request = json.loads(request)


def s_recieve(s_quit):
    while not s_quit:
        try:
            client_socket, addr = server_socket.accept()
            request = client_socket.recv(1024)
            request = request.decode('UTF-8')
            request = json.loads(request)
            print("--[" + str(addr[0]) + "][" + str(addr[1]) + "]---Connected")
            if not request[0]:
                continue  # or, IDK, send smth, be kind and gentle:))
            if request[0] == 'loginform':
                response = json.dumps(login_check(request))
                client_socket.sendall(response.encode())
                client_socket.close()
            elif request[0] == 'registerform':
                registration(request, client_socket)
                # response = json.dumps(registration(request))
                # client_socket.sendall(response.encode())
                client_socket.close()
        except:
            print("<---Server-stopped--->")
            s_quit = True


def start():
    server_socket.bind((host, port))
    s_quit = False
    server_socket.listen()
    print("<---Server-started--->")
    s_recieve(s_quit)


if __name__ == '__main__':
    start()
