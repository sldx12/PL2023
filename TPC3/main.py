import pprint
import json

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
					if ano in freq_ano:
						freq_ano[ano] += 1
					else:
						freq_ano[ano] = 1

				freq_ano_s = list(freq_ano.items())
				freq_ano_s.sort(key=lambda x: x[1], reverse=True)

				for key, value in freq_ano_s:
					print(f"{key}: {value}")

			if o == 2:
				nomes = {}
				apelidos = {}

				for linha in linhas:
					ano = int(linha.split('::')[1].split('-')[0])
					if ano % 100 == 0:
						seculo = ano // 100
					else:
						seculo = (ano // 100) + 1

					nome = linha.split('::')[2].split(' ')[0]
					apelido = linha.split('::')[2].split(' ')[-1]

					if seculo not in nomes:
						nomes[seculo] = {}
						apelidos[seculo] = {}

					if nome in nomes[seculo]:
						nomes[seculo][nome] += 1
					else:
						nomes[seculo][nome] = 1

					if apelido in apelidos[seculo]:
						apelidos[seculo][apelido] += 1
					else:
						apelidos[seculo][apelido] = 1

				pprint.pprint(nomes)
	
			if o == 4:
				output = []
				vinte = linhas[0:20]

				for item in vinte:
					campos = item.strip().split('::')

					op = {
						'Pasta': campos[0],
						'Data': campos[1],
						'Nome': campos[2],
						'Pai': campos[3],
						'Mae': campos[4],
						'Obs': campos[5],
						'Obs2': campos[6]
					}

					output.append(op)

				final = json.dumps(output, indent=2)
				with open('processos.json', 'w') as j:
					j.write(final)

				print("\nFeito!\n")

		else:
			print("\nOpção inválida.\n")

if __name__ == "__main__":
	main()
