
from files import files
from tools import tools







if __name__ == "__main__":
	f = files("text_short.txt")
	#print(f.read())
	#print(f.read_wos())

	test = f.read()

	d = tools.count_symbols(test)
	#print(d)
	tools.dict_freq(d,test)
	#print(d)
	d = tools.dict_sort(d)
	print(d)

	print("Entropy for monogram:", tools.dict_calc_entropy(d))