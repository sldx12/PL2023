import pprint

def main():
	while True:
		print("1 - calcular a frequência de processos por ano\n2 - calcular a frequência de nomes próprios e apelidos por séculos e apresentar os 5 mais usados\n3 - calcular a frequência dos vários tipos de relação\n4 - converter os 20 primeiros registos num novo ficheiro de output em formato json")
		o = int(input("> "))

		with open('processos.txt', 'r') as p:
			linhas = p.readlines()
			linhas.pop()
	
		if o in [1,2,3,4]:
			if o == 1:
				freq_ano = {}

				for linha in linhas:
					ano = linha.split('::')[1].split('-')[0]
					#print(linha.split('::')[1])
					if ano in freq_ano:
						freq_ano[ano] += 1
					else:
						freq_ano[ano] = 1

				freq_ano_s = list(freq_ano.items())
				freq_ano_s.sort(key=lambda x: x[1], reverse=True)

				for key, value in freq_ano_s:
					print(f"{key}: {value}")

			if o == 2:
				freq_nome = {}
				freq_apelido = {}

if __name__ == "__main__":
	main()
