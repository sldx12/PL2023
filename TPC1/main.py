def parser():
	data = []

	with open("myheart.csv", "r") as f:
		f.readline()

		for line in f.readlines():
			l = []
			for p in line.split(","):
				l.append(p)
			l[-1] = l[-1][0]
			data.append(l)

	return data

def get_age_range(age):
	low = (age // 5) * 5
	up = low + 4
	return f"[{low}-{up}]"

def get_col_range(col):
	low = (col // 10) * 10
	up = low + 9
	return f"[{low}-{up}]"

def dist_sex(data):
	results = { "M": [0, 0], "F": [0, 0]} # [x, y], x = tem doenca, y = nao tem

	for d in data:
		if (d[1] == "M"):
			if (d[5] == "1"):
				results["M"][0] += 1
			else:
				results["M"][1] += 1
		else:
			if (d[5] == "1"):
				results["F"][0] += 1
			else:
				results["F"][1] += 1
	
	return results

def dist_age(data):
	results = {}

	for d in data:
		age = int(d[0])
		a_range = get_age_range(age)
		if a_range in results:
			results[a_range] += 1
		else:
			results[a_range] = 1

	return results

def dist_col(data):
	results = {}

	for d in data:
		col = int(d[3])
		col_range = get_col_range(col)
		if col_range in results:
			results[col_range] += 1
		else:
			results[col_range] = 1

	return results

def main():
	d = parser()
	while True:
		print("Qual a distribuição que pretende visualizar?\n1 - Doença por sexo\n2 - Doença por idade\n3 - Doença por colesterol\n")
		o = int(input("> "))

		if o in [1,2,3]:
			if o == 1:
				r = dist_sex(d)

				print("M com doença: " + str(r["M"][0]) + "\nM sem doença: " + str(r["M"][1]) + "\nF com doença: " + str(r["F"][0]) + "\nF sem doença: " + str(r["F"][1]) + "\n")

			elif o == 2:
				r = dist_age(d)
				
				for ran in r:
					print(ran + ": " + str(r[ran]))

			elif o == 3:
				r = dist_col(d)

				for ran in r:
					print(ran + ": " + str(r[ran]))

		else:
			print("Opção inválida.\n")



if __name__ == "__main__":
	main()
