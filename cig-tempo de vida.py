print('Quanto tempo de vida e perdido para o cigarro?')
print()
cig = int(input('Quantos cigarros por dia? '))
print()
tempo = int(input('Por quantos anos? '))
dias = (tempo*365*cig)/144
print()
print(f'Foram {dias:.0f} dias perdidos.')
