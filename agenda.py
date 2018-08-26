#Agenda Telefonica
import funcoes

funcoes.bemvindo()
#funcoes.menu()

#Opcoes do Usuario
opcao = int(input())
print("Selecionou a ", opcao)

#Estrutura de controle/Aula: Seleção da solição
if opcao == 1:
	funcoes.adicionar()
elif opcao == 2:
	funcoes.listar()
else:
	funcoes.falha()


