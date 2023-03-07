import json

def main():
	while True:
		print("Which file do you want to open?")
		filename = input("> ")

		with open(filename, 'r') as f:
			linhas = f.readlines()
		
		cabeca = linhas[0]
		linhas.pop(0)
		if "{" not in cabeca:
			colunas = cabeca.split(",")
			colunas[-1] = colunas[-1].rstrip("\n")

			final = []
			tmp = {}

			for linha in linhas:
				cols = linha.split(",")
				cols[-1] = cols[-1].rstrip("\n")
				ii = 0
				for i in colunas:
					tmp[i] = cols[ii]
					ii += 1
				final.append(tmp)
			
			y = json.dumps(final)

			with open('output.json', 'w') as j:
				j.write(y)

if __name__ == "__main__":
	main()
