class Cantina:
    def __init__(self, alunos, produtos) -> None:
        self.alunos = alunos
        self.produtos = produtos
        self.fila = []

    def auth_cliente(self, matricula, senha):
        for i in range(len(self.alunos)):
            aluno = self.alunos[i].retornar_aluno()
            if aluno["Matricula"] == matricula and aluno["Senha"] == senha:
                return matricula
        return False
    
    def autenticacao_produto(self, produto):
        for i in range(len(self.produtos)):
            if self.produtos[i]["id"] == produto:
                prod = self.produtos[i]
                return prod
        return False
    
    def fazer_pedido(self, cliente, produto):
        prod = self.autenticacao_produto(produto)
        if not prod:
            return False
        
        for i in range(len(self.alunos)):
            aluno = self.alunos[i].retornar_aluno()
            if aluno["Matricula"] == cliente:
                self.alunos[i].realizar_compra(prod["Valor"])
        id_pedido = len(self.fila) + 1 
        nota = {"id": id_pedido,"cliente": cliente, "produto": prod}
        self.fila.append(nota)

    def retonar_alunos(self):
        for aluno in self.alunos:
            print(aluno.retornar_aluno())
        #return self.alunos

    def retornar_produtos(self):
        return self.produtos
    
    def retornar_pedidos(self):
        return self.fila