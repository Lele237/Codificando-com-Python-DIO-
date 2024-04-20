
 # Função para verificar se B corresponde aos últimos dígitos de A
def verifica_correspondencia(A, B):
    if len(A) < len(B):
        return "nao encaixa"
    if A[-len(B):] == B:
        return "encaixa"
    else:
        return "nao encaixa"

# Leitura da quantidade de casos de teste
N = int(input())

# Processamento dos casos de teste
caso_atual = 0
while caso_atual < N:
    A, B = input().split()
    resultado = verifica_correspondencia(A, B)
    print(resultado)
    caso_atual += 1
