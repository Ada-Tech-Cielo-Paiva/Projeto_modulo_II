# @file Projeto_risco_de_credito.ipynb
# @author Anderson Duarte de Paiva
# @author Anderson de Oliveira
# @author Bruno Beltrame
# @date 23 Fevereiro 2024


# Importacao da biblioteca csv para leitura, escrita e manipulação dos dados
import csv

# Inicializar uma lista vazia para armazenar os dados de risco de crédito
credit_risk_data = []

# Abre o arquivo CSV "german_credit_risk.csv" em modo leitura 'r'
# A instrução with garante o fechamento do arquivo de forma automática
with open('german_credit_risk.csv', 'r', encoding='utf-8-sig') as file:
    # Leitura do arquivo csv convertendo cada linha em um dicionário
    reader = csv.DictReader(file)
    # Percorre/itera cada linha do dicionário
    for row in reader:
        #Adiciona cada linha à lista vazia credit_risk_data
        credit_risk_data.append(row)

# CRIA UM DICIONÁRIO DO TIPO "CREDIT_RISK_DATA"
def get_credit_risk_entry():
    # Dicionário vazio para armazenar os dados do usuário
    data = {}
    try:
        # Solicita ao usuário fornecer/digitar as informações em cada campo
        data[''] = len(credit_risk_data)
        data['Age'] = input("Digite a Idade: ")
        data['Sex'] = input("Digite o Sexo: ")
        data['Job'] = input("Digite o Trabalho: ")
        data['Housing'] = input("Digite a Moradia: ")
        data['Saving accounts'] = input("Digite a Conta de Poupança: ")
        data['Checking account'] = input("Digite a Conta Corrente: ")
        data['Credit amount'] = input("Digite o Valor do Crédito: ")
        data['Duration'] = input("Digite a Duração: ")
        data['Purpose'] = input("Digite o Propósito: ")
        data['Risk'] = input("Digite o Risco: ") 
    # Trata as exceções do tipo Exception       
    except Exception as e:
        # Exibe o erro com os detalhes sobre a exceção
        print(f"Error: {e}")
    # Retorna o dicionário contendo os dados do usuário
    return data

# Função para criar um novo registro de risco de crédito
def create_credit_risk_entry(data):
    # Trecho do código onde podem ocorrer exceções
    try:
        # Verificar se os dados são um dicionário
        if isinstance(data, dict):
            # Adicionar os dados à lista de risco de crédito
            credit_risk_data.append(data)
            # Imprime uma mensagem caso o registro seja criado com sucesso
            print("Registro de risco de crédito criado com sucesso.")
        else:
            # Indica uma exceção do tipo "ValueError" com uma mensagem personalizada/associada
            raise ValueError("Formato de dados inválido. Por favor, forneça um dicionário.")
    # Trata as exceções do tipo Exception 
    except ValueError as e:
        # Exibe o erro com os detalhes sobre a exceção
        print(f"Erro: {e}")



# Função para ler todos os registros de risco de crédito
def read_credit_risk_entries():
    # Trecho do código onde podem ocorrer exceções
    try:
        # Verificar se existem registros de risco de crédito
        if len(credit_risk_data) > 0:
            # Imprimir cada registro de risco de crédito
            for entry in credit_risk_data:
                print(entry)
        else:
            print("Nenhum registro de risco de crédito encontrado.")
    # Trata as exceções do tipo Exception
    except Exception as e:
        # Exibe o erro com os detalhes sobre a exceção
        print(f"Erro: {e}")


# Define a função chamada update com dois parâmetros data que é um dicionário e o index
def update(data, index):
    # Trecho do código onde podem ocorrer exceções
    try:
        # Atualizando cada dado do dicionario
        data[''] = index
        # Solicita ao usuário fornecer/digitar as informações em cada campo. Assim, o campo é atualizado
        data['Age'] = input("Digite a Idade: ")
        data['Sex'] = input("Digite o Sexo: ")
        data['Job'] = input("Digite o Trabalho: ")
        data['Housing'] = input("Digite a Moradia: ")
        data['Saving accounts'] = input("Digite a Conta de Poupança: ")
        data['Checking account'] = input("Digite a Conta Corrente: ")
        data['Credit amount'] = input("Digite o Valor do Crédito: ")
        data['Duration'] = input("Digite a Duração: ")
        data['Purpose'] = input("Digite o Propósito: ")
        data['Risk'] = input("Digite o Risco: ")
        
        print("Information updated successfully.")
        # Retorna o dicionário contendo os dados atualizados do usuário
        return data

    except Exception as e:
        # Exibe o erro com os detalhes sobre a exceção
        print(f"Error: {e}")
 

