# Preencha a lista com os números mecanográficos dos autores.
import random
# Grupo P7C
AUTORES = [118745, 119773]

# Defina funções aqui.
# Esta função é executada após a "Aposta" do jogador estar incorreta.
def Wrong():
    global wrongCount
    wrongCount += 1
    wrongLettersList.append(guess)

    # Se o jogador ainda não tiver perdido todas as vidas...
    if wrongCount < 6:
        print(f"""
Letra errada, restam-lhe {6-wrongCount} tentativas!""")



# Esta função é executada quando a "Aposta" do jogador está correta [Agora falta verificar se é um caracter normal ou especial (com acentos)].
def Correct(guess, remainingLettersList):
    global correctCount

    # Este ciclo 'for' itera pelas várias letras do "secret".
    for i in range(len(secret)):

        # Este "if" verifica se o "guess" é igual ao caracter secret[i] do "secret" e se assim for, então revela-o na "secretListEncoded".
        if guess == secret[i]:
            secretListEncoded.insert(i, secret[i])
            secretListEncoded.pop(i+1)

        # Este "if" e ciclo "for" verifica se o "guess" é "A", "E", "I", "O", "U" ou "C", se for, então procura se no "secret" tem alguma letra equivalente a essa mas com acentos e revela essa letra na "secretListEncoded".
        if guess in ['A', 'E', 'I', 'O', 'U', 'C']:
            for a in range(len(['A', 'E', 'I', 'O', 'U', 'C'])):
                if (secret[i] and guess) in differentLettersList[a]:
                    for b in range(len(differentLettersList[a])):
                        if secret[i] == differentLettersList[a][b]:
                            secretListEncoded.insert(i, secret[i])
                            secretListEncoded.pop(i+1)
        
        # Este "if" evita que a mesma letra seja adicionada a "correctLettersList" mais do que uma vez.
        if guess not in correctLettersList:
            correctLettersList.append(guess)

    contador = 0
    # Este ciclo "for" conta todos os caracteres diferentes de "_" que encontrar na "secretEncodedList", ou seja, verifica quantos caracteres já foram revelados.
    for i in range(len(secretListEncoded)):
        if secretListEncoded[i] != "_":
            contador += 1
    # O contador final é resultado da diferença entre o número de caracteres revelados atualmente e o número de caracteres revelados antes da aposta, evitando assim que seja feita uma soma incorreta.
    contador_final = contador-correctCount
    correctCount += contador_final

    # Se a palavra ainda não tiver sido completamente revelada...
    if correctCount != len(secret):
        print(f"""
Letra correta, restam-lhe {6-wrongCount} tentativas!""")



# Esta função verifica a quantidade de "Apostas" erradas que o jogador fez e altera o visual da forca em função disso.
def WrongCountChecker(wrongCount, remainingLettersList):
    
    if wrongCount == 1:
        hangmanLine1[0] = "O"
    if wrongCount == 2:
        hangmanLine2[1] = "|"
    if wrongCount == 3:
        hangmanLine2[0] = "/"
    if wrongCount == 4:
        hangmanLine2[2] = "\\"
    if wrongCount == 5:
        hangmanLine3[0] = "/"
    if wrongCount == 6:
        hangmanLine3[1] = "\\"

    print(f""" _____
|     |
|     {hangmanLine1[0]}
|    {hangmanLine2[0]+hangmanLine2[1]+hangmanLine2[2]}
|    {hangmanLine3[0]} {hangmanLine3[1]}
|_______
ERROS: {wrongCount}

{" ".join(secretListEncoded)}

Letras Corretas: {", ".join(correctLettersList)}
Letras Erradas: {", ".join(wrongLettersList)}
Letras Restantes: {", ".join(remainingLettersList)}
_________________________________________________________________________________________________________________________________""")



