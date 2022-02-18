# Dimer Generator by @ajay-mk
# github.com/ajay-mk/

# This file contains the class and functions for translation of monomer

import numpy as np

class Translate:
    """Class to handle translation of coordinates"""
    def __init__(self, coords, axis, distance):
        self.coords = coords
        self.axis = axis
        self.distance = distance
        self.translation_directions()
        self.translate_coordinates()
        
    def translate_coordinates(self):
        self.translation_direction = np.tile(self.translation_direction, (len(self.coords), 1))
        self.translated_coords = np.add(self.coords, (self.distance * self.translation_direction))
        self.translated_coords = np.round(self.translated_coords, 5)
        return self.translated_coords
    
    def translation_directions(self):
        if self.axis == 'x' or self.axis == 'X':
            self.translation_direction = [1, 0, 0]
        if self.axis == 'y' or self.axis == 'Y':
            self.translation_direction = [0, 1, 0]
        if self.axis == 'z' or self.axis == 'Z':
            self.translation_direction = [0, 0, 1]
        return self.translation_direction