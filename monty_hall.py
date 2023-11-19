import random
TROCA = True	# Se você troca de porta depois de Monty Hall revelar cabras
ABERTAS = 1	# quantidade de portas (com cabras) que Monty Hall abre depois de você escolher
CARROS = 1	# quantidade de carros (prêmios) atrás das portas 
CABRAS = 2	# quantidade de cabras (portas sem prêmios)

def monty_hall (troca = TROCA, cabras = CABRAS, carros = CARROS, abertas = ABERTAS):
	portas = [False] * (cabras + carros)
	
	print('\nCarros:')
	while carros:
		c = random.randint(0, len(portas) - 1)
		print(c, '\t', portas[c])
		carros -= not portas[c]
		portas[c] = True
	print(portas)	
		
	escolha = random.randint(0,len(portas)-1)
	escolhida = portas.pop(escolha)			
	
	while abertas and sum(portas) < len(portas):
		a = random.randint(0, len(portas) - 1)
		if portas[a]:
			continue
		portas.pop(a)	
		abertas -= 1
	print('\nEscolha:',escolha,'\t',escolhida,'\nFechadas:',portas)	
	if troca:	
		escolhida = portas[random.randint(0, len(portas) - 1)]
	print(escolhida)	
	
	return escolhida
	
n = 1000	
for t,s in {
	(t, sum(monty_hall(t) for k in range(n)) / n) for t in {True, False}
}: 	
	print(('Manter', 'Trocar')[t], '\t', s * 100)
	
	