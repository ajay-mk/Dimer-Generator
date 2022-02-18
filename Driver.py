# Dimer Generator by @ajay-mk
# github.com/ajay-mk/
# twitter.com/ajay_mk
# This program is free software: you can redistribute it and/or modify it
# If it is useful, I would appreciate an acknowledgment to the author

# This files controls the workflow of the program

import sys
from InputProcessing import *
from GenerateDimer import *
from Rotation import *
from Translation import *
from OutputFormatting import *

# Printing some information
print("*** *** *** *** ***")
print("Dimer Generator")
print("by @ajay-mk")
print("Visit: https://github.com/ajay-mk/Dimer-Generator")
print("*** *** *** *** ***")

if (sys.argv[1]).endswith('.xyz'):
    input_file = sys.argv[1]
else:
    print("Please provide an input file in xyz format")
    sys.exit()

print("Geometry obtained from: {}".format(input_file))

monomer = Monomer_Geom(input_file)
monomer.calculate_center_of_mass()
mono_coords = monomer.coords
print()
DisplayCoordinates(mono_coords, monomer.atoms)
print()
print('The coordinates of the center of mass are: {}'.format(monomer.center_of_mass))
print()

if (np.array(monomer.center_of_mass) == np.array((0, 0, 1))).all():
    print()
    print("The center of mass is at the origin.")
else:
    move_to_com = input("Would you like to move the coordinates to the center of mass? (y/n): ")
    if move_to_com == 'y':
        monomer.shift_to_center_of_mass()
        mono_coords = monomer.shifted_coords
        print()
        print("The coordinates have been shifted to the center of mass.")
        print()
        DisplayCoordinates(mono_coords, monomer.atoms)
    if move_to_com == 'n':
        print()
        print("The coordinates will be in the original frame")

