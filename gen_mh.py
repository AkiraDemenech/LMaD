# biblioteca para gerar valores aleatórios*
import random 

p = 3 # quantidade de portas 
n = 1 # quantidade de prêmios 
m = p - n - 1 # quantidade de portas abertas pelo apresentador depois da primeira escolha de porta


portas_fechadas = list(range(1, 1 + p)) # a princípio, todas as portas estão fechadas 
portas_vazias = list(portas_fechadas) # e vazias   
portas_premiadas = [portas_vazias.pop(random.randint(0, len(portas_vazias) - 1)) for c in range(n)] # traz as portas para cá
portas_premiadas.sort() # para mostrar as portas em ordem

print('Spoiler: há prêmio em',*portas_premiadas,'e não em',*portas_vazias) # exibição antecipada do(s) número(s) escolhido(s) 

print('\nVocê escolhe:\t',*portas_fechadas)
porta_escolhida = int(input()) # espera-se que a entrada seja um inteiro válido em [1,p]

# por simplicidade, este algoritmo não verifica se houve erro ou repetição na inserção dos números das portas   


if porta_escolhida in portas_vazias:
	portas_vazias.remove(porta_escolhida) # não poderão ser abertas portas escolhidas, mesmo que vazias 
		
# quando as portas premiadas não forem escolhidas, elas continuam fechadas e outras vazias são abertas **
portas_abertas = [portas_vazias.pop(random.randint(0, len(portas_vazias) - 1)) for c in range(m)] # p - n - k > 0 		
portas_abertas.sort() 

for q in portas_abertas:
	portas_fechadas.remove(q)
		
print('\nNão há prêmio em',*portas_abertas)
print('Escolha:\t',*portas_fechadas)

porta_escolhida_final = int(input()) # espera-se que a entrada seja um inteiro válido, que esteja em [1,p] e ainda esteja fechada


if porta_escolhida_final in portas_premiadas:
	print('Parabéns! Você ganhou o prêmio atrás da porta',porta_escolhida_final,':D')
else:	
	print('Porta errada. Nada atrás de',porta_escolhida_final,':C')

#	*	os valores gerados são pseudoaleatórios e a biblioteca usa distribuição uniforme   		
#	**	quando as portas premiadas são escolhidas, elas também continuam fechadas e as outras vazias são abertas 	