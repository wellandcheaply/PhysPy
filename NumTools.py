from random import randint as rd
import time as t


class Vec:
	def __init__(self, values):
		self.vals = values
		if len(self.vals) >= 1:
			self.x = values[0]
			if len(self.vals) >= 2:
				self.y = values[1]
				if len(self.vals) >= 3:
					self.z = values[2]
					if len(self.vals) >= 4:
						self.t = values[3]

	# TODO: class Vec() still has some magic methods that need overwriting, but it gets the job done.

	def __eq__(self, other):
		if type(other) is Vec:
			if self.__len__() == len(other):
				for x in range(self.__len__()):
					if self[x] != other[x]:
						return False
				return True
		return False

	def __getitem__(self, item):
		if(type(item) is int):
			return self.vals[item]
		else:
			raise ArithmeticError(
				"Indexing is only supported for integer indices"
			)

	def __repr__(self): return str(self.vals)

	def __len__(self): return len(self.vals)

	def __add__(self, other):
		if type(other) is int or type(other) is float:
			return Vec([x + other for x in self.vals])
		elif type(other) is Vec:
			if len(self.vals) == len(other.vals):
				return Vec([self.vals[x] + other.vals[x] for x in range(len(self))])
			else:
				raise ArithmeticError(
					"Arrays must be the same length to add them"
				)
		else:
			raise ArithmeticError(
				"Can only add Vec to type int, float, or Vec"
			)

	def __sub__(self, other):
		if type(other) is int or type(other) is float:
			return Vec([x - other for x in self.vals])
		elif type(other) is Vec:
			if len(self.vals) == len(other.vals):
				return Vec([self.vals[x] - other.vals[x] for x in range(len(self))])
			else:
				raise ArithmeticError(
					"Arrays must be the same length to subtract them"
				)
		else:
			raise ArithmeticError(
				"Can only subtract type int, float, or Vec from Vec"
			)

	def __mul__(self, other):
		if type(other) is int or type(other) is float:
			return Vec([x * other for x in self.vals])
		elif type(other) is Vec:
			if len(self.vals) == len(other.vals):
				return self.dot(other)
			else:
				raise ArithmeticError(
					"Vectors must be the same length to take the dot product"
				)
		else:
			raise ArithmeticError(
				"Multiplier must be of type int or type Vec (for dot product)"
			)

	def __truediv__(self, other):
		if type(other) is int or type(other) is float:
			if other != 0:
				return Vec([x / other for x in self.vals])
			else:
				raise ArithmeticError(
					"Cannot divide by 0"
				)
		elif type(other) is Vec:
			if len(other.vals) == len(self.vals):
				if 0 not in other.vals:
					return sum([self.vals[x] / other.vals[x] for x in range(len(self))])
				else:
					raise (ArithmeticError(
						"Cannot divide by 0"))
			else:
				raise ArithmeticError(
					"Vectors must be the same length to take the dot quotient"
				)
		else:
			raise ArithmeticError(
				"Divisor must be of type int or type Vec (for dot quotient)"
			)

	def __pow__(self, power, modulo=None):
		return Vec([x ** power for x in self.vals])

	def __mod__(self, modulo):
		return Vec([x % modulo for x in self.vals])

	def __iter__(self):
		for index in range(len(self.vals)):
			yield self.vals[index]

	'''
	Resets self.x/y/z/t after a change
	Called by a couple other functions (setVals, remove)
	'''
	def coors(self):
		if len(self.vals) >= 1:
			self.x = self.vals[0]
			if len(self.vals) >= 2:
				self.y = self.vals[1]
				if len(self.vals) >= 3:
					self.z = self.vals[2]
					if len(self.vals) >= 4:
						self.t = self.vals[3]

	# You're not writing java, jojo. Calm down.
	def getVals(self):
		toReturn = [x for x in self.vals]
		return toReturn

	'''
	This is handy though, as ypassing it by declaring Vec.vals = list(newVals) will fail to reset vec's "coordinates"
	Calling self.x/y/z/t would erroneously return the old value afterward
	'''
	def setVals(self, vals):
		self.vals = vals
		self.coors()

	# Removes an item and
	def remove(self, index):
		if type(index) is int:
			self.vals.remove(index)
			self.coors()
		else:
			raise ArithmeticError(
				"Indexing is only supported for integer indices"
			)

	# I have no idea why anyone would want this
	def total(self): return sum(self.vals)

	# This is a handy overlap though
	def sum(self, other): return self.__add__(other)

	# Float magnitude
	def mag(self): return sum([x ** 2 for x in self.vals]) ** (1 / 2)

	# Vec unit vector
	def unit(self): return Vec((self / self.mag()).vals)

	# Vec dot product
	def dot(self, other):
		if len(self.vals) != len(other.vals):
			raise ArithmeticError(
				"Arrays must be the same length to take the dot product."
			)
		else:
			return sum([self.vals[x] * other.vals[x] for x in range(len(self))])

	# Vec cross product
	def cross(self, other):
		if type(other) is not Vec or not (self.__len__() == 3 and len(other) == 3):
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
		self.cols = len(vecs[0].vals)
		self.isSquare = self.rows == self.cols
		self.vecs = vecs

	def __getitem__(self, item):
		if type(item) is int:
			return self.vecs[item]
		else:
			raise ArithmeticError(
				"Indexing is only supported for integer indicies."
			)

	def __eq__(self, other):
		if type(other) is not Matrix:
			return False
		elif self.rows == other.rows and self.cols == other.cols:
			for x in range(self.rows):
				if(self.__getitem__(x) != other[x]):
					return False
			return True
		else: return False

	def __len__(self):
		return [self.rows, self.cols]

	def __repr__(self):
		toReturn = ""
		for vec in self.vecs:
			toReturn += str(vec.vals) + '\n'
		return toReturn

	def __mul__(self, other):
		if type(other) not in [int, float]:
			raise ArithmeticError(
				"Multiply not supported for non-scalars"
			)
		else:
			return Matrix([Vec([other*x for x in vec]) for vec in self.vecs])

	def row(self, index):
		if type(index) is int:
			return self.__getitem__(index)
		else:
			raise ArithmeticError(
				"Indexing is only supported for integer indicies"
			)

	def col(self, index):
		if type(index) is int:
			return Vec([vec[index] for vec in self.vecs])
		else:
			raise ArithmeticError(
				"Indexing is only supported for integer indicies"
			)

	def array(self):
		return [[val for val in row.getVals()] for row in self.vecs]

	def T(self):
		return Matrix([Vec([self.vecs[j].vals[i] for j in range(len(self.vecs))]) for i in range(len(self.vecs[0].vals))])

	def isSymmetric(self):
		return self == self.T()

	def isSkew(self):
		return self.__mul__(-1) == self.T()

	'''
	A hilarious single-line masterpiece of Generator-foo
	
	Returns a Matrix which is the dot product of the calling Matrix and the passed one. 
	or
	Throws an ArithmeticError if the two matrices are of incompatible dimensions.
	'''
	def dot(self, other):
		return Matrix([Vec([sum([row.vals[i] * col[i] for i in range(len(self.vecs[0].vals))]) for col in [[rowT.vals[j] for rowT in other.vecs] for j in range(len(self.vecs[0].vals))]]) for row in self.vecs]) if self.cols == other.rows else ArithmeticError("Matrix Multiplication A.dot(B) only valid if the number of columns in A is equal to the number of rows in B.")

	'''
	This was written for the slow-ass function below now known as <Matrix.det2()>
	It might be handy somewhere else, but I dunno.
	
	Args
		index (int)
	
	Returns a matrix just like the calling one,
	except missing row 0 and column <index>
	'''
	def trim(self, index):
		keepRows = [self.vecs[x].getVals() for x in range(1, self.rows)]
		for row in range(0, self.rows-1):
			keepRows[row].pop(index)
			keepRows[row] = Vec(keepRows[row])
		return Matrix(keepRows)

	'''
	Returns True/False
	Does what it says on the tin
	'''
	def isEschelon(self):
		t = self.T()
		for x in range(t.rows):
			row = t.vecs[x].getVals()
			for y in range(x+1, t.cols):
				if(row[y] != 0): return False
		return True

	'''
	Find the determinant of a square matrix
	First, find its non-reduced row-eschelon form
	Then multiply accross the main diagonal
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
	This method is extremely slow at finding the determinant for large matrices.
	For 2x2 and 3x3 matrices, it's negligibly faster.
	It was a noble first attempt, really didn't make the cut
	
	Even in the (relatively) tame case of an 8x8 matrix, the <Matrix.det()> method
	above is 1000-2000 times faster. 
	
	It's really long and ugly, so I've included line-commented block comments top and bottom for if you hate it.
	Or just delete it tbh
	Ugh
	'''
	#'''
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
	#'''

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


