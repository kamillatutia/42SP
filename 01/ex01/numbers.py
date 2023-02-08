def	numbers():
	file = open("numbers.txt", "r")
	txt = file.read()
	splitted_text = txt.split(",")
	for eachnumber in splitted_text:
		print(eachnumber.strip())
	file.close()

if __name__ == '__main__':
	numbers()