# Dimer Generator by @ajay-mk
# github.com/ajay-mk/
# twitter.com/ajay_mk
# This program is free software: you can redistribute it and/or modify it
# If it is useful, I would appreciate an acknowledgment to the author

# This files controls the workflow of the program
# This program makes use of the argumets provided by the user in the command line

import sys
from drivers.InputProcessing import *
from drivers.GenerateDimer import *
from drivers.Rotation import *
from drivers.Translation import *
from drivers.OutputFormatting import *
from drivers.GenerateDimer import *
import argparse

parser = argparse.ArgumentParser(description='Inputting the parameters for transforming the dimer.')
parser.add_argument('-i', '--input_file', help='Input file in xyz format', required=True, type=str, metavar='')
parser.add_argument('-c', '--com_to_origin', help='Specify if centre of mass is translated to origin (y/n)', required=False, type=str, metavar='', default='n')
parser.add_argument('-t', '--translate', help='Input translation direction', required=False, type=str, metavar='')
parser.add_argument('-td', '--translation_distance', help='Input translation distance', required=False, type=float, metavar='')
parser.add_argument('-r', '--rotate', help='Input rotation axis', required=False, type=str, metavar='')
parser.add_argument('-ra', '--rotation_angle', help='Input rotation angle in degrees', required=False, type=float, metavar='')
args = parser.parse_args()

if (args.input_file).endswith('.xyz'):
    input_file = args.input_file
else:
    print()
    print("Please provide an input file in xyz format")
    sys.exit()

print("Geometry obtained from: {}".format(input_file))

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
    if args.com_to_origin == 'y':
        monomer.shift_to_center_of_mass()
        reference_coords = monomer.shifted_coords
        print()
        print("The centre of mass has been shifted to the origin.")
        print()
        Output(reference_coords, monomer.atoms).display_coordinates()
    if args.com_to_origin == 'n':
        print()
        print("The coordinates will be in the original frame")
        print()

if args.translate == 'x' or args.translate == 'y' or args.translate == 'z':
    trans_dir = args.translate
    trans_distance = args.translation_distance
    translated_monomer = Translate(reference_coords, trans_dir, trans_distance)
    modified_coords = translated_monomer.translated_coords
else:
    translated_monomer = Translate(reference_coords, 'z', 0)
    modified_coords = translated_monomer.translated_coords
    
if args.rotate == 'x' or args.rotate == 'y' or args.rotate == 'z':
    rotate_axis = args.rotate
    rotate_angle = args.rotation_angle
    rotate_angle = np.deg2rad(rotate_angle)
    rotated_monomer = Rotate(modified_coords, rotate_axis, rotate_angle)
    modified_coords = rotated_monomer.rotated_coords
else:
    rotated_monomer = Rotate(modified_coords, 'z', 0)
    modified_coords = rotated_monomer.rotated_coords
    
    
    
    
print()
print("The final coordinates are:")
print()
dimer = Dimer_Geom(reference_coords, modified_coords, monomer.atoms, monomer.atoms)
Output(dimer.coords, dimer.atoms).display_coordinates()

print()
save_file = input("Enter the name of the file to save the dimer coordinates: ")
save_file = save_file+'_dimer'
Output(dimer.coords, dimer.atoms).save_coordinates(save_file+'.xyz', save_file, len(dimer.atoms))
print()
print("The coordinates have been saved to {}.xyz!!".format(save_file))
print()