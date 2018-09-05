def hello():
	print "Global hello"

class bla:
	def hello(self):
		self.thing()
		hello()
	def thing(self):
		print "hello"
b=bla()
b.hello()

