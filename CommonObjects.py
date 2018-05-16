from PhysPy.PhysicalObjects import *

# Sub-Atomic Particles
proton = Particle(pro=1, neu=0, ele=0)
electron = Particle(pro=0, neu=0, ele=1)
neutron = Particle(pro=0, neu=1, ele=0)

# Alpha Particle
alpha = Particle(pro=2, neu=2, ele=0)

# Planets & Celestial Bodies
sun = Planet(1.99e+30, r=6.95e+8)

mercury = Planet(3.30e+23, r=2.44e+6)
venus = Planet(4.87e+24, r=6.052e+6)

earth = Planet(5.9722e+24, r=6.3781e+6)
moon = Planet(1.27e+22, r=1.150e+6)

mars = Planet(6.42e+23, r=3.397e+6)
jupiter = Planet(1.9e+27, r=7.1492e+7)
saturn = Planet(5.68e+26, r=6.0268e+7)
uranus = Planet(8.68e+25, r=2.5559e+7)
neptune = Planet(1.02e+26, r=2.4766e+7)
