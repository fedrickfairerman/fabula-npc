classes_disponiveis = ['Necromante', 'Mago', 'Guerreiro', 'Paladino', 'Ladino']
racas_disponiveis = ['Humano', 'Gnomo', 'Orc', 'Anão', 'Elfo']

def exibir_opcoes():
    print('1 - Montar Personagem')
    print('2 - Ver Classes')
    print('3 - Ver Raças')
    print('4 - Adicionar Classe Nova')
    print('5 - Adicionar Raça Nova')

def escolhendo_a_classe():
    escolha_classe = input('Escolha a Classe do seu personagem ').capitalize()
    classe_escolhida = None
    for classe in classes_disponiveis:
        if escolha_classe == classe:
            classe_escolhida = classe
            break
    if classe_escolhida:
            print(f'Você escolheu a classe {classe_escolhida} para seu personagem')
            return classe_escolhida
    else:
        print('A classe não existe em nossa lista')
        return escolhendo_a_classe()
        escolhendo_a_classe()
def escolhendo_a_raca():
    escolha_raca = input('Escolha Raça do seu personagem ').capitalize()
    raca_escolhida = None
    for raca in racas_disponiveis:
        if escolha_raca == raca:
            raca_escolhida = raca
            break
    if raca_escolhida:
            print(f'Você escolheu a raça {raca_escolhida} para seu personagem')
            return raca_escolhida
    else:
        print('A raça não existe em nossa lista')
        return escolhendo_a_raca()
        escolhendo_a_raca()

def montar_personagem():
    classe_final = escolhendo_a_classe()
    raca_final = escolhendo_a_raca()
    nome_do_personagem = input('Diga o nome do seu personagem ')
    print(f'Você é {nome_do_personagem}, um(a){classe_final}, da raça {raca_final}')


def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opcção '))
    
        if opcao_escolhida == 1:
            montar_personagem()
        elif opcao_escolhida == 2:
            print(classes_disponiveis)
        elif opcao_escolhida == 3:
            print(racas_disponiveis)
        elif opcao_escolhida == 4:
            add_classe = input('Digite uma classe nova ')
            classes_disponiveis.append(add_classe)
            print(f'As classes novas são: {classes_disponiveis}')
            exibir_opcoes()
            escolher_opcao()
        elif opcao_escolhida == 5:
            add_raca = input('Digite uma raça nova ')
            racas_disponiveis.append(add_raca)
            print(f'As racas novas são: {racas_disponiveis}')
            exibir_opcoes()
            escolher_opcao()
    except:
        print('Opcao Invalida')
        exibir_opcoes()
        escolher_opcao()

def intro():
    print('Bem vindo a criação de Personagem')
    print('O que você deseja fazer?')
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    intro()