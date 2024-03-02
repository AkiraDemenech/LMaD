# biblioteca para gerar valores aleatórios*
import random 

porta_premiada = random.randint(1,3) # é escolhido um inteiro no intervalo fechado [1,3]
print('Spoiler: está na porta',porta_premiada) # exibição antecipada do número escolhido 

print('\nVocê escolhe a porta 1, 2 ou 3?')
porta_escolhida = int(input()) # espera-se que a entrada seja um inteiro válido e que seja 1, 2 ou 3

# por simplicidade, este algoritmo não verifica se houve erro na inserção do número da porta, caso não seja, haverá problemas  

porta_fechada = porta_premiada # quando a porta premiada não for escolhida, ela continua fechada e a outra vazia é aberta **

if porta_premiada == 1:
	if porta_escolhida == 1:
		abertura = random.randint(0,1)
		porta_aberta = 2 + abertura # pode abrir tanto a 2 quanto a 3, nenhuma tem o prêmio, nem foi escolhida inicialmente     
		porta_fechada = 3 - abertura # 2 + (1 - abertura)		

	elif porta_escolhida == 2:		
		porta_aberta = 3
		#porta_fechada = 1		

	elif porta_escolhida == 3:		
		porta_aberta = 2
		#porta_fechada = 1		

elif porta_premiada == 2:
	if porta_escolhida == 1:		
		porta_aberta = 3
		#porta_fechada = 2		

	elif porta_escolhida == 2:		
		abertura = 2 * random.randint(0,1)
		porta_aberta = 1 + abertura # pode abrir tanto a 1 quanto a 3, nenhuma tem o prêmio, nem foi escolhida inicialmente     
		porta_fechada = 3 - abertura # 1 + (2 - abertura)				

	elif porta_escolhida == 3:		
		porta_aberta = 1
		#porta_fechada = 2

elif porta_premiada == 3:
	if porta_escolhida == 1:		
		porta_aberta = 2
		#porta_fechada = 3		

	elif porta_escolhida == 2:				
		porta_aberta = 1
		#porta_fechada = 3					

	elif porta_escolhida == 3:		
		abertura = random.randint(0,1)
		porta_aberta = 1 + abertura # pode abrir tanto a 1 quanto a 3, nenhuma tem o prêmio, nem foi escolhida inicialmente     
		porta_fechada = 2 - abertura # 1 + (1 - abertura)

# não é mais necessário continuar dentro das condicionais porque as variáveis representam perfeitamente o estado agora sem mais necessidade de escolhas do programa		

print('\nA porta',porta_aberta,'está aberta e o prêmio não está atrás dela.')
print('Quer manter a porta',porta_escolhida,'ou trocar para a porta',porta_fechada,'?')

porta_escolhida_final = int(input()) # espera-se que a entrada seja um inteiro válido e que seja uma das duas portas ainda fechadas  

if porta_escolhida_final == porta_premiada:
	print('Parabéns! Você ganhou o prêmio atrás da porta',porta_premiada,':D')
else:	
	print('Porta errada. O prêmio estava na porta',porta_premiada,':C')
		

#	*	os valores gerados são pseudoaleatórios e a biblioteca usa distribuição uniforme   		
#	**	quando a porta premiada é escolhida, ela também continua fechada e uma das duas outras vazias é aberta 	