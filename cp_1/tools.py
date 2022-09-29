import math


class tools:


	#на вході текст, на виході словник, ключ - буква, значення кількість символів в тексті
	def count_symbols(text):
		res = {}
		for i in text:
			if not i in res:
				res[i] = 1
			else:
				res[i] += 1
		return res


	def dict_freq(d, text):
		for i in d.items():
			d[i[0]] = i[1] / len(text)


	def dict_sort(x):
		return {k: v for k, v in sorted(x.items(), key=lambda item: item[1])[::-1]}


	def dict_calc_entropy(d):
		res = 0
		for i in d.values():
			entropy = (-i*math.log2(i))
			res += entropy

		return res

	
	def dict_bigram(text, intersection):
		d = []
		if intersection:
			for i in range(0, len(text)-1):
				d.append(text[i]+text[i+1])
		else:
			for i in range(0, len(text)-1, 2):
				d.append(text[i]+text[i+1])
		return d


	def dict_calc_entropy_bigram(l,d):
		res = 0
		elements = len(l)
		for i in d.values():
			res += - (i/elements) * math.log2(i/elements)
		
		return res/2
