import json
import re

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

			o_filename = filename.split(".")[0] + ".json"
			with open(o_filename, 'w') as j:
				j.write(y)

		elif re.search(r'\{(\d+)\}', cabeca) != None:
			colunas = cabeca.split(",")
			colunas = colunas[:-1]

			final = []
			tmp = {}

			for linha in linhas:
				cols = linha.split(",")
				cols[-1] = cols[-1].rstrip("\n")
				ii = 0
				cc = 0
				while cc < len(colunas):
					if "{" not in colunas[cc]:
						tmp[colunas[cc]] = cols[ii]
						ii += 1
						cc += 1
					else:
						num = re.search(r"\{(.+?)\}", colunas[cc])
						num = int(num.group(1))
						content = re.search(r"(.+?)\{", colunas[cc])
						content = content.group(1)

						tmp[content] = []
						for x in range(0, num):
							tmp[content].append(cols[ii])
							ii += 1
							cc += 1

				final.append(tmp)

			y = json.dumps(final)

			o_filename = filename.split(".")[0] + ".json"
			with open(o_filename, 'w') as j:
				j.write(y)

		elif re.search(r'\{(\d+(,\d+)*)\}', cabeca) != None and "::" not in cabeca:
			colunas = []
			temp = ""
			skip_next = False

			for i, c in enumerate(cabeca):
				if skip_next:
					temp += c
					if c == '}':
						skip_next = False
					continue
				elif c == '{':
					skip_next = True
					temp += c
				elif c == ',':
					if skip_next:
						temp += c
					else:
						colunas.append(temp)
						temp = ""

				else:
					temp += c
			colunas.append(temp)
			colunas.pop()
			colunas.pop()

			final = []

			for linha in linhas:
				tmp = {}
				cols = linha.split(",")
				ii = 0
				cc = 0
				while cc < len(colunas) - 1:
					if "{" not in colunas[cc]:
						tmp[colunas[cc]] = cols[ii]
						ii += 1
						cc += 1
					else:
						match = re.search(r'(\d+),(\d+)', colunas[cc])
						num_min = int(match.group(1))
						num_max = int(match.group(2))
						content = re.search(r"(.+?)\{", colunas[cc])
						content = content.group(1)

						tmp[content] = []
						for x in range(0, num_max):
							if x < num_min:
								tmp[content].append(cols[ii])
								ii += 1
								cc += 1
							else:
								if len(cols[ii]) != 0:
									tmp[content].append(cols[ii])
									ii += 1
									cc += 1

				final.append(tmp)

			y = json.dumps(final)
			
			o_filename = filename.split(".")[0] + ".json"
			with open(o_filename, 'w') as j:
				j.write(y)

		elif "::" in cabeca:
			colunas = []
			temp = ""
			skip_next = False

			for i, c in enumerate(cabeca):
				if skip_next:
					temp += c
					if c == "}":
						skip_next = False
					continue
				elif c == '{':
					skip_next = True
					temp += c
				elif c == ',':
					if skip_next:
						temp += c
					else:
						colunas.append(temp)
						temp = ""
				else:
					temp += c

			colunas.append(temp)

			colunas.pop()
			colunas.pop()

			final = []

			for linha in linhas:
				tmp = {}
				cols = linha.split(",")
				ii = 0
				cc = 0
				while cc < len(colunas) - 1:
					if "{" not in colunas[cc]:
						tmp[colunas[cc]] = cols[ii]
						ii += 1
						cc += 1
					else:
						match = re.search(r'(\d+),(\d+)', colunas[cc])
						num_min = int(match.group(1))
						num_max = int(match.group(2))
						content = re.search(r"(.+?)\{", colunas[cc])
						content = content.group(1)
						content2 = re.search(r"::(.+)", colunas[cc])
						content2 = content2.group(1)

						tmp2 = []
						for x in range(0, num_max):
							if x < num_min:
								tmp2.append(int(cols[ii]))
								ii += 1
								cc += 1
							else:
								if len(cols[ii]) != 0 and cols[ii] != '\n':
									tmp2.append(int(cols[ii]))
									ii += 1
									cc += 1

						n = content + "_" + content2
						tmp[n] = sum(tmp2)

				final.append(tmp)

			y = json.dumps(final)
			
			o_filename = filename.split(".")[0] + ".json"
			with open(o_filename, 'w') as j:
				j.write(y)

if __name__ == "__main__":
	main()
