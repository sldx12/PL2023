import pprint
import json
import re

def main():
	while True:
		print("1 - calcular a frequência de processos por ano\n2 - calcular a frequência de nomes próprios e apelidos por séculos e apresentar os 5 mais usados\n3 - calcular a frequência dos vários tipos de relação\n4 - converter os 20 primeiros registos num novo ficheiro de output em formato json")
		o = int(input("> "))

		with open('processos.txt', 'r') as p:
			linhas = p.readlines()
			linhas.pop()

		for i in linhas[:]:
			if len(i) < 2:
				linhas.remove(i)

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

				all_nomes = {}
				for s, ns in nomes.items():
					for n, f in ns.items():
						if n not in all_nomes:
							all_nomes[n] = {'frequencia': f, 'seculo': s}
						else:
							if f > all_nomes[n]['frequencia']:
								all_nomes[n]['frequencia'] = f
								all_nomes[n]['seculo'] = s

				s_names = sorted(all_nomes.keys(), key=lambda x: all_nomes[x]['frequencia'], reverse=True)[:5]

				print("\n")
				for n in s_names:
					f = all_nomes[n]['frequencia']
					s = all_nomes[n]['seculo']
					print(f"nome: {n}, frequência: {f}, século: {s}")

				all_apelidos = {}
				for s, aps in apelidos.items():
					for a, f in aps.items():
						if a not in all_apelidos:
							all_apelidos[a] = {'frequencia': f, 'seculo': s}
						else:
							if f > all_apelidos[a]['frequencia']:
								all_apelidos[a]['frequencia'] = f
								all_apelidos[a]['seculo'] = s

				s_apelidos = sorted(all_apelidos.keys(), key=lambda x: all_apelidos[x]['frequencia'], reverse=True)[:5]

				for a in s_apelidos:
					f = all_apelidos[a]['frequencia']
					s = all_apelidos[a]['seculo']
					print(f"apelido: {a}, frequência: {f}, século: {s}")
				print("\n")

			if o == 3:
				r = {}
				for linha in linhas:
					relacao = re.findall(r'Tio Materno|Tio Paterno|Irmao[s]?|Primo Materno|Primo Paterno|Sobrinho Materno|Sobrinho Paterno|Filho|Pai|Avo Materno|Avo Paterno', linha)
					for rel in relacao:
						if rel in r:
							r[rel] += 1
						else:
							r[rel] = 1

				pprint.pprint(r)

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
