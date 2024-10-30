import secrets as ss


class Criador():
    def __init__(self):
        print('Bem-vindo ao Criador de Senhas! \nEscolha:\n1 - Forte\n2 - Fraca')
        self.escolha = int(input(('Qual você quer? (1 ou 2):')))
        self.quantidade = int(input(('Quantos digitos você quer que tenha a sua senha? \n(Só é possivel usar números positivos): ')))
        self.gerar_senha()

    def gerar_senha(self):
        if self.escolha == 1:
            senha = ss.token_hex(self.quantidade // 2)
        else:
            senha = ''.join(ss.choice('abcdefghijklmnopqrstuvwxyz!@#$%¨&*_-+=') for _ in range(self.quantidade))
        print("Senha gerada:", senha)

Criador()

