import regex


class files:
	def __init__(self, file_name):
		self.file_name = file_name

	def read(self):
		file = open(self.file_name)
		t = file.read()
		file.close()
		t = regex.sub(r'\p{^IsCyrillic}', ' ', t)
		print(t)


	def text(self):
		pass

	def text_wos(self):
		pass