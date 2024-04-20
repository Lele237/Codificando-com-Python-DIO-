# Codificando-com-Python-DIO-

<img src="https://cdn.discordapp.com/attachments/893692958623268874/1220113361333915798/Captura_de_tela_2024-03-20_175046.png?ex=6632ac1d&is=6620371d&hm=2ba8295c3144c5471efbc562488abaf27446087097d1b66fb84569e939cb82a9&"/>

1- ``def:`` Esta é uma função que verifica se B corresponde aos últimos dígitos de A. Ela recebe dois argumentos, A e B, que são strings representando números.

2- ``if 1:`` Verifica se o comprimento de A é menor que o comprimento de B. Se isso acontecer, significa que B não pode ser uma parte de A, então retorna "nao encaixa".

3- ``if 2:`` Verifica se os últimos dígitos de A (obtidos usando slicing com índice negativo) são iguais a B. Se forem iguais, retorna "encaixa", caso contrário, retorna "nao encaixa".

4- ``(N = int(input())):`` Solicita ao usuário que insira a quantidade de casos de teste e armazena o valor em N, que é o número de vezes que o loop while iterará.

## Loop while para processamento dos casos de teste: 

``caso_atual = 0:`` Inicializa uma variável caso_atual com valor 0, que será usada para controlar o número de casos de teste processados.

``while:`` Este loop while é executado enquanto o número de casos de teste processados (caso_atual) for menor que o número total de casos de teste (N).

``input().split():`` Lê a entrada que contém os valores de A e B separados por espaço e atribui a A e B, respectivamente.

``resultado = verifica_correspondencia(A, B):`` Chama a função verifica_correspondencia() com os valores de A e B e armazena o resultado retornado na variável resultado.

``caso_atual += 1:`` Incrementa o número de casos de teste processados para controlar o loop.

## Resultado

encaixa
nao encaixa
encaixa
nao encaixa
