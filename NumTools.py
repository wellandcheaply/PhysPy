from random import randint as rd
from math import floor, ceil, sqrt

class Vec:

	# TODO: class Vec() is pretty much done for the moment, so that's good.

	def __init__(self, values):
		self.vals = values
		if len(self) >= 1:
			self.x = values[0]
			if len(self) >= 2:
				self.y = values[1]
				if len(self) >= 3:
					self.z = values[2]
					if len(self) >= 4:
						self.t = values[3]

	# define the syntax Vec(x) == Vec(y)
	def __eq__(self, other):
		'''
		:param other: a Vec() object to be compared
		:return:
			True if the ordered values of the calling Vec object
			are identical to those of the passed Vec object
			False otherwise
		'''
		if type(other) is Vec:
			return self.vals == other.vals
		return False

	# define the syntax Vec(x) != Vec(y)
	def __ne__(self, other):
		'''
		:param other: a Vec() object to be compared
		:return:
			False if the ordered values of the calling Vec object
			are identical to those of the passed Vec object
			True otherwise
		'''
		if type(other) is Vec:
			return self.vals != other.vals
		return True

	# define the syntax Vec(x) < Vec(y)
	def __lt__(self, other):
		'''
		:param other: a Vec() object to be compared
		:return:
			True if the magnitude of <self> is
			less than to the magnitude of <other>
			False otherwise
		'''
		if type(other) is Vec:
			return self.mag() < other.mag()
		raise ArithmeticError(
			"Cannot compare objects of two different types"
		)

	# define the syntax Vec(x) > Vec(y)
	def __gt__(self, other):
		'''
		:param other: a Vec() object to be compared
		:return:
			True if the magnitude of <self> is
			greater than the magnitude of <other>
			False otherwise
		'''
		if type(other) is Vec:
			return self.mag() > other.mag()
		raise ArithmeticError(
			"Cannot compare objects of two different types"
		)

	# define the syntax Vec(x) <= Vec(y)
	def __le__(self, other):
		'''
		:param other: a Vec() object to be compared
		:return:
			True if the magnitude of <self> is
			less than or equal to the magnitude of <other>
			False otherwise
		'''
		if type(other) is Vec:
			return self.mag() <= other.mag()
		raise ArithmeticError(
			"Cannot compare objects of two different types"
		)

	# define the syntax Vec(x) >= Vec(y)
	def __ge__(self, other):
		'''
		:param other: a Vec() object to be compared
		:return:
			True if the magnitude of <self> is
			greater than or equal to the magnitude of <other>
			False otherwise
		'''
		if type(other) is Vec:
			return self.mag() >= other.mag()
		raise ArithmeticError(
			"Cannot compare objects of two different types"
		)

	# define the syntax -Vec(x) as returning an equal and opposite vector
	def __neg__(self):
		return Vec([-x for x in self])

	# define the syntax ~Vec(x) as returning the reverse of the vector (no longer a bit op)
	def __invert__(self):
		return Vec(self.vals[::-1])

	# define the int(Vec(x)) function
	def __int__(self):
		# return a copy of the valling vector wherein all values are rounded down to the nearest integer
		return Vec([int(x) for x in self])

	# define the round(Vec(x), n) function
	def __round__(self, n):
		'''
		:param n: the number of decimal places to round to
		:return:
			a copy of the passed Vec() object with
			each of its values rounded to n decimal places
		'''
		return Vec([round(x, n) for x in self])

	# define the math.floor(Vec(x)) function
	def __floor__(self):
		return Vec([floor(x) for x in self])

	# define the math.ceil(Vec(x)) function
	def __ceil__(self):
		return Vec([ceil(x)] for x in self)

	# define the behavior of calling print() on a
	def __repr__(self):
		return str(self.vals)

	# define the behavior of calling len() on a
	def __len__(self):
		return len(self.vals)

	# define the behavior of the symbol + as it applies to Vec objects
	def __add__(self, other):
		'''
		:param other: an object of type int, float, or Vec to be added
		:return:
			if other is of type Vec:
				the result of the vector addition of the two vectors
			if other is of type int or float:
				the result of adding other to each value in the calling vector
		'''
		if type(other) is int or type(other) is float:
			return Vec([x + other for x in self])
		elif type(other) is Vec:
			if self.__len__() == len(other):
				return Vec([self[x] + other[x] for x in range(len(self))])
			else:
				raise ArithmeticError(
					"Arrays must be the same length to add them"
				)
		else:
			raise ArithmeticError(
				"Can only add Vec to type int, float, or Vec"
			)

	# define the behavior of the symbol - as it applies to Vec objects
	def __sub__(self, other):
		'''
		:param other: an object of type int, float, or Vec to be subtracted
		:return:
			if other is of type Vec:
				the result of subtracting other from the calling vector
			if other is of type int or float:
				the result of subtrcating other from each value in the calling vector
		'''
		if type(other) is int or type(other) is float:
			return Vec([x - other for x in self])
		elif type(other) is Vec:
			if len(self) == len(other):
				return Vec([self[x] - other[x] for x in range(len(self))])
			else:
				raise ArithmeticError(
					"Arrays must be the same length to subtract them"
				)
		else:
			raise ArithmeticError(
				"Can only subtract type int, float, or Vec from Vec"
			)

	# define the behavior of the symbol * as it applies to Vec objects
	def __mul__(self, other):
		'''
		:param other: an object of type int, float, or Vec by which to multiply
		:return:
			if other is of type Vec:
				the dot product of the two vectors
			if other is of type int or float:
				the result of scalar multiplication of the calling vector by other
		'''
		if type(other) is int or type(other) is float:
			return Vec([x * other for x in self])
		elif type(other) is Vec:
			if len(self) == len(other):
				return self.dot(other)
			else:
				raise ArithmeticError(
					"Vectors must be the same length to take the dot product"
				)
		else:
			raise ArithmeticError(
				"Multiplier must be of type int or type Vec (for dot product)"
			)

	# define the behavior of the symbol / as it applies to Vec() objects
	def __truediv__(self, other):
		'''
		:param other: an object of type int, float, or Vec by which to divide
		:return:
			if other is of type int or float:
				the result of scalar vision of each value in self.vals by other
			if other is of type Vec:
				the result of the 'dot division' of the two vectors
		'''
		if type(other) is int or type(other) is float:
			if other != 0:
				return Vec([x / other for x in self])
			else:
				raise ArithmeticError(
					"Cannot divide by 0"
				)
		elif type(other) is Vec:
			if len(self) == len(other):
				if 0 not in other.vals:
					return sum([self[x] / other[x] for x in range(len(self))])
				else:
					raise ArithmeticError(
						"Cannot divide by 0"
					)
			else:
				raise ArithmeticError(
					"Vectors must be the same length to take the dot quotient"
				)
		else:
			raise ArithmeticError(
				"Divisor must be of type int or type Vec (for dot quotient)"
			)

	# define the behavior of the symbol ** as it applies to Vec() objects.
	def __pow__(self, power):
		'''
		syntax must take the form
			<Vec> ** int_or_float
		rather than the form
			int_or_float ** <Vec>

		:param power: the power to which to raise each value
		:return:
			a Vec() object wherein each value of the
			calling vector has been raised to the passed power
		'''
		return Vec([x ** power for x in self])

	# define the behavior of the symbol % as it applies to Vec() objects.
	def __mod__(self, modulo):
		'''
		:param modulo: the argument of the mathematical mod() function
		:return:
			the remainder of each value in <some Vec()>.vals after division by <modulo>
		'''
		return Vec([x % modulo for x in self])

	# define the behavior of the keyword 'in' as it applies to Vec() objects
	def __contains__(self, item):
		'''
		(i.e. ' for x in <some Vec()>: ... ' )
		:param item: the item to be searched for in <some Vec()>.vals
		:return:
			True if the x is a value in <some Vec()>.vals
			else False
		'''
		return item in self.vals

	# define the behavior of list indexing syntax as it applies to Vec() objects.
	def __getitem__(self, index):
		'''
		(i.e. ' var = <some Vec()>[index] ' )

		:param index: the index of the item to be returned
		:return: the item at <index> in <some Vec()>.vals
		'''
		if(type(index) is int):
			return self.vals[index]
		else:
			raise ArithmeticError(
				"Indexing is only supported for integer indices"
			)

	# define the behavior of the keyphrase 'for i in' as it applies to Vec() objects
	def __iter__(self):
		'''
		(i.e. ' for x in <some Vec()>: ... ' )
		iterate through the list <some Vec()>.vals and yield each value
		'''
		for index in range(len(self)):
			yield self[index]

	def coors(self):
		'''
		reset self.x/y/z/t after a change
		called by a few other functions (setVals, append, remove) but should otherwise probably be treated as 'private'
		'''
		if len(self) >= 1:
			self.x = self[0]
			if len(self) >= 2:
				self.y = self[1]
				if len(self) >= 3:
					self.z = self[2]
					if len(self) >= 4:
						self.t = self[3]

	def setVals(self, vals):
		'''
		set the values of the calling vector to the passed values without creating a new Vec object

		this function should be used in place of syntax such as <some Vec()>.vals = new_vals
		as that would fail to reset the Vec object's "coordinates" whereafter
		calling self.x/y/z/t would erroneously return the old values

		:param vals: object of type list containing real values
		'''
		self.vals = vals
		self.coors()

	# append the item to the vector at the given optional index and update the vectors coordinate syntax
	def append(self, value, index=None):
		if index is None:
			self.vals.append(value)

		elif type(index) is int:
			self.vals.append(value, index)
		else:
			raise ArithmeticError(
				"Indexing is only supported for integer indices"
			)
		self.coors()

	# remove the item at the passed index and refactors the vector's coordinate synatx
	def remove(self, index):
		if type(index) is int:
			self.vals.remove(index)
			self.coors()
		else:
			raise ArithmeticError(
				"Indexing is only supported for integer indices"
			)

	# return the sum of all values in the calling Vec() object
	def total(self):
		return sum(self.vals)

	# return the result of self + other ... just a handy redundancy, really
	def sum(self, other):
		return self + other

	# return the magnitude of the calling Vec() object
	def mag(self):
		return (self**2).total()**(1/2)

	# return the Vec representation of the unit vector of the calling Vec() object
	def unit(self):
		return Vec((self / self.mag()).vals)

	# return the straight-line distance between two vectors
	def dist(self, other):
		difference = self - other
		return (difference**2).total()**(1/2)

	# return the slope between the Vec() representation of two points
	def slope(self, other):
		'''
		:param r1: the Vec() representation of one point
		:param r2: the Vec() representation of another point
		:return:
			if r1 and r2 in R^2:
				float(dy/dx)
			else: (ex. r1 and r2 in R^4)
				Vec([dy/dx, dz/dx, dt/dx, dz/dy, dt/dy, dt/dz])
		'''
		if len(self) == len(other):
			dr = self - other
			toReturn = Vec([[dr[numer]/dr[denom] for numer in range(denom+1, len(other))] for denom in range(len(other)-1)])
			if len(toReturn) == 1:
				return toReturn[0]
			else:
				return Vec(toReturn)

	def dot(self, other):
		'''
		perform standard vector dot product operation
		return an int or float object
		'''
		if len(self) == len(other):
			return sum([self[x] * other[x] for x in range(len(self))])
		else:
			raise ArithmeticError(
				"Arrays must be the same length to take the dot product."
			)

	def cross(self, other):
		'''
		perform standard vector cross product operation - only valid for vectors of length 3
		return a Vec object
		'''
		if type(other) is not Vec or not (len(self) == 3 and len(other) == 3):
			raise ArithmeticError(
				"Can only take cross product of two 3-dimensional vectors."
			)
		else:
			a = self.y*other.z - self.z*other.y
			b = self.z*other.x - self.x*other.z
			c = self.x*other.y - self.y*other.x
			return Vec([a,b,c])