def generateSquare(n):
	rows = []
	for rowDex in range(n):
		row = []
		for colDex in range(n):
			row.append(rd(0,50))
		rows.append(Vec(row))
	return Matrix(rows)

'''
Some tests / matricies I might use again

four = Matrix([Vec([20, 44, 15, 5]),
			   Vec([42, 48, 18, 33]),
			   Vec([2, 24, 4, 32]),
			   Vec([44, 38, 8, 30])])

five = Matrix([Vec([0,17,2,3,4]),
			   Vec([5,6,7,8,9]),
			   Vec([10,11,12,13,14]),
			   Vec([15,16,17,18,19]),
			   Vec([20,21,22,23,24])])
			   
five2 = Matrix([Vec([0,17,2,3,4]),
				Vec([5,6,7,7,7]), 
				Vec([13,22,7,7,27]), 
				Vec([14,44,2,3,2]), 
				Vec([11,5,1,6,1])])

eight = Matrix([Vec([10, 5, 27, 0, 0, 0, 50, 24]),
				Vec([0, 38, 15, 28, 5, 7, 37, 2]),
				Vec([25, 40, 6, 12, 1, 18, 14, 11]),
				Vec([48, 25, 23, 15, 36, 35, 28, 5]),
				Vec([27, 46, 30, 2, 20, 26, 32, 40]),
				Vec([11, 9, 40, 38, 49, 19, 29, 12]),
				Vec([24, 1, 6, 21, 23, 1, 3, 27]),
				Vec([34, 27, 47, 10, 13, 3, 40, 44])])
'''

'''
This 8x8 of randomly generated values on [0,50] gave me 3 0's in a row.
It was the first matrix of any size I generated randomly!
That's freakishly unlikely. 

[10, 5, 27, 0, 0, 0, 50, 24]
[0, 38, 15, 28, 5, 7, 37, 2]
[25, 40, 6, 12, 1, 18, 14, 11]
[48, 25, 23, 15, 36, 35, 28, 5]
[27, 46, 30, 2, 20, 26, 32, 40]
[11, 9, 40, 38, 49, 19, 29, 12]
[24, 1, 6, 21, 23, 1, 3, 27]
[34, 27, 47, 10, 13, 3, 40, 44]

I shall investigate the properties of random.randint()'s default seed.
'''
