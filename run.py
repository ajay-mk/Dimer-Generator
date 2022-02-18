# Dimer Generator by @ajay-mk
# github.com/ajay-mk/
# twitter.com/ajay_mk
# This program is free software: you can redistribute it and/or modify it
# If it is useful, I would appreciate an acknowledgment to the author

# This files controls the workflow of the program

import sys
from drivers.InputProcessing import *
from drivers.GenerateDimer import *
from drivers.Rotation import *
from drivers.Translation import *
from drivers.OutputFormatting import *
from drivers.GenerateDimer import *

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
reference_coords = monomer.coords
monomer.calculate_center_of_mass()
print()
Output(reference_coords, monomer.atoms).display_coordinates()
print()
print('The coordinates of the center of mass are: {}'.format(monomer.center_of_mass))
print()


if (np.array(monomer.center_of_mass) == np.array((0, 0, 0))).all():
    print()
    print("The center of mass is at the origin.")
else:
    move_to_com = input("Would you like to move center of mass to the origin? (y/n): ")
    if move_to_com == 'y':
        monomer.shift_to_center_of_mass()
        reference_coords = monomer.shifted_coords
        print()
        print("The centre of mass has been shifted to the origin.")
        print()
        Output(reference_coords, monomer.atoms).display_coordinates()
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
    translated_monomer = Translate(reference_coords, trans_dir, trans_distance)
    modified_coords = translated_monomer.translated_coords
if translation == 'n':
    translated_monomer = Translate(reference_coords, 'z', 0)
    modified_coords = translated_monomer.translated_coords
    
    
# Rotation
print()
rotation = input("Do you want to rotate the molecule? (y/n): ")
print()
if rotation == 'y':
    rotate_axis = input("Please provide the axis of rotation (x, y, z): ")
    rotate_angle = float(input("Please provide the angle for rotation (in degrees): "))
    rotate_angle = np.deg2rad(rotate_angle)
    rotated_monomer = Rotate(modified_coords, rotate_axis, rotate_angle)
    modified_coords = rotated_monomer.rotated_coords
if rotation == 'n':
    rotated_monomer = Rotate(modified_coords, 'z', 0)
    modified_coords = rotated_monomer.rotated_coords

print()
print("The final coordinates are:")
print()
dimer = Dimer_Geom(reference_coords, modified_coords, monomer.atoms, monomer.atoms)
Output(dimer.coords, dimer.atoms).display_coordinates()

#Saving the output
print()
save_file = input("Do you want save the coordinates as xyz file? (y/n): ")
if save_file == 'y':
    save_file = input("Please provide the file name for saving the coordinates: ")
    Output(dimer.coords, dimer.atoms).save_coordinates(save_file+'.xyz', input_file+'_dimer', len(dimer.atoms))
    print()
    print("The coordinates have been saved to {}.xyz!!".format(save_file))
    print()


### End of Program ###