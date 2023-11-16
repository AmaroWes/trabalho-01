import socket


HOST = 'localhost'
PORT = 50007

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    login = str(input("Matricula: "))
    senha = str(input("Senha: "))
    mensagem = login + '/' + senha

    sock.connect((HOST, PORT))
    sock.sendall(bytes(mensagem, "utf-8"))

    data = sock.recv(1024)
    print(bytes.decode(data))
    mensagem = str(input('Option: '))
    sock.sendall(bytes(mensagem, "utf-8"))

    data = sock.recv(1024)
    print(bytes.decode(data))
    opt = str(input('Confirmar o pedido [S/N]: '))
    sock.sendall(bytes(opt, "utf-8"))

    data = sock.recv(1024)
    print(bytes.decode(data))
