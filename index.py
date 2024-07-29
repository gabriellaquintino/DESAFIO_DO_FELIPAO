heroi_name = "Ana"
xp = 8500

def nivel_heroi():
   
    if xp < 1000:
        nivel = "Ferro"
    elif 1001 <= xp <= 2000:
        nivel = "Bronze"
    elif 2001 <= xp <= 5000:
        nivel = "Prata"
    elif 5001 <= xp <= 7000:
        nivel = "Ouro"
    elif 7001 <= xp <= 8000:
        nivel = "Platina"
    elif 8001 <= xp <= 9000:
        nivel = "Ascendente"
    elif 9001 <= xp <= 10000:
        nivel = "Imortal"
    elif xp > 10000:
        nivel = "Radiante"
    else:
        nivel = "Desconhecido"

    print(f"O herói de nome {heroi_name} está no nível {nivel} com {xp} XP.")

nivel_heroi()



