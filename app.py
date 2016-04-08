#!flask/bin/python
from flask import Flask, jsonify, abort
app = Flask(__name__)


#created a class so that I can pass the funciton names via the API and retrieve the function object
class Functions(object):
	#fibonacci
	def fibonacci(self, n):
		a = 0
		b = 1
		sequence = []
		while len(sequence) < n:
			sequence.append(a)
			a = b
			b = sequence[-1] + a
		return sequence

	#happy numbers, with a helper function for recursion
	def happy(self, n):
		a = 1
		sequence = []
		while len(sequence) < n:
			reduced = self.happy_helper(a)
			if reduced:
				sequence.append(a)
			a += 1
		return sequence

	def happy_helper(self, a):
		string_numerals = list(str(a))
		reduced = reduce(lambda x,y: x+y, map(lambda x:int(x)**2, string_numerals))
		if reduced == 1:
			return True
		#i read about happy numbers on wikipedia and learned all unhappy numbers reach this cycle
		elif reduced in [4, 16, 37, 58, 89, 145, 42, 20]:
			return False
		else: 
			return self.happy_helper(reduced)
			
	#abundant numbers
	def abundant(self, n):
		a = 1
		sequence = []
		while len(sequence) < n:
			filtered = reduce(lambda x,y: x+y, filter(lambda x: a % x == 0, range(1,a+1)))
			if filtered > 2 * a:
				sequence.append(a) 
			a += 1
		return sequence

#serves response
@app.route('/api/v1.0/functions/<function>/<int:num>/<int:option>', methods=['GET'])
def nth(function, num, option):
	m = Functions()
	if len(function) == 0 or len(str(num)) == 0 or len(str(option)) == 0 or num < 0:
		abort(404)
	if option == 1:
		return jsonify({'sequence':function,'n':num,'list':getattr(m,function)(num)})
	elif option == 2:
		return jsonify({'sequence':function,'n': num, 'term':getattr(m,function)(num).pop()})
	else:
		abort(404)



if __name__ == '__main__':
    app.run(debug=True)