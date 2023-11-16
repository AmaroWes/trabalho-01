import socket
from threading import Thread
from aluno import Aluno
from cantina import Cantina
from produtos import produto

HOST = ''
PORT = 50007

aluno1 = Aluno("Carlos", "0", "0", 50)
aluno2 = Aluno("Roberto", "1", "0", 100)
aluno3 = Aluno("Ricardo", "2", "0", 0)
alunos = [aluno1, aluno2, aluno3]

cant = Cantina(alunos, produto)

def menu_process(item):
    menu = item.retornar_produtos()
    ret = '\nMENU:\n'
    for m in menu:
        ret = ret + f'Item: {m["id"]} - Nome: {m["Nome"]} - Valor: {m["Valor"]}\n'
    return ret

def pedido_process(item):
    pedido = item.retornar_pedidos()
    ret = '\nPEDIDO:\n'
    for p in pedido:
        ret = ret + f"Número do pedido: {p['id']}\nCliente {p['cliente']}\nProduto: {p['produto']['Nome']}\nValor: {p['produto']['Valor']}"
    return ret

def handler(conn):
    while True:
        data = conn.recv(1024)
        if not data: break
        msg = bytes.decode(data).split('/')
        auth = cant.auth_cliente(msg[0], msg[1])
        
        if not auth: break
        menu = menu_process(cant)
        conn.sendall(bytes(menu, "utf-8"))
        data = conn.recv(1024)
        produto = bytes.decode(data)

        if not cant.autenticacao_produto(produto): break
        cant.fazer_pedido(auth, produto)

        pedido = pedido_process(cant)
        conn.sendall(bytes(pedido, "utf-8"))
        data = conn.recv(1024)
        opt = bytes.decode(data)

        if opt.upper() == "S":
            conn.sendall(bytes("Pedido confirmado", "utf-8"))
        break

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    sock.listen(1)
    while True:
        conn, addr = sock.accept()
        thrd = Thread(target=handler, args=[conn])
        thrd.start()