class Matrix:
	def __init__(self, vecs):
		self.rows = len(vecs)
		self.cols = len(vecs[0])
		self.isSquare = self.rows == self.cols
		self.vecs = vecs

	'''
	define the behavior of the syntax <object>[someIndex] as it applies to Matrix objects
	return a Vec object: the _row_ of the matrix at that index.
	'''
	def __getitem__(self, item):
		if type(item) is int:
			return self.vecs[item]
		else:
			raise ArithmeticError(
				"Indexing is only supported for integer indicies."
			)

	'''
	define the behavior of the symbol = as it applies to a Matrix
	'''
	def __eq__(self, other):
		if type(other) is not Matrix:
			return False
		elif self.rows == other.rows and self.cols == other.cols:
			for x in range(self.rows):
				if(self[x] != other[x]):
					return False
			return True
		else:
			return False

	'''
	define the behavior of calling len(<object>) on a Matrix.
	'''
	def __len__(self):
		return [self.rows, self.cols]

	'''
	define the behavior of calling print(<object>) on a Matrix
	'''
	def __repr__(self):
		toReturn = ""
		for vec in self.vecs:
			toReturn += str(vec.vals) + '\n'
		return toReturn

	'''
	define the behavior of the symbol * as it relates to a Matrix
	
	multiply all values in the matrix by a passed multiplier multiplier must be a scalar of type int or float
	complex functionality to come in the future
	
	NOTE: the matrix must come first;
		<Matrix> * 5 works.
		5 * <Matrix> does not. 
	
	return a Matrix object
	'''
	def __mul__(self, multiplier):
		if type(multiplier) not in [int, float]:
			raise ArithmeticError(
				"Multiply not supported for non-scalars"
			)
		else:
			return Matrix([Vec([multiplier*x for x in vec]) for vec in self.vecs])

	'''
	get the row of at the given index 
	NOTE: the row said in mathematics to be row #1 would be returned by passing 0 to this function, etc
	return a Vec object
	'''
	def row(self, index):
		if type(index) is int:
			return self.__getitem__(index)
		else:
			raise ArithmeticError(
				"Indexing is only supported for integer indicies"
			)

	'''
	get the column of at the given index 
		(note: the column said in mathematics to be column #1 would be returned by passing 0 to this function, etc)
	return a Vec object
	'''
	def col(self, index):
		if type(index) is int:
			return Vec([vec[index] for vec in self.vecs])
		else:
			raise ArithmeticError(
				"Indexing is only supported for integer indicies"
			)

	def array(self):
		return [[val for val in row.getVals()] for row in self.vecs]

	'''
	return a matrix which is the transpose of the calling object.
	the transpose of a matrix is just its reflection about the long North-West to South-East diagonal.
	'''
	def T(self):
		return Matrix([Vec([self.vecs[j].vals[i] for j in range(len(self.vecs))]) for i in range(len(self.vecs[0].vals))])

	'''
	a matrix is symmetric if it's equal to its transposition
	return True/False
	'''
	def isSymmetric(self):
		return self == self.T()

	'''
	a matrix is skew if it's equal to the negation of its transposition
	return True/False
	'''
	def isSkew(self):
		return self.__mul__(-1) == self.T()

	'''
	a hilarious single-line masterpiece of Generator-foo
	
	return a Matrix which is the dot product of the calling Matrix and the passed one. 
	or
	throw an ArithmeticError if the two matrices are of incompatible dimensions.
	'''
	def dot(self, other):
		return Matrix([Vec([sum([row.vals[i] * col[i] for i in range(len(self.vecs[0].vals))]) for col in [[rowT.vals[j] for rowT in other.vecs] for j in range(len(self.vecs[0].vals))]]) for row in self.vecs]) if self.cols == other.rows else ArithmeticError("Matrix Multiplication A.dot(B) only valid if the number of columns in A is equal to the number of rows in B.")

	'''
	this was written for the slow-ass function below now known as <Matrix.det2()>
	it might be handy somewhere else, but I dunno.
	
	return a matrix just like the calling one,
	except missing row 0 and column <index>
	'''
	def trim(self, index):
		keepRows = [self.vecs[x].getVals() for x in range(1, self.rows)]
		for row in range(0, self.rows-1):
			keepRows[row].pop(index)
			keepRows[row] = Vec(keepRows[row])
		return Matrix(keepRows)

	'''
	does what it says on the tin
	return True/False
	'''
	def isEschelon(self):
		t = self.T()
		for x in range(t.rows):
			row = t.vecs[x].getVals()
			for y in range(x+1, t.cols):
				if(row[y] != 0): return False
		return True

	'''
	find the determinant of a square matrix
	first find its non-reduced row-eschelon form
	then multiply accross the main diagonal
	'''
	def det(self):
		if not self.isSquare:
			raise ArithmeticError(
				"The determinant can only be taken for square matrices"
			)
		def format(m):
			listRows = m.array()  # get the matrix in list-o-lists format
			signFlip = False  # account for negation after each row swap

			for i in range(m.rows-1):
				if m.col(i).vals.count(0) == m.rows:
					# no row swap can be made, so you've got a sticky 0
					return Matrix([[0]]), False

				diagonal = listRows[i][i]

				# handle any pesky zeroes in the diagonal
				if diagonal == 0:
					# A swap can be made, so find a suitable row
					for j in range(i+1, m.rows):
						if listRows[j][i] != 0:
							listRows[i], listRows[j] = listRows[j], listRows[i]
							signFlip = not signFlip
							diagonal = listRows[i][i]

				# find the factor, multiply across, and subtract down
				for j in range(i+1, m.rows):
					mult = listRows[j][i]/diagonal
					for k in range(m.rows):
						listRows[j][k] -= listRows[i][k]*mult

			# return the relevant conclusions
			return Matrix([Vec([val for val in row]) for row in listRows]), signFlip

		newMat, signFlip = format(self)  # format the matrix
		total = 1 if not signFlip else -1  # account for any outstanding negation
		for i in range(newMat.rows): total *= newMat[i][i]  # multiply down the diagonal

		# handle rounding errors
		return int(round(total))  # (this works fine up to ~14/15-digit determinants)

	'''
	this method is extremely slow at finding the determinant for large matrices.
	for 2x2 and 3x3 matrices, it's negligibly faster.
	it was a noble first attempt, really didn't make the cut
	
	even in the (relatively) tame case of an 8x8 matrix, the <Matrix.det()> method above is ___ 500-2500 times faster ___.
	'''
	def det2(self):
		
		def det2x2():
			if not self.isSquare:
				raise ArithmeticError(
					"The determinant can only be taken for square matrices"
				)
			elif not(self.rows == 2 and self.cols == 2):
				raise ArithmeticError(
					"This function can only be used on 2x2 square matricies"
				)
			else:
				return self.vecs[0][0]*self.vecs[1][1] - self.vecs[0][1]*self.vecs[1][0]

		def det3x3():
			if not self.isSquare:
				raise ArithmeticError(
					"The determinant can only be taken for square matrices"
				)
			elif not(self.rows == 3 and self.cols == 3):
				raise ArithmeticError(
					"This function can only be used on 3x3 square matricies"
				)
			else:
				vals = [[val for val in self.__getitem__(row)] for row in range(3)]
				pos = sum([
					vals[0][0] * vals[1][1] * vals[2][2],
					vals[0][1] * vals[1][2] * vals[2][0],
					vals[0][2] * vals[1][0] * vals[2][1]])
				neg = sum([
					vals[2][0] * vals[1][1] * vals[0][2],
					vals[2][1] * vals[1][2] * vals[0][0],
					vals[2][2] * vals[1][0] * vals[0][1]])
			return pos-neg
		
		if not self.isSquare:
			raise ArithmeticError(
				"The determinant can only be taken for square matrices"
			)
		elif self.rows == 2:
			return det2x2()
		elif self.rows == 3:
			return det3x3()
		else:
			rowI = self.vecs[0]
			add = True
			total = 0
			for x in range(self.cols):
				total += rowI[x]*self.trim(x).det() if add else -1*rowI[x]*self.trim(x).det()
				add = not add
			return total

	# TODO: A third determinant function (Leibniz formual - should be very fast) is still coming along
	# TODO: Matrix still won't give you RowEschelon form or do much elimination.
	# TODO: Matrix still won't solve your system of equations
	# TODO: Matrix still has no functions for eigenvalues/vectors
	# TODO: Matrix still won't give you the inverse of a matrix
	# TODO: Matrix still doesn't handle complex numbers, and I honestly don't even want to think about that.
	# TODO: ^^^ Probably warrants it whole own class rather than much change to this one.