# Esta função é usada no fim do código para saber se o jogador pretende jogar outra vez ou não.
def PlayAgain():
    playAgain = input("""
                                                   Quer tentar outra vez? (s/n) """).strip().lower()
    while playAgain not in ("s", "n"):
        print("""
                                                    ___________________________
              
                                                       Comando desconhecido.
                                                    ___________________________
""")
        playAgain = input("""
                                                   Quer tentar outra vez? (s/n) """).strip().lower()
    if playAgain == "s":
        return True
    else:
        return False



def main():
    menuOption = input(""" ________________________________________________________________________________________________________________________________
|      __     ______     ______     ______        _____     ______        ______   ______     ______     ______     ______       |
|     /\ \   /\  __ \   /\  ___\   /\  __ \      /\  __-.  /\  __ \      /\  ___\ /\  __ \   /\  == \   /\  ___\   /\  __ \      |
|    _\_\ \  \ \ \/\ \  \ \ \__ \  \ \ \/\ \     \ \ \/\ \ \ \  __ \     \ \  __\ \ \ \/\ \  \ \  __<   \ \ \____  \ \  __ \     |
|   /\_____\  \ \_____\  \ \_____\  \ \_____\     \ \____-  \ \_\ \_\     \ \_\    \ \_____\  \ \_\ \_\  \ \_____\  \ \_\ \_\    |
|   \/_____/   \/_____/   \/_____/   \/_____/      \/____/   \/_/\/_/      \/_/     \/_____/   \/_/ /_/   \/_____/   \/_/\/_/    |
|________________________________________________________________________________________________________________________________|         

                                  ____                         _           _        __   __   _ 
                                 |  _ \                       (_)         | |      / /   \ \ | |
                                 | |_) | ___ _ __ ___   __   ___ _ __   __| | ___ | | __ _| || |
                                 |  _ < / _ \ '_ ` _ \  \ \ / / | '_ \ / _` |/ _ \| |/ _` | || |
                                 | |_) |  __/ | | | | |  \ V /| | | | | (_| | (_) | | (_| | ||_|
                                 |____/ \___|_| |_| |_|   \_/ |_|_| |_|\__,_|\___/| |\__,_| |(_)
                                                                                   \_\   /_/     
              
                                                          -------------- 
                                                         |     Menu     |
                                                         |              |
                                                         |  1 - Jogar   |
                                                         |  2 - Regras  |
                                                         |  3 - Sair    |
                                                          --------------

                                                             Comando: """).strip()
    while menuOption not in ("1", "2", "3"):
        print("""
                                                    ___________________________
              
                                                       Comando desconhecido.
                                                    ___________________________
""")
        menuOption = input("""                                                             Comando: """).strip()

    if menuOption == "2":
        menuOption = input("""
 ________________________________________________________________________________________________________________________________
                                                  _____                          
                                                 |  __ \                         
                                                 | |__) |___  __ _ _ __ __ _ ___ 
                                                 |  _  // _ \/ _` | '__/ _` / __|
                                                 | | \ \  __/ (_| | | | (_| \__ \\
                                                 |_|  \_\___|\__, |_|  \__,_|___/
                                                              __/ |              
                                                             |___/      
                           
 No jogo da forca, o jogador tem de adivinhar uma palavra que inicialmente é apresentada com cada letra substituída por um traço.
                               Em cada jogada, o jogador escolhe uma letra do alfabeto para apostar.
                                Se a letra ocorrer na palavra, todas as ocorrências são reveladas.
                                             Se a letra não ocorrer, conta-se o erro.
  O jogo acaba quando se adivinham e revelam todas as letras da palavra ou quando se atinge um certo número de jogadas erradas.
       A cada jogada errada acrescenta-se um elemento ao boneco da forca. A figura completa significa que o jogador perde.

                                                             Exemplo:
                  
                                             Se a palavra sorteada for "INFORMÁTICA"
                  
                                                  O jogo vai apresentá-la como:
                                                      _ _ _ _ _ _ _ _ _ _ _

                                     Se o jogador apostar uma letra correta, por exemplo "A",
                                   o jogo vai revelar 2 caracteres da palavra, mostrando assim:
                                                      _ _ _ _ _ _ Á _ _ _ A

                                    Se o jogador apostar uma letra incorreta, por exemplo "L",
                                    o jogo vai acrescentar um elemento ao boneco da forca:

                              _____       _____        _____        _____        _____        _____
                             |     |     |     |      |     |      |     |      |     |      |     |
                             |     O     |     O      |     O      |     O      |     O      |     O
                             |           |     |      |    /|      |    /|\     |    /|\     |    /|\\
                             |           |            |            |            |    /       |    / \\
                             |_______    |_______     |_______     |_______     |_______     |_______
                             ERROS: 1    ERROS: 2     ERROS: 3     ERROS: 4      ERROS:5     ERROS: 6
                               
 ________________________________________________________________________________________________________________________________
                              
                                                       Deseja jogar? (s/n) """).lower().strip()
        while menuOption not in ("s", "n"):
            print("""
                                                    ___________________________
              
                                                       Comando desconhecido.
                                                    ___________________________
""")
            menuOption = input("""
                                                       Deseja jogar? (s/n) """).lower().strip()
        if menuOption != "s":
                exit()

    if menuOption == "3":
        exit()
    
    # Este "while" faz com que o jogo receba um reset em todas as variáveis para que um novo jogo possa começar.
    while True:
        from wordlist import words1, words2

        # Descomente a linha que interessar para testar
        # words = words1              # palavras sem acentos nem cedilhas.
        # words = words2             # palavras com acentos ou cedilhas.
        words = words1 + words2    # palavras de ambos os tipos

        # Complete o programa
        # Variáveis globais
        global secret
        global guess
        global correctCount
        global wrongCount
        global hangmanLine1
        global hangmanLine2
        global hangmanLine3
        global secretListEncoded
        global differentLettersList
        global wrongLettersList
        global correctLettersList

        import sys                  # INCLUA estas 3 linhas para permitir
        if len(sys.argv) > 1:       # correr o programa com palavras dadas:
            words = sys.argv[1:]    #   python3 forca.py duas palavras

        # Escolhe palavra aleatoriamente
        secret = random.choice(words).upper()

        # Defini listas e variáveis aqui para que fossem tomadas como globais durante todo o código
        secretList = []
        secretListEncoded = []
        wrongLettersList = []
        correctLettersList = []
        remainingLettersList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        differentLettersList = [['A', 'Á', 'À', 'Ã', 'Â'], ['E', 'É', 'È', 'Ê'], ['I', 'Í', 'Ì', 'Î'], ['O', 'Ó', 'Ò', 'Õ', 'Ô'], ['U', 'Ú', 'Ù', 'Û'], ['C', 'Ç']]

        # Estas listas dizem apenas respeito às linhas do corpo do boneco e apenas vão ter como variavéis strings com as partes do corpo, como segue na figura:
        # hangmanLine 1 = ['O']
        # hangmanLine 2 = ['/', '|', '\']
        # hangmanLine 3 = ['/', '\']

        hangmanLine1 = ['']
        hangmanLine2 = [' ', '', '']
        hangmanLine3 = ['', '']

        wrongCount = 0
        correctCount = 0

        # Este ciclo 'for' separa a palavra em letras numa lista, por exemplo, a string 'JOÃO' ficaria secretList = ['J', 'O', 'Ã', 'O']
        for i in range(len(secret)):
            secretList.append(secret[i])
            secretListEncoded.append("_")
            
        print("""
                                                    Uma palavra foi sorteada!
                                                            Boa sorte!""")
        
        # Este ciclo 'while' repete-se enquanto a pessoa não errar 6 vezes ou então enquanto não tiver acertado as letras todas.
        while wrongCount != 6 and correctCount != len(secret):
            # Este "if" inicial é para dar print da forca inicial sem que, a partir da primeira jogada ela se repita 2 vezes, visto que há outro WrongCountChecker no fim do código.
            if len(remainingLettersList) == 26:
                WrongCountChecker(wrongCount, remainingLettersList)

            guess = input("""
Aposta? """).strip().upper()
            # Este ciclo 'while' "obriga" o jogador a dar input de letra sem acentos
            while guess not in remainingLettersList:
                if guess in wrongLettersList or guess in correctLettersList:
                    print("Esta letra já foi usada!")
                elif guess == "":
                    print("O seu input não pode ser vazio!")
                elif len(guess) > 1:
                    print("Não introduza mais do que um caráter ao mesmo tempo!")
                else:
                    print("O seu input é inválido!")

                guess = input("""
Aposta? """).upper().strip()

            remainingLettersList.remove(guess)

            # Se o "guess" (sem acento) estiver na palavra, então Correct()
            if guess in secretList:
                Correct(guess, remainingLettersList)

            # Este "if" e ciclo "for" verifica se o "guess" é "A", "E", "I", "O", "U" ou "C", se for, então procura se no "secret" tem alguma letra equivalente a essa mas com acentos e chama Correct()
            elif guess in ['A', 'E', 'I', 'O', 'U', 'C']:
                for i in range(len(secret)):
                    for a in range(len(['A', 'E', 'I', 'O', 'U', 'C'])):
                        if guess in ['A', 'E', 'I', 'O', 'U', 'C'][a]:
                            if secret[i] in [['Á', 'À', 'Ã', 'Â'], ['É', 'È', 'Ê'], ['Í', 'Ì', 'Î'], ['Ó', 'Ò', 'Õ', 'Ô'], ['Ú', 'Ù', 'Û'], ['Ç']][a]:
                                Correct(guess, remainingLettersList)
                            # Este "if" verifica se, quando estivermos no fim da iteração, se o guess ainda não estiver na "correctLettersList", então é porque está errado, logo Wrong()
                            if i == len(secret)-1 and guess not in correctLettersList:
                                Wrong()

            # Se o "guess" não validar nenhum "if" acima, então é porque está errado, logo Wrong()
            else:
                Wrong()

            # Atualiza vários dados após a jogada
            if wrongCount != 6 and correctCount != len(secret):
                WrongCountChecker(wrongCount, remainingLettersList)

        if wrongCount == 6:
            print(f""" ________________________________________________________________________________________________________________________________
                  
                               __________________________________________________________________
                              |    _____          __  __ ______    ______      ________ _____    |
                              |   / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \   |
                              |  | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |  |
                              |  | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  /   |
                              |  | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \   |
                              |   \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\  |
                              |__________________________________________________________________|          
                  
 ________________________________________________________________________________________________________________________________
 _____
|     |
|     {hangmanLine1[0]}
|    {hangmanLine2[0]+hangmanLine2[1]+hangmanLine2[2]}
|    {hangmanLine3[0]} \\
|_______

{" ".join(secretListEncoded)}
""")
            print(f"Você perdeu! A palavra correta era {secret}.")
        
        if correctCount == len(secret):
            print(f""" ________________________________________________________________________________________________________________________________

                                                  ______________________________
                                                 |  __          _______ _   _   |
                                                 |  \ \        / /_   _| \ | |  |
                                                 |   \ \  /\  / /  | | |  \| |  |
                                                 |    \ \/  \/ /   | | | . ` |  |
                                                 |     \  /\  /   _| |_| |\  |  |
                                                 |      \/  \/   |_____|_| \_|  |
                                                 |______________________________|
 _____
|     |
|     {hangmanLine1[0]}
|    {hangmanLine2[0]+hangmanLine2[1]+hangmanLine2[2]}
|    {hangmanLine3[0]} {hangmanLine3[1]}
|_______

{" ".join(secretListEncoded)}
""")
            print(f"Parabéns! Você ganhou com {wrongCount} letras erradas!")

        if not PlayAgain():
            exit()

if __name__ == "__main__":
    main()
