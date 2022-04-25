from Bio.PDB import *
import nglview as nv
import ipywidgets

parser = MMCIFParser()
structure = parser.get_structure("Thioredoxin", "files/1ert.cif")
view = nv.show_biopython(structure)

# Function 1: 
# Is a residue used for immobilization in the active 
# site and also accessible?




# Function 2: Are the vertices between clusters of residues 
# for attachment on the vertice of domain movement 
# Alterntive: Rigidity of protein

'''
from numpy import vectorize


Import query_pdb

Generate molecular dynamics 

Calculate average displacement vector
'''



# Function 3: Access the Relative Surface accessibility of 
# each important residue



# Function 4: pH Stability of the query protein