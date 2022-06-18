# lista -> tabuleiro vazio
tabuleiro = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
# lista -> valores validos
valores_validos = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
input("Aperte Enter para continuar...")

# definir nome do jogador 1
player_1 = input("Player 1, digite seu nome: ")
#  definir nome do jogador 2
player_2 = input("Player 2, digite seu nome: ")

# variavel controladora para jogadas validas
controle = 0
# variavel controladora para o jogo
game_over = False

# variavel para controlar o turno
while True:
    # inicio da estrutura para verificar de quem é a vez 
    if controle % 2 == 0 and game_over == False:
        jogador = player_1 # jogador 1
        simbolo = "\033[31mX\033[m" # simbolo do jogador 1 -> X
    elif controle % 2 == 1 and game_over == False:
        jogador = player_2 # jogador 2
        simbolo = "\033[32mO\033[m" # simbolo do jogador 2 -> O
    # fim da estrutura para verificar de quem é a vez
    
    # template do tabuleiro já montado
    template = f"""
 {tabuleiro[0]} |  {tabuleiro[1]}  | {tabuleiro[2]} 
---+----+----
 {tabuleiro[3]} |  {tabuleiro[4]}  | {tabuleiro[5]} 
---+-----+----
 {tabuleiro[6]} |  {tabuleiro[7]}  | {tabuleiro[8]} 

"""
    print(template)
    # inicio da estrutura para verificar se já acabou o jogo
    if game_over:
        print("Fim de jogo!")
        print('Resultado do jogo: ', jogador)
        break
        
    print(f"Jogador: {jogador}")

    # fim da estrutura para verificar se já acabou o jogo
    
    # receber a jogada do jogador
    casa = input(f"{jogador} digite o número da casa: ")
    # verificar se o jogador digitou um valor errado, e não parar o jogo
    if casa in valores_validos:
        casa = int(casa) - 1 # transformar o valor da casa em index da lista inteiro
        # verificando se a casa já tá preenchida
        if tabuleiro[casa] == "\033[31mX\033[m" or tabuleiro[casa] == "\033[32mO\033[m":
            print("Já marcou essa casa ou é invalida!")
            continue
        else: 
        # marcar a casa
            tabuleiro[casa] = simbolo
            controle += 1

            # verificar se há vencedor
            if tabuleiro[0] == tabuleiro[1] == tabuleiro[2]:
                game_over = True
            if tabuleiro[3] == tabuleiro[4] == tabuleiro[5]:
                game_over = True
            if tabuleiro[6] == tabuleiro[7] == tabuleiro[8]:
                game_over = True
            if tabuleiro[0] == tabuleiro[3] == tabuleiro[6]:
                game_over = True
            if tabuleiro[1] == tabuleiro[4] == tabuleiro[7]:
                game_over = True
            if tabuleiro[2] == tabuleiro[5] == tabuleiro[8]:
                game_over = True
            if tabuleiro[0] == tabuleiro[4] == tabuleiro[8]:
                game_over = True
            if tabuleiro[2] == tabuleiro[4] == tabuleiro[6]:
                game_over = True
            # fim da verificação de vencedor

            if controle == 9 and not game_over:
                jogador = "Deu velha!"
                print('Resultado do jogo: ', jogador)
                game_over = True
                # while True:
                #     resposta = input("Deseja jogar novamente? (S/N) ")
                #     if resposta == "S":
                #         tabuleiro = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
                #         controle = 0
                #         game_over = False
                #         break

        
    else:
        print("Jogada inválida!")
        continue