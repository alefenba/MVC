from model import Pessoa
class PessoaDal():
    @classmethod
    def salvar(cls, pessoa: Pessoa):
        with open ('pessoas.txt', 'w' ) as arq:
            arq.write(pessoa.nome + " " + str(pessoa.idade) + " " + pessoa.cpf)


    @classmethod
    def ler(cls):
        nome = " Alefe"
        idade = 24
        cpf = 12345678
        return Pessoa(nome, idade , cpf)


p1 = Pessoa('Alefe', 24, '12345678')
print(PessoaDal.ler().nome)
