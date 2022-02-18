# Dimer Generator by @ajay-mk
# github.com/ajay-mk/

# This file contains the class and functions for rotation of monomer

import numpy as np

class Rotate:
    """Class for rotating the coordinates"""
    def __init__(self, coords, axis, angle):
        self.coords = coords
        self.axis = axis
        self.angle = angle
        self.rotation_matrices()
        self.rotate_coordinates()
        
    def rotate_coordinates(self):
        self.rotated_coords = np.dot(self.coords, self.rotation_matrix)
        self.rotated_coords = np.round(self.rotated_coords, 5)
        return self.rotated_coords
    
    # Define rotation matrix about the axis
    def rotation_matrices(self):
        if self.axis == 'x' or self.axis == 'X':
            self.rotation_matrix = np.array([[1, 0, 0],
                                             [0, np.cos(self.angle), -np.sin(self.angle)],
                                             [0, np.sin(self.angle), np.cos(self.angle)]])
        if self.axis == 'y' or self.axis == 'Y':
            self.rotation_matrix = np.array([[np.cos(self.angle), 0, np.sin(self.angle)],
                                             [0, 1, 0],
                                             [-np.sin(self.angle), 0, np.cos(self.angle)]])
        if self.axis == 'z' or self.axis == 'Z':
            self.rotation_matrix = np.array([[np.cos(self.angle), -np.sin(self.angle), 0],
                                             [np.sin(self.angle), np.cos(self.angle), 0],
                                             [0, 0, 1]])
        return self.rotation_matrix