'''
Defines classes for all 118 elements on the periodic table.
Each element inherits from the Atom class
Each element also has its own child class which represents an atomic nucleus of that element.
'''

from PhysPy.PhysicalObjects import *

# class defining an uncharged, isotopally typical Hydrogen atom
class H(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Hydrogen",
                "H",
                1,
                1,
                0,
                1,
                1.008,
                1,
                1,
                8.988e-05,
                14.01,
                20.28,
                14.304,
                2.2,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Hydrogen nucleus
class H_n(H):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Helium atom
class He(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Helium",
                "He",
                2,
                2,
                2,
                2,
                4.0026022,
                18,
                1,
                0.0001785,
                None,
                4.22,
                5.193,
                None,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Helium nucleus
class He_n(He):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Lithium atom
class Li(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Lithium",
                "Li",
                3,
                3,
                4,
                3,
                6.94,
                1,
                2,
                0.534,
                453.69,
                1560.0,
                3.582,
                0.98,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Lithium nucleus
class Li_n(Li):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Beryllium atom
class Be(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Beryllium",
                "Be",
                4,
                4,
                5,
                4,
                9.01218315,
                2,
                2,
                1.85,
                1560.0,
                2742.0,
                1.825,
                1.57,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Beryllium nucleus
class Be_n(Be):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Boron atom
class B(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Boron",
                "B",
                5,
                5,
                6,
                5,
                10.81,
                13,
                2,
                2.34,
                2349.0,
                4200.0,
                1.026,
                2.04,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Boron nucleus
class B_n(B):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Carbon atom
class C(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Carbon",
                "C",
                6,
                6,
                6,
                6,
                12.011,
                14,
                2,
                2.267,
                3800.0,
                4300.0,
                0.709,
                2.55,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Carbon nucleus
class C_n(C):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Nitrogen atom
class N(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Nitrogen",
                "N",
                7,
                7,
                7,
                7,
                14.007,
                15,
                2,
                0.0012506,
                63.15,
                77.36,
                1.04,
                3.04,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Nitrogen nucleus
class N_n(N):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Oxygen atom
class O(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Oxygen",
                "O",
                8,
                8,
                8,
                8,
                15.999,
                16,
                2,
                0.001429,
                54.36,
                90.2,
                0.918,
                3.44,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Oxygen nucleus
class O_n(O):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Fluorine atom
class F(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Fluorine",
                "F",
                9,
                9,
                10,
                9,
                18.9984031636,
                17,
                2,
                0.001696,
                53.53,
                85.03,
                0.824,
                3.98,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Fluorine nucleus
class F_n(F):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Neon atom
class Ne(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Neon",
                "Ne",
                10,
                10,
                10,
                10,
                20.17976,
                18,
                2,
                0.0008999,
                24.56,
                27.07,
                1.03,
                None,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Neon nucleus
class Ne_n(Ne):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Sodium atom
class Na(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Sodium",
                "Na",
                11,
                11,
                12,
                11,
                22.989769282,
                1,
                3,
                0.971,
                370.87,
                1156.0,
                1.228,
                0.93,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Sodium nucleus
class Na_n(Na):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Magnesium atom
class Mg(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Magnesium",
                "Mg",
                12,
                12,
                12,
                12,
                24.305,
                2,
                3,
                1.738,
                923.0,
                1363.0,
                1.023,
                1.31,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Magnesium nucleus
class Mg_n(Mg):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Aluminium atom
class Al(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Aluminium",
                "Al",
                13,
                13,
                14,
                13,
                26.98153857,
                13,
                3,
                2.698,
                933.47,
                2792.0,
                0.897,
                1.61,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Aluminium nucleus
class Al_n(Al):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Silicon atom
class Si(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Silicon",
                "Si",
                14,
                14,
                14,
                14,
                28.085,
                14,
                3,
                2.3296,
                1687.0,
                3538.0,
                0.705,
                1.9,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Silicon nucleus
class Si_n(Si):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Phosphorus atom
class P(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Phosphorus",
                "P",
                15,
                15,
                16,
                15,
                30.9737619985,
                15,
                3,
                1.82,
                317.3,
                550.0,
                0.769,
                2.19,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Phosphorus nucleus
class P_n(P):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Sulfur atom
class S(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Sulfur",
                "S",
                16,
                16,
                16,
                16,
                32.06,
                16,
                3,
                2.067,
                388.36,
                717.87,
                0.71,
                2.58,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Sulfur nucleus
class S_n(S):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Chlorine atom
class Cl(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Chlorine",
                "Cl",
                17,
                17,
                18,
                17,
                35.45,
                17,
                3,
                0.003214,
                171.6,
                239.11,
                0.479,
                3.16,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Chlorine nucleus
class Cl_n(Cl):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Argon atom
class Ar(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Argon",
                "Ar",
                18,
                18,
                22,
                18,
                39.9481,
                18,
                3,
                0.0017837,
                83.8,
                87.3,
                0.52,
                None,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Argon nucleus
class Ar_n(Ar):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Potassium atom
class K(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Potassium",
                "K",
                19,
                19,
                20,
                19,
                39.09831,
                1,
                4,
                0.862,
                336.53,
                1032.0,
                0.757,
                0.82,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Potassium nucleus
class K_n(K):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Calcium atom
class Ca(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Calcium",
                "Ca",
                20,
                20,
                20,
                20,
                40.0784,
                2,
                4,
                1.54,
                1115.0,
                1757.0,
                0.647,
                1.0,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Calcium nucleus
class Ca_n(Ca):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Scandium atom
class Sc(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Scandium",
                "Sc",
                21,
                21,
                24,
                21,
                44.9559085,
                3,
                4,
                2.989,
                1814.0,
                3109.0,
                0.568,
                1.36,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Scandium nucleus
class Sc_n(Sc):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Titanium atom
class Ti(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Titanium",
                "Ti",
                22,
                22,
                26,
                22,
                47.8671,
                4,
                4,
                4.54,
                1941.0,
                3560.0,
                0.523,
                1.54,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Titanium nucleus
class Ti_n(Ti):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Vanadium atom
class V(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Vanadium",
                "V",
                23,
                23,
                28,
                23,
                50.94151,
                5,
                4,
                6.11,
                2183.0,
                3680.0,
                0.489,
                1.63,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Vanadium nucleus
class V_n(V):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Chromium atom
class Cr(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Chromium",
                "Cr",
                24,
                24,
                28,
                24,
                51.99616,
                6,
                4,
                7.15,
                2180.0,
                2944.0,
                0.449,
                1.66,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Chromium nucleus
class Cr_n(Cr):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Manganese atom
class Mn(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Manganese",
                "Mn",
                25,
                25,
                30,
                25,
                54.9380443,
                7,
                4,
                7.44,
                1519.0,
                2334.0,
                0.479,
                1.55,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Manganese nucleus
class Mn_n(Mn):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Iron atom
class Fe(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Iron",
                "Fe",
                26,
                26,
                30,
                26,
                55.8452,
                8,
                4,
                7.874,
                1811.0,
                3134.0,
                0.449,
                1.83,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Iron nucleus
class Fe_n(Fe):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Cobalt atom
class Co(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Cobalt",
                "Co",
                27,
                27,
                32,
                27,
                58.9331944,
                9,
                4,
                8.86,
                1768.0,
                3200.0,
                0.421,
                1.88,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Cobalt nucleus
class Co_n(Co):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Nickel atom
class Ni(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Nickel",
                "Ni",
                28,
                28,
                31,
                28,
                58.69344,
                10,
                4,
                8.912,
                1728.0,
                3186.0,
                0.444,
                1.91,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Nickel nucleus
class Ni_n(Ni):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Copper atom
class Cu(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Copper",
                "Cu",
                29,
                29,
                35,
                29,
                63.5463,
                11,
                4,
                8.96,
                1357.77,
                2835.0,
                0.385,
                1.9,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Copper nucleus
class Cu_n(Cu):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Zinc atom
class Zn(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Zinc",
                "Zn",
                30,
                30,
                35,
                30,
                65.382,
                12,
                4,
                7.134,
                692.88,
                1180.0,
                0.388,
                1.65,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Zinc nucleus
class Zn_n(Zn):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Gallium atom
class Ga(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Gallium",
                "Ga",
                31,
                31,
                39,
                31,
                69.7231,
                13,
                4,
                5.907,
                302.9146,
                2673.0,
                0.371,
                1.81,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Gallium nucleus
class Ga_n(Ga):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Germanium atom
class Ge(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Germanium",
                "Ge",
                32,
                32,
                41,
                32,
                72.6308,
                14,
                4,
                5.323,
                1211.4,
                3106.0,
                0.32,
                2.01,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Germanium nucleus
class Ge_n(Ge):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Arsenic atom
class As(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Arsenic",
                "As",
                33,
                33,
                42,
                33,
                74.9215956,
                15,
                4,
                5.776,
                1090.0,
                887.0,
                0.329,
                2.18,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Arsenic nucleus
class As_n(As):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Selenium atom
class Se(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Selenium",
                "Se",
                34,
                34,
                45,
                34,
                78.9718,
                16,
                4,
                4.809,
                453.0,
                958.0,
                0.321,
                2.55,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Selenium nucleus
class Se_n(Se):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Bromine atom
class Br(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Bromine",
                "Br",
                35,
                35,
                45,
                35,
                79.904,
                17,
                4,
                3.122,
                265.8,
                332.0,
                0.474,
                2.96,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Bromine nucleus
class Br_n(Br):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Krypton atom
class Kr(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Krypton",
                "Kr",
                36,
                36,
                48,
                36,
                83.7982,
                18,
                4,
                0.003733,
                115.79,
                119.93,
                0.248,
                3.0,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Krypton nucleus
class Kr_n(Kr):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Rubidium atom
class Rb(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Rubidium",
                "Rb",
                37,
                37,
                48,
                37,
                85.46783,
                1,
                5,
                1.532,
                312.46,
                961.0,
                0.363,
                0.82,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Rubidium nucleus
class Rb_n(Rb):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Strontium atom
class Sr(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Strontium",
                "Sr",
                38,
                38,
                50,
                38,
                87.621,
                2,
                5,
                2.64,
                1050.0,
                1655.0,
                0.301,
                0.95,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Strontium nucleus
class Sr_n(Sr):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Yttrium atom
class Y(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Yttrium",
                "Y",
                39,
                39,
                50,
                39,
                88.905842,
                3,
                5,
                4.469,
                1799.0,
                3609.0,
                0.298,
                1.22,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Yttrium nucleus
class Y_n(Y):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Zirconium atom
class Zr(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Zirconium",
                "Zr",
                40,
                40,
                51,
                40,
                91.2242,
                4,
                5,
                6.506,
                2128.0,
                4682.0,
                0.278,
                1.33,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Zirconium nucleus
class Zr_n(Zr):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Niobium atom
class Nb(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Niobium",
                "Nb",
                41,
                41,
                52,
                41,
                92.906372,
                5,
                5,
                8.57,
                2750.0,
                5017.0,
                0.265,
                1.6,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Niobium nucleus
class Nb_n(Nb):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Molybdenum atom
class Mo(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Molybdenum",
                "Mo",
                42,
                42,
                54,
                42,
                95.951,
                6,
                5,
                10.22,
                2896.0,
                4912.0,
                0.251,
                2.16,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Molybdenum nucleus
class Mo_n(Mo):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Technetium atom
class Tc(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Technetium",
                "Tc",
                43,
                43,
                55,
                43,
                98.0,
                7,
                5,
                11.5,
                2430.0,
                4538.0,
                None,
                1.9,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Technetium nucleus
class Tc_n(Tc):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Ruthenium atom
class Ru(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Ruthenium",
                "Ru",
                44,
                44,
                57,
                44,
                101.072,
                8,
                5,
                12.37,
                2607.0,
                4423.0,
                0.238,
                2.2,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Ruthenium nucleus
class Ru_n(Ru):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Rhodium atom
class Rh(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Rhodium",
                "Rh",
                45,
                45,
                58,
                45,
                102.905502,
                9,
                5,
                12.41,
                2237.0,
                3968.0,
                0.243,
                2.28,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Rhodium nucleus
class Rh_n(Rh):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Palladium atom
class Pd(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Palladium",
                "Pd",
                46,
                46,
                60,
                46,
                106.421,
                10,
                5,
                12.02,
                1828.05,
                3236.0,
                0.244,
                2.2,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Palladium nucleus
class Pd_n(Pd):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Silver atom
class Ag(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Silver",
                "Ag",
                47,
                47,
                61,
                47,
                107.86822,
                11,
                5,
                10.501,
                1234.93,
                2435.0,
                0.235,
                1.93,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Silver nucleus
class Ag_n(Ag):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Cadmium atom
class Cd(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Cadmium",
                "Cd",
                48,
                48,
                64,
                48,
                112.4144,
                12,
                5,
                8.69,
                594.22,
                1040.0,
                0.232,
                1.69,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Cadmium nucleus
class Cd_n(Cd):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Indium atom
class In(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Indium",
                "In",
                49,
                49,
                66,
                49,
                114.8181,
                13,
                5,
                7.31,
                429.75,
                2345.0,
                0.233,
                1.78,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Indium nucleus
class In_n(In):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Tin atom
class Sn(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Tin",
                "Sn",
                50,
                50,
                69,
                50,
                118.7107,
                14,
                5,
                7.287,
                505.08,
                2875.0,
                0.228,
                1.96,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Tin nucleus
class Sn_n(Sn):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Antimony atom
class Sb(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Antimony",
                "Sb",
                51,
                51,
                71,
                51,
                121.7601,
                15,
                5,
                6.685,
                903.78,
                1860.0,
                0.207,
                2.05,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Antimony nucleus
class Sb_n(Sb):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Tellurium atom
class Te(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Tellurium",
                "Te",
                52,
                52,
                76,
                52,
                127.603,
                16,
                5,
                6.232,
                722.66,
                1261.0,
                0.202,
                2.1,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Tellurium nucleus
class Te_n(Te):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Iodine atom
class I(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Iodine",
                "I",
                53,
                53,
                74,
                53,
                126.904473,
                17,
                5,
                4.93,
                386.85,
                457.4,
                0.214,
                2.66,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Iodine nucleus
class I_n(I):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Xenon atom
class Xe(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Xenon",
                "Xe",
                54,
                54,
                77,
                54,
                131.2936,
                18,
                5,
                0.005887,
                161.4,
                165.03,
                0.158,
                2.6,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Xenon nucleus
class Xe_n(Xe):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Caesium atom
class Cs(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Caesium",
                "Cs",
                55,
                55,
                78,
                55,
                132.905451966,
                1,
                6,
                1.873,
                301.59,
                944.0,
                0.242,
                0.79,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Caesium nucleus
class Cs_n(Cs):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Barium atom
class Ba(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Barium",
                "Ba",
                56,
                56,
                81,
                56,
                137.3277,
                2,
                6,
                3.594,
                1000.0,
                2170.0,
                0.204,
                0.89,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Barium nucleus
class Ba_n(Ba):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Lanthanum atom
class La(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Lanthanum",
                "La",
                57,
                57,
                82,
                57,
                138.905477,
                3,
                6,
                6.145,
                1193.0,
                3737.0,
                0.195,
                1.1,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Lanthanum nucleus
class La_n(La):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Cerium atom
class Ce(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Cerium",
                "Ce",
                58,
                58,
                82,
                58,
                140.1161,
                None,
                6,
                6.77,
                1068.0,
                3716.0,
                0.192,
                1.12,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Cerium nucleus
class Ce_n(Ce):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Praseodymium atom
class Pr(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Praseodymium",
                "Pr",
                59,
                59,
                82,
                59,
                140.907662,
                None,
                6,
                6.773,
                1208.0,
                3793.0,
                0.193,
                1.13,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Praseodymium nucleus
class Pr_n(Pr):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Neodymium atom
class Nd(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Neodymium",
                "Nd",
                60,
                60,
                84,
                60,
                144.2423,
                None,
                6,
                7.007,
                1297.0,
                3347.0,
                0.19,
                1.14,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Neodymium nucleus
class Nd_n(Nd):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Promethium atom
class Pm(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Promethium",
                "Pm",
                61,
                61,
                84,
                61,
                145.0,
                None,
                6,
                7.26,
                1315.0,
                3273.0,
                None,
                1.13,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Promethium nucleus
class Pm_n(Pm):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Samarium atom
class Sm(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Samarium",
                "Sm",
                62,
                62,
                88,
                62,
                150.362,
                None,
                6,
                7.52,
                1345.0,
                2067.0,
                0.197,
                1.17,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Samarium nucleus
class Sm_n(Sm):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Europium atom
class Eu(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Europium",
                "Eu",
                63,
                63,
                89,
                63,
                151.9641,
                None,
                6,
                5.243,
                1099.0,
                1802.0,
                0.182,
                1.2,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Europium nucleus
class Eu_n(Eu):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Gadolinium atom
class Gd(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Gadolinium",
                "Gd",
                64,
                64,
                93,
                64,
                157.253,
                None,
                6,
                7.895,
                1585.0,
                3546.0,
                0.236,
                1.2,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Gadolinium nucleus
class Gd_n(Gd):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Terbium atom
class Tb(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Terbium",
                "Tb",
                65,
                65,
                94,
                65,
                158.925352,
                None,
                6,
                8.229,
                1629.0,
                3503.0,
                0.182,
                1.2,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Terbium nucleus
class Tb_n(Tb):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Dysprosium atom
class Dy(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Dysprosium",
                "Dy",
                66,
                66,
                97,
                66,
                162.5001,
                None,
                6,
                8.55,
                1680.0,
                2840.0,
                0.17,
                1.22,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Dysprosium nucleus
class Dy_n(Dy):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Holmium atom
class Ho(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Holmium",
                "Ho",
                67,
                67,
                98,
                67,
                164.930332,
                None,
                6,
                8.795,
                1734.0,
                2993.0,
                0.165,
                1.23,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Holmium nucleus
class Ho_n(Ho):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Erbium atom
class Er(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Erbium",
                "Er",
                68,
                68,
                99,
                68,
                167.2593,
                None,
                6,
                9.066,
                1802.0,
                3141.0,
                0.168,
                1.24,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Erbium nucleus
class Er_n(Er):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Thulium atom
class Tm(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Thulium",
                "Tm",
                69,
                69,
                100,
                69,
                168.934222,
                None,
                6,
                9.321,
                1818.0,
                2223.0,
                0.16,
                1.25,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Thulium nucleus
class Tm_n(Tm):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Ytterbium atom
class Yb(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Ytterbium",
                "Yb",
                70,
                70,
                103,
                70,
                173.0451,
                None,
                6,
                6.965,
                1097.0,
                1469.0,
                0.155,
                1.1,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Ytterbium nucleus
class Yb_n(Yb):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Lutetium atom
class Lu(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Lutetium",
                "Lu",
                71,
                71,
                104,
                71,
                174.96681,
                None,
                6,
                9.84,
                1925.0,
                3675.0,
                0.154,
                1.27,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Lutetium nucleus
class Lu_n(Lu):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Hafnium atom
class Hf(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Hafnium",
                "Hf",
                72,
                72,
                106,
                72,
                178.492,
                4,
                6,
                13.31,
                2506.0,
                4876.0,
                0.144,
                1.3,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Hafnium nucleus
class Hf_n(Hf):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Tantalum atom
class Ta(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Tantalum",
                "Ta",
                73,
                73,
                108,
                73,
                180.947882,
                5,
                6,
                16.654,
                3290.0,
                5731.0,
                0.14,
                1.5,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Tantalum nucleus
class Ta_n(Ta):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Tungsten atom
class W(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Tungsten",
                "W",
                74,
                74,
                110,
                74,
                183.841,
                6,
                6,
                19.25,
                3695.0,
                5828.0,
                0.132,
                2.36,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Tungsten nucleus
class W_n(W):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Rhenium atom
class Re(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Rhenium",
                "Re",
                75,
                75,
                111,
                75,
                186.2071,
                7,
                6,
                21.02,
                3459.0,
                5869.0,
                0.137,
                1.9,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Rhenium nucleus
class Re_n(Re):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Osmium atom
class Os(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Osmium",
                "Os",
                76,
                76,
                114,
                76,
                190.233,
                8,
                6,
                22.61,
                3306.0,
                5285.0,
                0.13,
                2.2,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Osmium nucleus
class Os_n(Os):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Iridium atom
class Ir(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Iridium",
                "Ir",
                77,
                77,
                115,
                77,
                192.2173,
                9,
                6,
                22.56,
                2719.0,
                4701.0,
                0.131,
                2.2,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Iridium nucleus
class Ir_n(Ir):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Platinum atom
class Pt(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Platinum",
                "Pt",
                78,
                78,
                117,
                78,
                195.0849,
                10,
                6,
                21.46,
                2041.4,
                4098.0,
                0.133,
                2.28,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Platinum nucleus
class Pt_n(Pt):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Gold atom
class Au(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Gold",
                "Au",
                79,
                79,
                118,
                79,
                196.9665695,
                11,
                6,
                19.282,
                1337.33,
                3129.0,
                0.129,
                2.54,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Gold nucleus
class Au_n(Au):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Mercury atom
class Hg(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Mercury",
                "Hg",
                80,
                80,
                121,
                80,
                200.5923,
                12,
                6,
                13.5336,
                234.43,
                629.88,
                0.14,
                2.0,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Mercury nucleus
class Hg_n(Hg):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Thallium atom
class Tl(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Thallium",
                "Tl",
                81,
                81,
                123,
                81,
                204.38,
                13,
                6,
                11.85,
                577.0,
                1746.0,
                0.129,
                1.62,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Thallium nucleus
class Tl_n(Tl):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Lead atom
class Pb(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Lead",
                "Pb",
                82,
                82,
                125,
                82,
                207.21,
                14,
                6,
                11.342,
                600.61,
                2022.0,
                0.129,
                1.87,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Lead nucleus
class Pb_n(Pb):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Bismuth atom
class Bi(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Bismuth",
                "Bi",
                83,
                83,
                126,
                83,
                208.980401,
                15,
                6,
                9.807,
                544.7,
                1837.0,
                0.122,
                2.02,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Bismuth nucleus
class Bi_n(Bi):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Polonium atom
class Po(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Polonium",
                "Po",
                84,
                84,
                125,
                84,
                209.0,
                16,
                6,
                9.32,
                527.0,
                1235.0,
                None,
                2.0,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Polonium nucleus
class Po_n(Po):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Astatine atom
class At(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Astatine",
                "At",
                85,
                85,
                125,
                85,
                210.0,
                17,
                6,
                7.0,
                575.0,
                610.0,
                None,
                2.2,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Astatine nucleus
class At_n(At):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Radon atom
class Rn(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Radon",
                "Rn",
                86,
                86,
                136,
                86,
                222.0,
                18,
                6,
                0.00973,
                202.0,
                211.3,
                0.094,
                2.2,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Radon nucleus
class Rn_n(Rn):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Francium atom
class Fr(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Francium",
                "Fr",
                87,
                87,
                136,
                87,
                223.0,
                1,
                7,
                1.87,
                300.0,
                950.0,
                None,
                0.7,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Francium nucleus
class Fr_n(Fr):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Radium atom
class Ra(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Radium",
                "Ra",
                88,
                88,
                138,
                88,
                226.0,
                2,
                7,
                5.5,
                973.0,
                2010.0,
                0.094,
                0.9,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Radium nucleus
class Ra_n(Ra):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Actinium atom
class Ac(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Actinium",
                "Ac",
                89,
                89,
                138,
                89,
                227.0,
                3,
                7,
                10.07,
                1323.0,
                3471.0,
                0.12,
                1.1,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Actinium nucleus
class Ac_n(Ac):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Thorium atom
class Th(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Thorium",
                "Th",
                90,
                90,
                142,
                90,
                232.03774,
                None,
                7,
                11.72,
                2115.0,
                5061.0,
                0.113,
                1.3,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Thorium nucleus
class Th_n(Th):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Protactinium atom
class Pa(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Protactinium",
                "Pa",
                91,
                91,
                140,
                91,
                231.035882,
                None,
                7,
                15.37,
                1841.0,
                4300.0,
                None,
                1.5,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Protactinium nucleus
class Pa_n(Pa):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Uranium atom
class U(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Uranium",
                "U",
                92,
                92,
                146,
                92,
                238.028913,
                None,
                7,
                18.95,
                1405.3,
                4404.0,
                0.116,
                1.38,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Uranium nucleus
class U_n(U):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Neptunium atom
class Np(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Neptunium",
                "Np",
                93,
                93,
                144,
                93,
                237.0,
                None,
                7,
                20.45,
                917.0,
                4273.0,
                None,
                1.36,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Neptunium nucleus
class Np_n(Np):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Plutonium atom
class Pu(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Plutonium",
                "Pu",
                94,
                94,
                150,
                94,
                244.0,
                None,
                7,
                19.84,
                912.5,
                3501.0,
                None,
                1.28,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Plutonium nucleus
class Pu_n(Pu):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Americium atom
class Am(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Americium",
                "Am",
                95,
                95,
                148,
                95,
                243.0,
                None,
                7,
                13.69,
                1449.0,
                2880.0,
                None,
                1.13,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Americium nucleus
class Am_n(Am):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Curium atom
class Cm(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Curium",
                "Cm",
                96,
                96,
                151,
                96,
                247.0,
                None,
                7,
                13.51,
                1613.0,
                3383.0,
                None,
                1.28,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Curium nucleus
class Cm_n(Cm):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Berkelium atom
class Bk(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Berkelium",
                "Bk",
                97,
                97,
                150,
                97,
                247.0,
                None,
                7,
                14.79,
                1259.0,
                2900.0,
                None,
                1.3,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Berkelium nucleus
class Bk_n(Bk):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Californium atom
class Cf(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Californium",
                "Cf",
                98,
                98,
                153,
                98,
                251.0,
                None,
                7,
                15.1,
                1173.0,
                1743.0,
                None,
                1.3,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Californium nucleus
class Cf_n(Cf):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Einsteinium atom
class Es(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Einsteinium",
                "Es",
                99,
                99,
                153,
                99,
                252.0,
                None,
                7,
                8.84,
                1133.0,
                1269.0,
                None,
                1.3,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Einsteinium nucleus
class Es_n(Es):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Fermium atom
class Fm(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Fermium",
                "Fm",
                100,
                100,
                157,
                100,
                257.0,
                None,
                7,
                9.7,
                1125.0,
                None,
                None,
                1.3,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Fermium nucleus
class Fm_n(Fm):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Mendelevium atom
class Md(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Mendelevium",
                "Md",
                101,
                101,
                157,
                101,
                258.0,
                None,
                7,
                10.3,
                1100.0,
                None,
                None,
                1.3,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Mendelevium nucleus
class Md_n(Md):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Nobelium atom
class No(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Nobelium",
                "No",
                102,
                102,
                157,
                102,
                259.0,
                None,
                7,
                9.9,
                1100.0,
                None,
                None,
                1.3,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Nobelium nucleus
class No_n(No):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Lawrencium atom
class Lr(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Lawrencium",
                "Lr",
                103,
                103,
                163,
                103,
                266.0,
                None,
                7,
                15.6,
                1900.0,
                None,
                None,
                1.3,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Lawrencium nucleus
class Lr_n(Lr):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Rutherfordium atom
class Rf(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Rutherfordium",
                "Rf",
                104,
                104,
                163,
                104,
                267.0,
                4,
                7,
                23.2,
                2400.0,
                5800.0,
                None,
                None,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Rutherfordium nucleus
class Rf_n(Rf):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Dubnium atom
class Db(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Dubnium",
                "Db",
                105,
                105,
                163,
                105,
                268.0,
                5,
                7,
                29.3,
                None,
                None,
                None,
                None,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Dubnium nucleus
class Db_n(Db):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Seaborgium atom
class Sg(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Seaborgium",
                "Sg",
                106,
                106,
                163,
                106,
                269.0,
                6,
                7,
                35.0,
                None,
                None,
                None,
                None,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Seaborgium nucleus
class Sg_n(Sg):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Bohrium atom
class Bh(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Bohrium",
                "Bh",
                107,
                107,
                163,
                107,
                270.0,
                7,
                7,
                37.1,
                None,
                None,
                None,
                None,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Bohrium nucleus
class Bh_n(Bh):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Hassium atom
class Hs(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Hassium",
                "Hs",
                108,
                108,
                169,
                108,
                277.0,
                8,
                7,
                40.7,
                None,
                None,
                None,
                None,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Hassium nucleus
class Hs_n(Hs):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Meitnerium atom
class Mt(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Meitnerium",
                "Mt",
                109,
                109,
                169,
                109,
                278.0,
                9,
                7,
                37.4,
                None,
                None,
                None,
                None,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Meitnerium nucleus
class Mt_n(Mt):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Darmstadtium atom
class Ds(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Darmstadtium",
                "Ds",
                110,
                110,
                171,
                110,
                281.0,
                10,
                7,
                34.8,
                None,
                None,
                None,
                None,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Darmstadtium nucleus
class Ds_n(Ds):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Roentgenium atom
class Rg(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Roentgenium",
                "Rg",
                111,
                111,
                171,
                111,
                282.0,
                11,
                7,
                28.7,
                None,
                None,
                None,
                None,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Roentgenium nucleus
class Rg_n(Rg):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Copernicium atom
class Cn(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Copernicium",
                "Cn",
                112,
                112,
                173,
                112,
                285.0,
                12,
                7,
                23.7,
                None,
                357.0,
                None,
                None,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Copernicium nucleus
class Cn_n(Cn):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Nihonium atom
class Nh(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Nihonium",
                "Nh",
                113,
                113,
                173,
                113,
                286.0,
                13,
                7,
                16.0,
                700.0,
                1400.0,
                None,
                None,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Nihonium nucleus
class Nh_n(Nh):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Flerovium atom
class Fl(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Flerovium",
                "Fl",
                114,
                114,
                175,
                114,
                289.0,
                14,
                7,
                14.0,
                None,
                210.0,
                None,
                None,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Flerovium nucleus
class Fl_n(Fl):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Moscovium atom
class Mc(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Moscovium",
                "Mc",
                115,
                115,
                175,
                115,
                290.0,
                15,
                7,
                13.5,
                700.0,
                1400.0,
                None,
                None,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Moscovium nucleus
class Mc_n(Mc):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Livermorium atom
class Lv(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Livermorium",
                "Lv",
                116,
                116,
                177,
                116,
                293.0,
                16,
                7,
                12.9,
                709.0,
                1085.0,
                None,
                None,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Livermorium nucleus
class Lv_n(Lv):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Tennessine atom
class Ts(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Tennessine",
                "Ts",
                117,
                117,
                177,
                117,
                294.0,
                17,
                7,
                7.2,
                723.0,
                883.0,
                None,
                None,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Tennessine nucleus
class Ts_n(Ts):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


# class defining an uncharged, isotopally typical Oganesson atom
class Og(Atom):
    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):
        super().__init__(
                "Oganesson",
                "Og",
                118,
                118,
                176,
                118,
                294.0,
                18,
                7,
                5.0,
                None,
                350.0,
                None,
                None,
                position=position,
                velocity=velocity,
                nucleus=nucleus
        )


# class defining an isotopally typical Oganesson nucleus
class Og_n(Og):
    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):
        super().__init__(position, velocity, nucleus=True)


