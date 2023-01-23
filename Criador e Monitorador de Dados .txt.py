from os import system
system ('cls')
# Livraria e comando para limpar o terminal.
# Deixa o terminal mais limpo e fácil de visualizar.

# Laço infinito até que seja fechado
while True:
    try:
        def escrever_no_arquivo(file):
            # Criar o arquivo e fechar ao final da execução
            arquivo = open(file, 'w')
            # Determinar a quantidade de endereços IP que serão lidos
            qtda = int(input('Informe a quantidade de linhas para a entrada: '))
            system('cls')
            # Loop para fazer a leitura dos IPs
            for num in range(qtda):
                # Lendo um IP por linha
                print(f'{num+1}', end=' ')
                arquivo.write(f'{input()}\n')
            # Fechando o arquivo
            arquivo.close()
            
        def ler_no_arquivo(file):
            linha = 0
            # Abrindo o arquivo para leitura
            arquivo = open(file, 'r')
            # Percorrendo a lista para avaliar cada IP
            for item in arquivo:
                linha += 1
                print(f'{linha} {item}')
            # Fechando o arquivo
            arquivo.close()
            
        def buscar(file, name):
            # Criação de variáveis que serão usadas para o armazenamento
            # de onde o(s) nome(s) foi(foram) encontrado(s).
            lin_enc = 0
            linhas = []
            arquivo = open(file, 'r')
            # Loop para procurar o nome no arquivo
            for item in arquivo:
                # Variável responsável por identificar em qual(quais)
                # linha(s) o(s) nome(s) se encontra(m)
                lin_enc += 1
                detect = name + '\n'
                if item == detect:
                    # Atribui o valor da linha para identificar 
                    # onde o(s) nome(s) foi(foram) encontrado(s)
                    linhas.append(lin_enc)
            # Retorna a busca feita
            return item, linhas
        
        while True:
            # Listar opções para o usuário decidir
            print('1 - Criar e Escrever\n2 - Ler Arquivo\n3 - Buscar\n4 - Sair')
            opcao = int(input('> '))
            # Tratar as opções
            if opcao == 1:
                system ('cls')
                # Pedir o nome do arquivo
                arquivo = input('Informe o nome do arquivo: ')
                system('cls')
                # Invocando a função de escrita no arquivo
                escrever_no_arquivo(arquivo)
                
            elif opcao == 2:
                # Pedir o nome do arquivo
                arquivo = input('Informe o nome do arquivo: ')
                system('cls')
                # Invocando a função de leitura do arquivo
                ler_no_arquivo(arquivo)
                input('Pressione qualquer tecla para continuar...')
                system('cls')
                
            elif opcao == 3:
                # Pedir o nome do arquivo e da variável
                # para qual a busca será feita
                arquivo = input('Informe o nome do arquivo: ')
                nome = input('Informe o nome para a busca: ')
                # Fazer a busca
                busca, linhas = buscar(arquivo, nome)
                # Caso a busca seja bem sucedida e o caso contrário
                if busca and linhas:
                    print(f'\nNome encontrado: {nome}\nLinhas onde foi encontrado: {linhas}\n')
                else:
                    print('Nome não encontrado.')
                    
            elif opcao == 4:
                # Finalizando o loop
                system('cls')
                print ('Obrigado. Volte sempre!')
                break
            
            else:
                # Caso a opção escolhida não exista
                system ('cls')
                print ('Número inválido. Favor, informar apenas números possíveis.')
                
# Tratamento de erro e exceções
    except ValueError:
        system ('cls')
        print ('Erro de atribuição de valores numéricos. Favor, informar apenas números possíveis.')
        
    except KeyboardInterrupt:
        system ('cls')
        print ('Ctrl + C não é permitido. Favor, informar apenas números possíveis.')
        
    except FileNotFoundError:
        system ('cls')
        print ('Arquivo não encontrado. Favor, informar um arquivo válido.')
        
    finally:
        # Condições para identificar se o
        # programa deve ser fechado ou continuado
        if opcao == 4:
            break
        else:
            continue