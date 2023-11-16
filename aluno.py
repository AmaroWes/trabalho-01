class Aluno:
    def __init__(self, nome, matricula, senha=0, saldo=0) -> None:
        self.nome = nome
        self.matricula = matricula
        self.saldo = saldo
        self.senha = senha

    def verificar_saldo(self):
        return self.saldo

    def realizar_compra(self, valor):
        self.saldo -= valor

    def retornar_aluno(self):
        aluno = {"Nome": self.nome, "Matricula": self.matricula,"Senha": self.senha, "Saldo": self.saldo}
        return aluno