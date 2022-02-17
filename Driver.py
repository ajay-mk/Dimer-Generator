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

# Printing some information
print("*** *** *** *** ***")
print()
print("Dimer Generator")
print("by @ajay-mk")
print("Visit: https://github.com/ajay-mk/Dimer-Generator")
print()
print("*** *** *** *** ***")

if (sys.argv[1]).endswith('.xyz'):
    input_file = sys.argv[1]
else:
    print("Please provide an input file in xyz format")
    sys.exit()

print("Input file:", input_file)

monomer = Monomer_Geom(input_file)
monomer.calculate_center_of_mass()
print()
monomer.display_coordinates()
print()
print('The coordinates of the center of mass are:')
print(monomer.center_of_mass)
