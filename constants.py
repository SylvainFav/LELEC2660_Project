'''
This file only contains the constants.
'''


class Core:
    def __init__(self, name, L, l, c, h, H):
        self.name = name
        self.L, self.H, self.c = L, H, c
        self.l, self.h = l, h

    @property
    def Wa(self):
        return (self.l - self.c) * self.h

    def __repr__(self):
        return self.name


from math import pi as pi

# general constants
Pin_min, Pin_max = 30, 300
Pnom = 100
Vout = 24
Vin = 300
vgrid, fgrid = 220, 50
fsw = 100e3

# suggested constants
VDSS_max = 650
J = 5

# datasheets constants
mu_r = 2000
cores = [Core("E55/28/21", 56.2, 37.5, 17.2, 18.5, 27.5),
         Core("E30/15/7", 30.8, 19.5, 7.2, 9.7, 15.0),
         Core("E32/16/9", 32.0, 22.7, 9.5, 11.2, 16.4),
         Core("E42/21/15", 43.0, 29.5, 12.2, 14.8, 21.0),
         Core("E42/21/20", 43.0, 29.5, 12.2, 14.8, 21.0)]

# derived constants
mu = mu_r * 4e-7 * pi
Vin = 300

# choosen constants
alpha = 2
margin = 0.05 * VDSS_max
