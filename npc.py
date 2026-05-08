
def exibir_opcao():
    print('1 - Soldado - NPC basico')
    print('2 - Elite - Um NPC mais perigoso')
    print('3 - Campeão - Um NPC Chefe, normalmente o Boss de alguma batalha epica!')

def escolher_opcao():
    while True:
        try:
            opcao_escolhida = int(input('Digite o numero da opção '))
            if opcao_escolhida == 1:
                print('Vamos criar um Soldado!')
            elif opcao_escolhida == 2:
                print('Vamos criar um Elite!')
            elif opcao_escolhida == 3:
                print('Vamos criar um Campeão!')
            else:
                print('Opcão invalida!')
        except ValueError:
            print('Opção invalida! Digite apenas numeros')
            escolher_opcao()


def intro():
    print('Bem vindo ao criador de NPC de Fabula Ultima')
    print('Que tipo de NPC você irá criar?')
    exibir_opcao()
    escolher_opcao()


if __name__ == '__main__':
    intro()