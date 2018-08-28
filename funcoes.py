#Mensagem de Bem Vindo e Opcoes ao Usuario
def bemvindo():
	print("Bem Vindo a Agenda")   #Função de abertura do programa em Python!!!!!!!!!!
	print("Selecione uma Opcao")
	print("1  Adicionar um novo contato")
	print("2  Listar os contatos da agenda")

#Funcoes do processo
def adicionar():
	print("Adicionar um registro") #Adicionado funcao adicionar 
	
	agenda = open("agendatelefonica.csv",'a')
	nome = input("Nome do Contato:")
	telefone = input("Digite o telefone:")
	print("Contato salvo com nome:",nome," e numero",telefone)
	agenda.write(nome)
	agenda.write(",") #Escrevendo arquivo.csv
	agenda.write(telefone) #Escrevendo arquivo.csv
	agenda.write(",")  #Escrevendo arquivo.csv
	agenda.write("\n") #Escrevendo arquivo.csv
	agenda.close()
#Função Listar	
def listar():
	print("Lista de Contatos") #mostra a lista de contatos
	
	agenda = open("agendatelefonica.csv")
	numero = 0
	while numero < 25: #laço de repetição
                
	 	print (agenda.readline())
	 	numero = numero + 1
	print("Listado correctamente")	
	agenda.close() #fim da execução

def falha():
	print("Opcao Incorreta")#Codigo Sera Executado Ao Inserir Dado Invalido

def menu():
        print("+----------------------+")   #meno para seleção dentro do programa 
        print("          Menu          ")
        print("     1 - Adicionar      ")
        print("     2 - Listar         ")
        print("+----------------------+")

        
        


        
	
