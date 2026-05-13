imu = []
vul = []
resist = []
absorb = []
vul_num = 0
cond_imu = []

def exibir_opcao():
    print('1 - Soldado - NPC basico')
    print('2 - Elite - Um NPC mais perigoso')
    print('3 - Campeão - Um NPC Chefe, normalmente o Boss de alguma batalha epica!')

def tipo_criatura(nivel,wlp,dex,ins,vida,mp,defesa,defesamagica,classe,mult=1,):
    print('Escolha qual tipo a criatura irá ser: ')
    print('1 - Humanoide, ganha a Skill Equipment de graça')      
    print('2 - Monstro')
    print('3 - Constructo, imune a Poison, a condição Poisoned e resistente a Earth')
    print('4 - Demonio, resistente a dois tipos de dano a sua escolha')
    print('5 - Fera, começa com 4 Skills')
    print('6 - Elemental, imune a Poison, a um dano extra a escolha. Imune a status Poisoned ')
    print('7 - Planta, imune as condições Dazed, Shaken e Enraged, vulneravel a um dano a escolha sua')
    print('8 - Undead, imune a Dark e Poison, a Poisoned e vulneravel a Light')
    criatura = 'nada'
    skill_num = 0
    tipo_escolhido = int(input('Digite o numero 1-8'))
    if tipo_escolhido == 1:
            criatura = 'Humanoide'
    elif tipo_escolhido == 2:
            criatura = 'Monstro'
    elif tipo_escolhido == 3:
            criatura = 'Constructo'
            imu.append('Poison')
            resist.append('Earth')
            cond_imu.append('Poisoned')
    elif tipo_escolhido == 4:
            criatura = 'Demonio'
            demon_new_resist_1 = input('Escolha um novo tipo de dano que ele será Resistente: Fire, Earth, Ice, Air, Physical, Light, Dark, Bolt, Poison: ')
            demon_new_resist_2 = input('Escolha um novo tipo de dano que ele será Resistente: Fire, Earth, Ice, Air, Physical, Light, Dark, Bolt, Poison: ')
            resist.extend([demon_new_resist_1, demon_new_resist_2])
    elif tipo_escolhido == 5:
            criatura = 'Fera'
            skill_num += 4
    elif tipo_escolhido == 6:
            criatura = 'Elemental'
            elemental_new_imu = input('Escolha um novo tipo de dano que ele será Resistente: Fire, Earth, Ice, Air, Physical, Light, Dark, Bolt: ')
            imu.extend(['Poison',elemental_new_imu])
            cond_imu.append('Poisoned')
    elif tipo_escolhido == 7:
            criatura = 'Planta'
            cond_imu.extend(['Dazed','Shaken','Enraged'])
            new_plant_vul = input('Escolha um novo tipo de dano que ele será Vulneravel: Fire, Earth, Ice, Air, Physical, Light, Dark, Bolt, Poison: ')
            vul.append(new_plant_vul)
    elif tipo_escolhido == 8:
            criatura = 'Undead'
            imu.extend(['Dark','Poison'])
            vul.append('Light')
    


def criar_elite():
    nivel = int(input('Informe o nivel do personagem '))
    wlp = int(input('Informe o dado de Willpower, diga 6, 8 ou 10 '))
    dex = int(input('Informe o dado de Dexterity, diga 6, 8 ou 10 '))
    ins = int(input('Informe o dado de Insight, diga 6, 8 ou 10'))
    mig = int(input('Informe o dado de Might, diga 6, 8 ou 10 '))
    vida = ((nivel * 2) + (mig * 5)) * 2
    mp = nivel + (ins * 5)
    defesa = dex
    defesamagica = wlp
    classe = 'elite'
    tipo_criatura(nivel,wlp,dex,ins,vida,mp,defesa,defesamagica,classe)
    

def criar_campeao():
    nivel = int(input('Informe o nivel do personagem '))
    wlp = int(input('Informe o dado de Willpower, diga 6, 8 ou 10 '))
    dex = int(input('Informe o dado de Dexterity, diga 6, 8 ou 10 '))
    ins = int(input('Informe o dado de Insight, diga 6, 8 ou 10'))
    mig = int(input('Informe o dado de Might, diga 6, 8 ou 10 '))
    mult = int(input('Quantos Soldados esse Campeão irá substituir? '))
    vida = ((nivel * 2) + (mig * 5)) * mult
    mp = (nivel + (ins * 5)) * 2
    defesa = dex
    defesamagica = wlp
    classe = 'campeão'
    tipo_criatura(nivel,wlp,dex,ins,vida,mp,defesa,defesamagica,classe,mult)

def criar_soldado():
    nivel = int(input('Informe o nivel do personagem '))
    wlp = int(input('Informe o dado de Willpower, diga 6, 8 ou 10 '))
    dex = int(input('Informe o dado de Dexterity, diga 6, 8 ou 10 '))
    ins = int(input('Informe o dado de Insight, diga 6, 8 ou 10'))
    mig = int(input('Informe o dado de Might, diga 6, 8 ou 10 '))
    vida = (nivel * 2) + (mig * 5)
    mp = nivel + (ins * 5)
    print(vida)
    print(mp)
    defesa = dex
    defesamagica = wlp
    classe = 'Soldado'
    tipo_criatura(nivel,wlp,dex,ins,vida,mp,defesa,defesamagica,classe)
    


def escolher_opcao():
    while True:
        try:
            opcao_escolhida = int(input('Digite o numero da opção '))
            if opcao_escolhida == 1:
                print('Vamos criar um Soldado!')
                criar_soldado()
            elif opcao_escolhida == 2:
                print('Vamos criar um Elite!')
                criar_elite()
                
            elif opcao_escolhida == 3:
                print('Vamos criar um Campeão!')
                criar_campeao()
                
            else:
                print('Opcão invalida!')
        except ValueError:
            print('Opção invalida! Digite apenas numeros')
            


def intro():
    print('Bem vindo ao criador de NPC de Fabula Ultima')
    print('Que tipo de NPC você irá criar?')
    exibir_opcao()
    escolher_opcao()


if __name__ == '__main__':
    intro()