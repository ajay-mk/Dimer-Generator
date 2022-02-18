# Dimer Generator by @ajay-mk
# github.com/ajay-mk/

# This file contains the class and functions for fromatting the output

import pandas as pd

class DisplayCoordinates:
    
    def __init__(self, coords, atoms):
        self.coords = coords
        self.atoms = atoms
        self.display_coordinates()
    
    def display_coordinates(self):
        self.df = pd.DataFrame(self.coords, columns=['X', 'Y', 'Z'])
        self.df.insert(0, 'Atom', self.atoms)
        self.df = self.df.reset_index(drop=True)
        print(self.df.to_string(index=False))
        return self.df