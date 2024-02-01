import os  # Importa o módulo os para interagir com o sistema operacional

# Lista inicial de restaurantes
restaurantes = ['Pizza', 'Sushi']

# Função para exibir o nome do programa em formato ASCII Art
def exibir_nome_do_programa():
    print("...")  # ASCII Art para o nome do programa

# Função para exibir as opções do menu principal
def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

# Função para encerrar o aplicativo
def finalizar_app():
    exibir_subtitulo('Finalizar app')

# Função para voltar ao menu principal
def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu ')
    main()

# Função para lidar com opção inválida
def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

# Função para exibir um subtítulo
def exibir_subtitulo(texto):
    os.system('cls')  # Limpa a tela
    print(texto)
    print()

# Função para cadastrar um novo restaurante
def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)  # Adiciona o restaurante à lista
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

# Função para listar todos os restaurantes
def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes')
    for restaurante in restaurantes:
        print(f'.{restaurante}')
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
            print('Ativar restaurante')  # Ação para ativar restaurante (não implementada)
        elif opcao_escolhida == 4: 
            finalizar_app()  # Encerra o aplicativo
        else: 
            opcao_invalida()  # Caso a opção não seja válida
    except:
        opcao_invalida()  # Trata erro caso a entrada não seja um número

# Ponto de entrada do programa
def main():
    os.system('cls')  # Limpa a tela
    exibir_nome_do_programa()  # Exibe o nome do programa
    exibir_opcoes()  # Exibe as opções do menu
    escolher_opcao()  # Permite ao usuário escolher uma opção

# Verifica se o script é o módulo principal e executa o programa
if __name__ == '__main__':
    main()
