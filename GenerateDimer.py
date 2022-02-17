# Dimer Generator by @ajay-mk
# github.com/ajay-mk/

# This file contains the class and functions for generating the dimer geometry

import numpy as np, pandas as pd

class Dimer_Geom:
    """Class for generating the dimer geometry"""
    def __init__(self, monomer_geom, modified_monomer_geom, monomer_atoms, modified_monomer_atoms):
        self.coords = []
        self.atoms = []
        self.monomer_geom = monomer_geom
        self.monomer_atoms = monomer_atoms
        self.modified_monomer_geom = modified_monomer_geom
        self.modified_monomer_atoms = modified_monomer_atoms
        self.generate_dimer_geometry()
        
    def generate_dimer_geometry(self):
        self.coords = np.concatenate((self.monomer_geom, self.modified_monomer_geom), axis=0)
        self.atoms = np.concatenate((self.monomer_atoms, self.modified_monomer_atoms), axis=0)
        return self.coords, self.atoms
    
    def display_coordinates(self):
        self.df = pd.DataFrame(self.coords, columns=['X', 'Y', 'Z'])
        self.df.insert(0, 'Atom', self.atoms)
        self.df = self.df.reset_index(drop=True)
        print("Dimer Geometry \n")
        print(self.df.to_string(index=False))
        return self.df
    