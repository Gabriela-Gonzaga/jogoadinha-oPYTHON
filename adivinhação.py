
print('bem-vindx ao jogo de adivinhação!')
print('funciona assim, vou executar um numero aleatoriamente')
print('e você vai precisar adivinhar qual numero é, beleza?')

from random import randint

numero1 = randint(0,5)

chute = int(input('Digite um numero de 0-5: '))

while(chute != numero1):
    print('Você errou tente novamente')
    chute = int(input('digite outro numero de 0-5: '))
else:
    print('parabens você acertou')
   
        

    
        
    
    



