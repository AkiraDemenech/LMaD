# biblioteca para gerar valores aleatórios*
import random 

porta_premiada = random.randint(1,3) # é escolhido um inteiro no intervalo fechado [1,3]
print('Spoiler: está na porta',porta_premiada) # exibição antecipada do número escolhido 

print('\nVocê escolhe a porta 1, 2 ou 3?')
porta_escolhida = int(input()) # espera-se que a entrada seja um inteiro válido e que seja 1, 2 ou 3

# por simplicidade, este algoritmo não verifica se houve erro na inserção do número da porta 

if porta_premiada == 1:
	if porta_escolhida == 1:
		abertura = random.randint(0,1)
		porta_aberta = 2 + abertura # pode abrir tanto a 2 quanto a 3, nenhuma tem o prêmio, nem foi escolhida inicialmente     
		porta_fechada = 3 - abertura # 2 + (1 - abertura)

		print('\nA porta',porta_aberta,'está aberta e o prêmio não está atrás dela.')
		print('Quer manter a porta 1 ou trocar para a porta',porta_fechada,'?')

		porta_escolhida_final = int(input()) # espera-se que a entrada seja um inteiro válido e que seja uma das duas portas ainda fechadas  

		if porta_escolhida_final == 1:
			print('Parabéns! Você ganhou o prêmio atrás da porta 1 :D')
		else:	
			print('Porta errada. O prêmio estava na porta 1 :C')

	elif porta_escolhida == 2:
		
		print('\nA porta 3 está aberta e o prêmio não está atrás dela.')
		print('Quer manter a porta 2 ou trocar para a porta 1 ?')

		porta_escolhida_final = int(input()) # espera-se que a entrada seja um inteiro válido e que seja uma das duas portas ainda fechadas  

		if porta_escolhida_final == 1:
			print('Parabéns! Você ganhou o prêmio atrás da porta 1 :D')
		else:	
			print('Porta errada. O prêmio estava na porta 1 :C')		

	elif porta_escolhida == 3:
		
		print('\nA porta 2 está aberta e o prêmio não está atrás dela.')
		print('Quer manter a porta 3 ou trocar para a porta 1 ?')

		porta_escolhida_final = int(input()) # espera-se que a entrada seja um inteiro válido e que seja uma das duas portas ainda fechadas  

		if porta_escolhida_final == 1:
			print('Parabéns! Você ganhou o prêmio atrás da porta 1 :D')
		else:	
			print('Porta errada. O prêmio estava na porta 1 :C')		

elif porta_premiada == 2:
	if porta_escolhida == 1:
		
		print('\nA porta 3 está aberta e o prêmio não está atrás dela.')
		print('Quer manter a porta 1 ou trocar para a porta 2 ?')

		porta_escolhida_final = int(input()) # espera-se que a entrada seja um inteiro válido e que seja uma das duas portas ainda fechadas  

		if porta_escolhida_final == 2:
			print('Parabéns! Você ganhou o prêmio atrás da porta 2 :D')
		else:	
			print('Porta errada. O prêmio estava na porta 2 :C')		

	elif porta_escolhida == 2:
		
		abertura = 2 * random.randint(0,1)
		porta_aberta = 1 + abertura # pode abrir tanto a 1 quanto a 3, nenhuma tem o prêmio, nem foi escolhida inicialmente     
		porta_fechada = 3 - abertura # 1 + (2 - abertura)

		print('\nA porta',porta_aberta,'está aberta e o prêmio não está atrás dela.')
		print('Quer manter a porta 2 ou trocar para a porta',porta_fechada,'?')

		porta_escolhida_final = int(input()) # espera-se que a entrada seja um inteiro válido e que seja uma das duas portas ainda fechadas  

		if porta_escolhida_final == 2:
			print('Parabéns! Você ganhou o prêmio atrás da porta 2 :D')
		else:	
			print('Porta errada. O prêmio estava na porta 2 :C')

		

	elif porta_escolhida == 3:
		
		print('\nA porta 1 está aberta e o prêmio não está atrás dela.')
		print('Quer manter a porta 3 ou trocar para a porta 2 ?')

		porta_escolhida_final = int(input()) # espera-se que a entrada seja um inteiro válido e que seja uma das duas portas ainda fechadas  

		if porta_escolhida_final == 2:
			print('Parabéns! Você ganhou o prêmio atrás da porta 2 :D')
		else:	
			print('Porta errada. O prêmio estava na porta 2 :C')

elif porta_premiada == 3:
	if porta_escolhida == 1:
		
		print('\nA porta 2 está aberta e o prêmio não está atrás dela.')
		print('Quer manter a porta 1 ou trocar para a porta 3 ?')

		porta_escolhida_final = int(input()) # espera-se que a entrada seja um inteiro válido e que seja uma das duas portas ainda fechadas  

		if porta_escolhida_final == 3:
			print('Parabéns! Você ganhou o prêmio atrás da porta 3 :D')
		else:	
			print('Porta errada. O prêmio estava na porta 3 :C')		

	elif porta_escolhida == 2:
		
		
		print('\nA porta 1 está aberta e o prêmio não está atrás dela.')
		print('Quer manter a porta 3 ou trocar para a porta 2 ?')

		porta_escolhida_final = int(input()) # espera-se que a entrada seja um inteiro válido e que seja uma das duas portas ainda fechadas  

		if porta_escolhida_final == 3:
			print('Parabéns! Você ganhou o prêmio atrás da porta 3 :D')
		else:	
			print('Porta errada. O prêmio estava na porta 3 :C')			
		

	elif porta_escolhida == 3:
		
		abertura = random.randint(0,1)
		porta_aberta = 1 + abertura # pode abrir tanto a 1 quanto a 3, nenhuma tem o prêmio, nem foi escolhida inicialmente     
		porta_fechada = 2 - abertura # 1 + (1 - abertura)

		print('\nA porta',porta_aberta,'está aberta e o prêmio não está atrás dela.')
		print('Quer manter a porta 3 ou trocar para a porta',porta_fechada,'?')

		porta_escolhida_final = int(input()) # espera-se que a entrada seja um inteiro válido e que seja uma das duas portas ainda fechadas  

		if porta_escolhida_final == 3:
			print('Parabéns! Você ganhou o prêmio atrás da porta 3 :D')
		else:	
			print('Porta errada. O prêmio estava na porta 3 :C')

		

#	*	os valores gerados são pseudoaleatórios e a biblioteca usa distribuição uniforme   		