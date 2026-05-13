imu = []
vul = []
resist = []
absorb = []
vul_num = 0
cond_imu = []


def escolher_opcao():
    while True:
        try:
            opcao_escolhida = int(input('Digite o numero da opção '))
            if opcao_escolhida in [1,2,3]:
                return opcao_escolhida
                
            else:
                print('Opcão invalida!')
        except ValueError:
            print('Opção invalida! Digite apenas numeros')


def exibir_opcao():
    print('1 - Soldado - NPC basico')
    print('2 - Elite - Um NPC mais perigoso')
    print('3 - Campeão - Um NPC Chefe, normalmente o Boss de alguma batalha epica!')

def intro():
    print('Bem vindo ao criador de NPC de Fabula Ultima')
    print('Que tipo de NPC você irá criar?')
    exibir_opcao()
    tipo = escolher_opcao()
    if tipo == 1:
        print('Iremos criar um soldado')
    elif tipo == 2:
        print('Iremos criar um Elite')
    elif tipo == 3:
        print('Iremos criar um Campeão')
    
    nivel = int(input('Informe o nivel do personagem '))
    wlp = int(input('Informe o dado de Willpower, diga 6, 8 ou 10 '))
    dex = int(input('Informe o dado de Dexterity, diga 6, 8 ou 10 '))
    ins = int(input('Informe o dado de Insight, diga 6, 8 ou 10 '))
    mig = int(input('Informe o dado de Might, diga 6, 8 ou 10 '))
    mp = (nivel + (ins * 5))
    init = 0
    skill_number = 0
    if tipo ==3:   
        mult = int(input('Quantos Soldados esse Campeão irá substituir? '))
    
    if tipo == 1:
        estilo = 'Soldado'
        vida = (nivel * 2) + (mig * 5)
    elif tipo == 2:
        estilo = 'Elite'
        vida = ((nivel * 2) + (mig * 5)) * 2
        init += 2
        skill_number = skill_number + 1
    elif tipo == 3:
         estilo = 'Campeão'
         vida = ((nivel * 2) + (mig * 5)) * mult
         mp = mp * 2
         init = init + mult
         skill_number = skill_number + mult
    crise = vida // 2
    skill_number += (nivel // 10)
    defesa = dex
    defesamagica = wlp
    iniciativa_final = ((dex + ins) // 2) + init
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
    tipo_escolhido = int(input('Digite o numero 1-8 '))
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
            skill_number += 4
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


    print("\n--- STATUS GERADOS ---")
    print(f'Você criou um {criatura} {estilo}' )
    print(f"Vida: {vida} Crise: {crise}| MP: {mp}")
    print(f"Defesa: {defesa} | Defesa Mágica: {defesamagica}")
    print(f"Iniciativa: {iniciativa_final}")
    print(f"Número de Skills: {skill_number}")
    print(f"Iniciativa: {iniciativa_final}")
    print("-" * 30)
    print(f"Imunidades: {', '.join(imu) if imu else 'Nenhuma'}")
    print(f"Resistências: {', '.join(resist) if resist else 'Nenhuma'}")
    print(f"Vulnerabilidades: {', '.join(vul) if vul else 'Nenhuma'}")
    print(f"Imunidade a Condições: {', '.join(cond_imu) if cond_imu else 'Nenhuma'}")
    print("=" * 30)

if __name__ == '__main__':
    intro()