# Função para atualizar um registro de risco de crédito
def update_credit_risk_entry(index, data):
    try:
        # Verificar se o índice é válido
        if index >= 0 and index < len(credit_risk_data):
            # Verificar se os dados são um dicionário
            if isinstance(data, dict):
                # Atualizar o registro de risco de crédito no índice especificado
                credit_risk_data[index] = data
                print("Registro de risco de crédito atualizado com sucesso.")
            else:
                raise ValueError("Formato de dados inválido. Por favor, forneça um dicionário.")
        else:
            raise IndexError("Índice inválido. Por favor, forneça um índice válido.")
    except (ValueError, IndexError) as e:
        print(f"Erro: {e}")


# Função para excluir um registro de risco de crédito
def delete_credit_risk_entry(index):
    try:
        # Verificar se o índice é válido
        if index >= 0 and index < len(credit_risk_data):
            # Excluir o registro de risco de crédito no índice especificado
            del credit_risk_data[index]
            print("Registro de risco de crédito excluído com sucesso.")
        else:
            raise IndexError("Índice inválido. Por favor, forneça um índice válido.")
    except IndexError as e:
        print(f"Erro: {e}")

# FUNÇÃO PARA SALVAR A LISTA NO ARQUIVO CSV
def exportar_csv(lista):
    with open('german_credit_risk.csv', 'w', encoding='utf-8-sig', newline='') as file:
        fieldnames = ['','Age', 'Sex', 'Job', 'Housing', 'Saving accounts', 'Checking account', 'Credit amount', 'Duration', 'Purpose', 'Risk']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()  # Escreve o cabeçalho no arquivo CSV
        for data in lista:
            writer.writerow(data)  # Escreve os dados no arquivo CSV

#FUNÇÃO MENU
def menu():
    while True:
        try:
            #MENU PARA MOSTRAR TODAS AS OPÇÕES
            print("Menu:")
            print("1. Criar novo registro de risco de crédito")
            print("2. Ler todos os registros de risco de crédito")
            print("3. Atualizar um registro de risco de crédito")
            print("4. Excluir um registro de risco de crédito")
            print("0. Sair")

            #VARIÁVEL PARA INSERIR A OPÇÃO DO MENU
            choice = input("Escolha uma opção: ")

            #OPÇÃO 1 - CRIAR UM NOVO REGISTRO
            if choice == "1":
                #VARIÁVEL DATA RECEBE A FUNÇÃO "get_credit_risk_entry" QUE RETORNA UM DICIONÁRIO
                #QUE FOI CRIADO PELO USUÁRIO
                data = get_credit_risk_entry()
                #FUNÇÃO PARA INSERIR O DICIONÁRIO QUE FOI PASSADO POR PARÂMETRO NA LISTA
                create_credit_risk_entry(data)
            #OPÇÃO 2 - LER TODOS OS REGISTROS
            elif choice == "2":
                #FUNÇÃO PARA LER TODOS OS REGISTROS DA LISTA
                read_credit_risk_entries()

            # OPÇÃO 3 - ATUALIZAR REGISTO PELO INDEX
            elif choice == "3":
                #FUNÇÃO PARA ATUALIZAR ALGUM DICIONÁRIO DA LISTA PELO INDEX
                index = int(input("Digite o índice do registro a ser atualizado: "))
                #VARIÁVEL DATA RECEBE A FUNÇÃO UPDATE QUE RETORNA O DICIONARIO JÁ ATUALIZADO
                data = update(credit_risk_data[index], index)
                #A FUNÇÃO QUE ATUALIZA O DICIONÁRIO DA LISTA PASSANDO POR PARÂMETRO O INDEX E O DICIONÁRIO JA ATUALIZADO
                update_credit_risk_entry(index, data)
                
            #OPÇÃO 4 - DELETAR ALGUM REGISTRO
            elif choice == "4":
                
                index = int(input("Digite o índice do registro a ser excluído: "))
                #fUNÇÃO PARA DELETAR UM DICIONARIO DA LISTA PELO INDEX
                delete_credit_risk_entry(index)

            # OPÇÃO 0 - SAIR DO PROGRAMA
            elif choice == "0":
                print('Programa Finalizado...')
                #FUNÇÃO PARA EXPORTAR O ARQUIVO, GARANTINDO A CONSISTÊNCIA DOS DADOS
                exportar_csv(credit_risk_data)
                break
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")
        except KeyboardInterrupt:
            print("Operação interrompida pelo usuário.")
        
        

menu()