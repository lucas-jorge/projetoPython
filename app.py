import os

# Lista de dicionários contendo informações sobre os restaurantes
restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False},
                {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]

# Função para exibir o nome do programa
def exibir_nome_do_programa():
    print("""
    # Arte ASCII representando o nome do programa
    """)

# Função para exibir as opções do menu
def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

# Função para finalizar o aplicativo
def finalizar_app():
    exibir_subtitulo('Finalizar app')

# Função para retornar ao menu principal
def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu ')
    main()

# Função para tratar opção inválida
def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

# Função para exibir um subtítulo
def exibir_subtitulo(texto):
    os.system('cls')  # Limpa a tela
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

# Função para cadastrar um novo restaurante
def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    # Solicita dados do restaurante
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    
    voltar_ao_menu_principal()

# Função para listar os restaurantes
def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes')
    # Exibe os restaurantes formatados
    print(f'{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

# Função para alternar o estado de ativação de um restaurante
def alternar_estado_restaurante():
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
            
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
            
    voltar_ao_menu_principal()

# Função para escolher uma opção do menu
def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1: 
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2: 
            listar_restaurantes()
        elif opcao_escolhida == 3: 
            alternar_estado_restaurante()
        elif opcao_escolhida == 4: 
            finalizar_app()
        else: 
            opcao_invalida()
    except:
        opcao_invalida()

# Função principal que inicia o programa
def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

# Verifica se o script é o ponto de entrada principal
if __name__ == '__main__':
    main()
