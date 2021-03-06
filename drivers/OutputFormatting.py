# Dimer Generator by @ajay-mk
# github.com/ajay-mk/

# This file contains the class and functions for fromatting the output

import pandas as pd

class Output:
    
    def __init__(self, coords, atoms):
        self.coords = coords
        self.atoms = atoms
        self.make_dataframe()
        
    def make_dataframe(self):
        self.df = pd.DataFrame(self.coords, columns=['X', 'Y', 'Z'])
        self.df.insert(0, 'Atom', self.atoms)
        self.df = self.df.reset_index(drop=True)
        return self.df
    
    def display_coordinates(self):
        print(self.df.to_string(index=False))
        return self.df
    
    def save_coordinates(self, filename, monomer_name, dimer_atom_count):
        with open(filename, 'w') as f:
            f.write('{}\n{}\n'.format(dimer_atom_count, monomer_name))
            f.write(self.df.to_string(index=False, header=False))
            f.write('\n')