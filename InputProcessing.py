# Dimer Generator by @ajay-mk
# github.com/ajay-mk/

# This file contains the class and functions for input processing

import numpy as np
from mendeleev import element # https://pypi.org/project/mendeleev/

class Monomer_Geom:
    """Class for reading and processing the input file containing the coordinates of the monomer"""
    def __init__(self, filename):
        self.name = filename
        self.read_coordinates()
        self.calculate_center_of_mass()
        
    # Read coordinates from file
    def read_coordinates(self):
        self.coords = []
        self.atoms = []
        with open(self.name, 'r') as f:
            # Read lines except blank lines
            lines = f.readlines()
            # Read the first line
            self.num_atoms = int(lines[0])
            self.title = lines[1]
            # Read remaining lines ans split them to get the coordinates
            for line in lines[2:]:
                line = line.split()
                if line:
                    self.atoms.append(line[0])
                    self.coords.append([float(line[1]), float(line[2]), float(line[3])])
        self.coords = np.round(np.array(self.coords), 5)
        self.atoms = np.array(self.atoms)
        return self.num_atoms, self.title, self.coords, self.atoms
    
    # Calculate Center of Mass
    def calculate_center_of_mass(self):
        self.mass = []
        self.center_of_mass = []
        for atom in self.atoms:
            mass = element(atom).mass_number
            self.mass.append(mass)
        self.mass = np.array(self.mass)
        self.center_of_mass = np.average(self.coords, axis = 0, weights = self.mass)
        self.center_of_mass = np.round(self.center_of_mass, 5)
        return self.center_of_mass
    
    # Shift the coordinates to the center of mass
    def shift_to_center_of_mass(self):
        self.shifted_coords = self.coords - self.center_of_mass
        return self.shifted_coords