def I(n):
	identity = []
	for rowDex in range(n):
		newRow = []
		for colDex in range(n):
			newRow.append(1) if colDex == rowDex else newRow.append(0)
		identity.append(Vec(newRow))
	return Matrix(identity)


def random_square_matrix(n):
	rows = []
	for rowDex in range(n):
		row = []
		for colDex in range(n):
			row.append(rd(0,50))
		rows.append(Vec(row))
	#return Matrix(rows)
	toReturn = "Matrix(["
	for x in rows:
		toReturn += "Vec({}), ".format(str(x.vals))
		toReturn += '\n'
	toReturn += "])"
	return toReturn

'''
eight = Matrix([Vec([10, 5, 27, 0, 0, 0, 50, 24]),
				Vec([0, 38, 15, 28, 5, 7, 37, 2]),
				Vec([25, 40, 6, 12, 1, 18, 14, 11]),
				Vec([48, 25, 23, 15, 36, 35, 28, 5]),
				Vec([27, 46, 30, 2, 20, 26, 32, 40]),
				Vec([11, 9, 40, 38, 49, 19, 29, 12]),
				Vec([24, 1, 6, 21, 23, 1, 3, 27]),
				Vec([34, 27, 47, 10, 13, 3, 40, 44])])
				
# 100x100 build time for random integer values on [0-50]: 0.1216 seconds
# Determinate of this matrix: 2284784652856255376675472288673118509546940811228880101478350821136420519792329633542833866718250902178657390136472868306416933282144585097519677731018847322252582918455804482975457776361216671744
# Jesus, you could put someone's eye out with that thing.
'''
