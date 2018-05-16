from PhysPy.NumTools import *
from PhysPy.PhysicalConstants import *
import decimal as d
d.getcontext().prec = 50


class Object:
	def __init__(self, position=Vec([0, 0, 0]), mass=0, velocity=Vec([0, 0, 0]), w=0):
		self.r = position
		self.m = mass
		self.v = velocity
		self.p = velocity*mass
		self.w = w

	def gmag(self, other):
		r_mag = Vec(self.r - other.r).mag()
		return (G*self.m*other.m)/r_mag

	def g(self, other):
		r_unit = Vec(self.r - other.r).unit()
		return r_unit*self.gmag(other)


class Sphere(Object):
	def __init__(
			self,
			position=Vec([0, 0, 0]), mass=0,
			velocity=Vec([0, 0, 0]),
			radius=0, w=0):

		super().__init__(position, mass, velocity, w)
		self.R = radius
		self.I = (self.R**2 * self.m * 2 / 5)  # describes a sphere of uniform density only
		self.L = self.I * self.w


class Disk(Object):
	def __init__(
			self,
			position=Vec([0, 0, 0]), mass=0,
			velocity=Vec([0, 0, 0]),
			radius=0, w=0):

		super().__init__(position, mass, velocity, w)
		self.R = radius
		self.I = self.R**2 * self.m / 2
		self.L = self.I * self.w


class Rod(Object):
	def __init__(
			self,
			position=Vec([0, 0, 0]), mass=0,
			velocity=Vec([0, 0, 0]),
			radius=0, length=0, w=0):

		super().__init__(position, mass, velocity, w)
		self.l = length
		self.R = radius
		self.Icenter = self.l**2 * self.m / 12
		self.Iend = self.l**2 * self.m / 3

	def Iabout(self, ratio):
		m = self.m
		above_about = self.l*ratio
		above_m = m*ratio
		below_about = self.l - above_about
		below_m = m-above_m
		return (above_about**2 * above_m + below_about**2 * below_m) / 3


class Particle:
	def __init__(
			self,
			pro=0, neu=0, ele=0, spin=0, q=None,
			mass=None, v=0, pos=Vec([0, 0, 0])):

		self.p = pro
		self.n = neu
		self.e = ele
		self.q = pro*1.6e-19 - ele*1.6e-19 if q is None else q
		self.m = (pro+neu)*1.7e-27 + ele*9e-31 if mass is None else mass
		self.pos = pos
		self.v = v
		self.spin = spin

		# if q is not None:
		#	 self.q = q
		# if mass is not None:
		#	 self.m = mass
		# if v is not None:
		#	 self.v = v
		# if spin is not None:
		# self.spin = spin

	def s_v(self, v):
		self.v = v

	def dist(self, other):
		return (self.pos-other.pos).mag()

	def F(self, other):
		return (self.q*other.q*CC) / self.dist(other)**2

	def U(self, other):
		return (self.q*other.q*CC) / self.dist(other)

	def rest(self):
		return self.m * c**2


class Atom:
	def __init__(
			self,
			name, symbol, atomic_number, protons, neutrons, electrons,
			mass, group, period, density, melting_point, boiling_point,
			specific_heat, electronegativity, youngs, radius, position=None,
			velocity=None, momentum=None, nucleus=False):

		self.name = name
		self.sym = symbol
		self.no = atomic_number

		self.pro = protons
		self.neu = neutrons
		self.ele = electrons if nucleus is False else 0

		self.m = mass

		self.group = group
		self.period = period
		self.dens = density
		self.mp = melting_point
		self.bp = boiling_point
		self.k = specific_heat
		self.x = electronegativity
		self.youngs = youngs

		self.R = radius
		self.r = position
		self.v = velocity
		self.p = momentum

	def s_mom(self, momentum):
		self.p = momentum

	def s_v(self, velocity):
		self.v = velocity

	def s_r(self, position):
		self.r = position

	def s_q(self, d_pro=None, d_neu=None):
		if d_pro is not None:
			self.pro += d_pro
		if d_neu is not None:
			self.neu += d_neu

	def nucle_on(self):
		self.ele = 0

	def nucle_off(self):
		self.ele = self.pro


class Spring:
	def __init__(self, ks, l0, dl=None):
		self.ks = ks
		self.l0 = l0
		self.dl = dl
		self.f = 0

	def stretch(self, dl):
		if self.dl is None:
			self.dl = dl
		else:
			self.dl += dl


class Planet:
	def __init__(
			self,
			mass, r=None, density=None,
			v=None):

		self.m = mass
		self.r = r

		if r is not None:
			self.r = r
			self.dens = mass/((4/3)*m.pi*r**3)
			self.i = (2/5) * self.m * self.r**2
		elif density is not None:
			self.dens = density
			self.r = (mass/((4/3)*m.pi*density))**(1/3)
			self.I = (2/5) * self.m * self.r**2

		if v is not None:
			self.v = v
			self.p = v*mass

	def i(self, r=None, I=None):
		if I is not None:
			self.I = I
		elif r is not None:
			self.r = r
			self.I = self.m * r**2
		elif self.r is not None:
			self.I = (2/5) * self.m * self.r**2
		else:
			return False

