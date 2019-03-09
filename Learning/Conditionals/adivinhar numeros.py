#jogador1
print('jogador 1, digite um numero')
numero1=int(input())
if numero1 < 0 or numero1 > 100:
    print('Os numeros devem estar entre 0 e 100. digite novamente!')
    numero1=int(input())
    
print('digite outro numero')
numero2=int(input())
if numero2 < 0 or numero2 > 100:
    print("digite um numero entre 0 e 100")
    numero2=int(input())
if numero1 > numero2:
    numeromaior=numero1
    numeromenor=numero2
else:
    numeromaior=numero2
    numeromenor=numero1
#jogador2
print('jogador2 tente adivinhar um dos numeros que o jogador 2 escolheu')
palpite=int(input())

if palpite > numeromenor and palpite < numeromaior:
    print('o seu palpite está entre os dois numeros do jogador 1')
elif palpite < numeromenor:
    print('o seu palpite é menor que o menor numero do jogador 1')
elif palpite > numeromaior:
    print('o seu palpite é maior que o maior numero do jogador 1')
else:
    print("voce acertou. parabéns")
    exit(0)

print('qual o seu outro palpite?')
palpite=int(input())

if palpite > numeromenor and palpite < numeromaior:
    print('o seu palpite está entre os dois numeros do jogador 1')
elif palpite < numeromenor:
    print('o seu palpite é menor que o menor numero do jogador 1')
elif palpite > numeromaior:
    print('o seu palpite é maior que o maior numero do jogador 1')
else:
    print("voce acertou. parabéns")
    exit(0)

print("Sua ultima chance?")
palpite=int(input())
            
if palpite > numeromenor and palpite < numeromaior:
    print('o seu palpite está entre os dois numeros do jogador 1')
elif palpite < numeromenor:
    print('o seu palpite é menor que o menor numero do jogador 1')
elif palpite > numeromaior:
    print('o seu palpite é maior que o maior numero do jogador 1')
else:
    print("voce acertou. parabéns")
    exit(0)
