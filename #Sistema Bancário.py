# Sistema bancário com Python.

from datetime import datetime

class ContaBancaria:
    def __init__(self, email, senha, saldo=0):
        self.email = email  # atributo para armazenar o email do usuário
        self.senha = senha  # atributo para armazenar a senha do usuário
        self.saldo = saldo  # atributo para armazenar o saldo da conta
        self.extrato = []  # lista para armazenar as transações da conta
        self.limite_saques_diario = 3  # limite de saques permitidos por dia
        self.saques_feitos_hoje = 0  # contador de saques realizados no dia
        self.ultimo_dia = datetime.now().day  # para acompanhar o último dia que o usuário realizou uma transação

    def depositar(self, quantia):
        if quantia >= 0:
            self.saldo += quantia  # adiciona a quantia ao saldo
            self.extrato.append(f'Depósito de R${quantia:.2f}')  # adiciona uma entrada ao extrato
            print(f'Depósito de R${quantia:.2f} realizado com sucesso.')  # mensagem de confirmação
        else:
            print('O valor do depósito não pode ser negativo.')  # aviso se o valor do depósito for negativo

    def sacar(self, quantia):
        hoje = datetime.now().day  # obtém o dia atual
        if hoje != self.ultimo_dia:  # se for um novo dia, reseta o contador de saques diários
            self.saques_feitos_hoje = 0
            self.ultimo_dia = hoje
        
        if self.saques_feitos_hoje < self.limite_saques_diario:  # se o limite de saques diários não for atingido
            if 0 < quantia <= self.saldo:  # verifica se a quantia de saque é válida
                self.saldo -= quantia  # diminui a quantia do saldo
                self.extrato.append(f'Saque de R${quantia:.2f}')  # adiciona uma entrada ao extrato
                print(f'Saque de R${quantia:.2f} realizado com sucesso.')  # mensagem de confirmação
                self.saques_feitos_hoje += 1  # incrementa o contador de saques diários
            else:
                print('Saldo insuficiente ou valor inválido para saque.')  # aviso se o saldo for insuficiente
        else:
            print('Limite de saques diário excedido.')  # aviso se o limite de saques diários for atingido

    def verificar_saldo(self):
        print(f'Saldo atual: R${self.saldo:.2f}')  # exibe o saldo atual da conta

    def ver_extrato(self):
        print("Extrato:")  # exibe o cabeçalho do extrato
        for transacao in self.extrato:  # itera sobre as transações no extrato
            print(transacao)  # exibe cada transação


def main():
    print("Bem-vindo ao nosso banco!")  # mensagem de boas-vindas

    email = input("Digite seu email: ")  # solicita o email do usuário
    senha = input("Digite sua senha: ")  # solicita a senha do usuário
    conta = ContaBancaria(email, senha)  # cria uma instância da classe ContaBancaria

    while True:
        opcao = input(menu)  # solicita uma opção ao usuário conforme o menu

        if opcao == "d":
            quantia = float(input("Digite a quantia a ser depositada: "))  # solicita a quantia a ser depositada
            conta.depositar(quantia)  # realiza o depósito
        elif opcao == "s":
            quantia = float(input("Digite a quantia a ser sacada: "))  # solicita a quantia a ser sacada
            conta.sacar(quantia)  # realiza o saque
        elif opcao == "e":
            conta.ver_extrato()  # exibe o extrato da conta
        elif opcao == "q":
            print("Obrigado por usar nosso banco. Adeus!")  # mensagem de despedida
            break  # encerra o loop e sai do programa
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")  # aviso se a opção for inválida


if __name__ == "__main__":
    menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """.strip()  # menu de opções
    main()  # chama a função principal
fgfgh

