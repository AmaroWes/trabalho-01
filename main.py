from aluno import Aluno
from cantina import Cantina
from produtos import produto

aluno1 = Aluno("Carlos", 0, 0, 50)
aluno2 = Aluno("Roberto", 1, 0, 100)
aluno3 = Aluno("Ricardo", 2, 0, 0)

alunos = [aluno1, aluno2, aluno3]

cant = Cantina(alunos, produto)

if __name__ == "__main__":
    print(cant.retonar_alunos())
    #print(cant.retornar_produtos())
    print(cant.auth_cliente(1, 0))
    print(cant.fazer_pedido(1, 1))
    print(cant.fazer_pedido(1, 1))
    print(cant.fazer_pedido(1, 1))
    print(cant.retornar_pedidos())
    print(cant.retonar_alunos())