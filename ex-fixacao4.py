# ==============================================================================
# Projeto: Sistema de Gerenciamento de Livros (Exercício Acadêmico Python)
# Autor(a): Ana Laura Feltrin
# Descrição: Sistema via console para cadastro, consulta e remoção de livros
# utilizando listas, dicionários, funções e laços de repetição.
# ==============================================================================

# A. Mensagem de boas-vindas com nome e sobrenome
print('Bem-vindo a Livraria de Ana Laura Feltrin')

# B. Inicialização da lista vazia para armazenar os dicionários de livros
# e da variável com o ID global inicializado com o número do RU
lista_livros = []
dicionario = {}
id_global = 6053581
print('\n==============================')
print('       MENU PRINCIPAL         ')
print('==============================')
print('1 - Cadastrar livro')
print('2 - Consultar livro(s)')
print('3 - Remover livro')
print('4 - Sair')

# C. Função para cadastrar novos livros
def cadastrar_livro(id):
    print('MENU CADASTRAR')
    print(f'Id do livro: {id}')

    # Criação de um dicionário local para armazenar os dados do livro atual
    dicionario['id'] = id
    dicionario['nome'] = input('Por favor, insira o nome do livro: ')
    dicionario['autor'] = input('Por favor, insira o autor do livro: ')
    dicionario['editora'] = input('Por favor, insira a editora do livro: ')

    # G. Insere uma cópia do dicionário dentro da lista de livros
    lista_livros.append(dicionario.copy())

# D. Função para consultar livros com submenu de opções
def consultar_livro():
    while True:
        print('MENU CONSULTAR LIVRO')
        print('1 - Consultar todos os livros')
        print('2 - Consultar livros por Id')
        print('3 - Consultar livros por autor')
        print('4 - Retornar')
        escolha_consultar = input('Escolha a opção desejada: ')

        # i. Consulta todos os livros cadastrados
        if escolha_consultar == '1':
            for livro in lista_livros:
                print(livro)

        # ii. Consulta específica por ID do livro
        elif escolha_consultar == '2':
            qual_id = int(input('Por favor, insira o id do livro: '))
            for livro in lista_livros:
                if livro['id'] == qual_id:
                    print(livro)

        # iii. Consulta por autor do livro
        elif escolha_consultar == '3':
            qual_autor = input('Por favor, insira o autor do livro: ')
            for livro in lista_livros:
                if livro['autor'] == qual_autor:
                    print(livro)

        # iv. Retorna ao menu principal
        elif escolha_consultar == '4':
            return

        # v. Para opção inválida no menu de consulta
        else:
            print('Opção inválida. Tente novamente.')


# E. Função para remover um livro com base no ID
def remover_livro():
    print('MENU REMOVER LIVRO')
    while True:
        qual_id = int(input('Digite o id do livro para ser removido: '))
        encontrado = False

        for livro in lista_livros:
            if livro['id'] == qual_id:
                lista_livros.remove(livro)
                encontrado = True
                print('Livro removido com sucesso!')
                break
        if encontrado:
            return  # remoção deu certo, volta ao menu principal

        # Caso o ID não pertença a nenhum livro da lista
        else:
            print('Id inválido. Tente novamente.')
            continue  # repete a pergunta do id

# F. Estrutura de menu principal
while True:
    escolha_principal = input('Escolha a opção desejada: ')
    if escolha_principal == '1':
        cadastrar_livro(id_global)
        id_global += 1
    elif escolha_principal =='2':
        consultar_livro()
    elif escolha_principal =='3':
        remover_livro()
    elif escolha_principal =='4':
        break
    else:
        print('Opção inválida.')
        continue
