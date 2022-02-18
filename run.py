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
print()
print("*** *** *** *** ***")
print("Dimer Generator")
print("by @ajay-mk")
print("Visit: https://github.com/ajay-mk/Dimer-Generator")
print("*** *** *** *** ***")
print()

if (sys.argv[1]).endswith('.xyz'):
    input_file = sys.argv[1]
else:
    print("Please provide an input file in xyz format")
    sys.exit()

print("Geometry obtained from: {}".format(input_file))

# Input reading and processing

monomer = Monomer_Geom(input_file)
mono_coords = monomer.coords
monomer.calculate_center_of_mass()
print()
DisplayCoordinates(mono_coords, monomer.atoms)
print()
print('The coordinates of the center of mass are: {}'.format(monomer.center_of_mass))
print()


def Move_to_CoM(coords):
    """Function to move the coordinates to the center of mass"""
    

if (np.array(monomer.center_of_mass) == np.array((0, 0, 0))).all():
    print()
    print("The center of mass is at the origin.")
else:
    move_to_com = input("Would you like to move center of mass to the origin? (y/n): ")
    if move_to_com == 'y':
        monomer.shift_to_center_of_mass()
        mono_coords = monomer.shifted_coords
        print()
        print("The centre of mass has been shifted to the origin.")
        print()
        DisplayCoordinates(mono_coords, monomer.atoms)
    if move_to_com == 'n':
        print()
        print("The coordinates will be in the original frame")
        print()
        
# Translation
print()
translation = input("Do you want to translate the molecule? (y/n): ")
print()
if translation == 'y':
    trans_dir = input("Please provide the direction (x, y, z): ")
    trans_distance = float(input("Please provide the distance for translation (in same units as the coordinates): "))
    translated_monomer = Translate(mono_coords, trans_dir, trans_distance)
    mono_coords = translated_monomer.translated_coords
    
print()
DisplayCoordinates(mono_coords, monomer.atoms)
