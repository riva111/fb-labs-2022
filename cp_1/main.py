import math

from files import files
from tools import tools







if __name__ == "__main__":
	f = files("text.txt")
	
	print("#")
	print("# MONOGRAM")
	print("#")

	text = f.read()
	text_wos = f.read_wos() #без пробілів

	print("\n# text with spaces")
	d = tools.count_symbols(text)
	tools.dict_freq(d,text)
	d = tools.dict_sort(d)
	print(d)
	entropy = tools.dict_calc_entropy(d)
	print("Entropy:", entropy)
	print("Redundant:", 1 - (entropy/math.log2(32)))

	print("\n# text without spaces")
	d_wos = tools.count_symbols(text_wos)
	tools.dict_freq(d_wos,text_wos)
	d_wos = tools.dict_sort(d_wos)
	print(d_wos)
	entropy = tools.dict_calc_entropy(d_wos)
	print("Entropy:", entropy)
	print("Redundant:", 1 - (entropy/math.log2(32)))