def main():
	sum = 0
	summing = True

	print("Introduza o texto.")
	text = input("> ")

	i = 0
	while i < len(text):
		if text[i:i+3].lower() == "off":
			summing = False
			i += 3
		elif text[i:i+2].lower() == "on":
			summing = True
			i += 2
		elif text[i] == "=":
			print(sum)
			i += 1
		elif summing == True:
			sum += int(text[i])
			i += 1
		elif summing == False:
			i += 1
	
if __name__ == "__main__":
	main()
