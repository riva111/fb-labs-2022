

from files import files







if __name__ == "__main__":
	f = files("text_short.txt")
	print(f.read())
	print(f.read_wos())