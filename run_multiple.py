# Dimer Generator by @ajay-mk
# github.com/ajay-mk/
# twitter.com/ajay_mk
# This program is free software: you can redistribute it and/or modify it
# If it is useful, I would appreciate an acknowledgment to the author

# This files controls the workflow of the program
# Using this file, you can generate geometries using multiple momnomers. Example: benzene and coronene
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
parser.add_argument('-i1', '--input_file_1', help='Input file 1 in xyz format', required=True, type=str, metavar='')
parser.add_argument('-i2', '--input_file_2', help='Input file 2 in xyz format', required=True, type=str, metavar='')
parser.add_argument('-t', '--translate', help='Input translation direction', required=False, type=str, metavar='')
parser.add_argument('-td', '--translation_distance', help='Input translation distance', required=False, type=float, metavar='')
parser.add_argument('-r', '--rotate', help='Input rotation axis', required=False, type=str, metavar='')
parser.add_argument('-ra', '--rotation_angle', help='Input rotation angle in degrees', required=False, type=float, metavar='')
args = parser.parse_args()

if (args.input_file_1).endswith('.xyz'):
    input_file_1 = args.input_file_1
    print("Geometry obtained from: {}".format(input_file_1))
if (args.input_file_2).endswith('.xyz'):
    input_file_2 = args.input_file_2
    print("Geometry obtained from: {}".format(input_file_2))
else:
    print()
    print("Please provide an input files in xyz format")
    sys.exit()
    
monomer_1 = Monomer_Geom(input_file_1)
monomer_2 = Monomer_Geom(input_file_2)

monomer_1.calculate_center_of_mass()
monomer_1.shift_to_center_of_mass()
monomer_2.calculate_center_of_mass()
monomer_2.shift_to_center_of_mass()

if args.translate == 'x' or args.translate == 'y' or args.translate == 'z':
    trans_dir = args.translate
    trans_distance = args.translation_distance
    translated_monomer = Translate(monomer_2.shifted_coords, trans_dir, trans_distance)
    modified_coords = translated_monomer.translated_coords
else:
    translated_monomer = Translate(monomer_2.shifted_coords, 'z', 0)
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
dimer = Dimer_Geom(monomer_1.shifted_coords, modified_coords, monomer_1.atoms, monomer_2.atoms)
Output(dimer.coords, dimer.atoms).display_coordinates()

print()
#save_file = 'Dimer'+'_{}_{}'.format(args.translation_distance, args.rotation_angle)
save_file = input("Enter the name of the file to save the dimer coordinates: ")
save_file = save_file+'_dimer'
Output(dimer.coords, dimer.atoms).save_coordinates(save_file+'.xyz', save_file, len(dimer.atoms))
print()
print("The coordinates have been saved to {}.xyz!!".format(save_file))
print()