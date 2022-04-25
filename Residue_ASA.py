# Import Modules
from pickle import TRUE
from Bio.PDB import MMCIFParser
from Bio.PDB.SASA import ShrakeRupley
import csv
import pandas as pd
import matplotlib.pyplot as plt

# mmCIf Parser
parser = MMCIFParser(QUIET=True)


# Loading the pdb file
struct = parser.get_structure("1ert", "files/1ert.cif")

# Start SASA Algorithm and create list 
sr = ShrakeRupley(n_points=500)
sr.compute(struct[0], level="R")
res_sasa_li = []
for chain in struct[0]:
    for res in chain:
        res_sasa_li.append((res.get_resname(), round(res.sasa,2)))

    #print("Created the list!")

# Write to list to csv file
with open('res_sasa.csv','w') as f:
    csv_out=csv.writer(f)
    csv_out.writerow(['RES_NUM','RES','SASA'])
    for numbering, row in enumerate(res_sasa_li):
        if row[0] != "HOH":
            csv_out.writerow([numbering+1, row[0], float(row[1])])    
f.close()

    #print("Created the file!")


# Generate Graph or SASA of all residues

df = pd.read_csv('res_sasa.csv')
df.set_index("RES", inplace=True)
res_type = str(input("Please enter the desired residue in three letter code: "))
print(df.loc[res_type])

#df.plot(x="RES_NUM", y="SASA")
#plt.show()

charged_res_coords = [] # store x,y,z of extracted charged resiudes 
charged_res = ["ARG", "HIS", "LYS", "ASP", "GLU"]

 # iterate over lines in pdb
for line in struct:
    # check if line starts with "ATOM"
    if line.startswith('ATOM'):
        # define fields of interest
        atom_id = line[6:11].strip()
        atom_name = line[12:16].strip()
        res_name = line[17:20].strip()
        chain_name = line[21:22].strip()
        residue_id = line[22:26].strip()
        x = line[30:38].strip()
        y = line[38:46].strip()
        z = line[46:54].strip()
        if res_name in charged_res:
            # pull out third spatial (y-coordinate)
            # print(z)
            # append groups to list
            charged_res_coords.append([atom_id, atom_name, res_name, chain_name, residue_id, x, y, z])

# print the stuff we added
print([item for item in charged_res_coords])



"""
Simple PDB parser
Coded by Steve Moss (gawbul [at] gmail [dot] com)
http://about.me/gawbul

Slicing features by Pierre Poulain 
http://cupnet.net/
"""