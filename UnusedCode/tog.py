# Copyright 2022, Jehu Morning, Alrights Reserved
"""
Putting it all together
"""
from FinishedCode.SimilarityCheck import SimCheck
import os

# SimCheck Resources

folderPath = '/Users/sadamhussein/PycharmProjects/FileWork_mac/TestLocation'
files = sorted([f'{folderPath}/{i}' for i in os.listdir(folderPath)])
print(files)
sim = SimCheck(fileList=files)

sim.quickSum()



folderPath = '/Users/sadamhussein/PycharmProjects/FileWork_mac/TestLocation'
files = [i for i in os.listdir(folderPath)]
filesOpen = [open(f'{folderPath}/{i}', 'r') for i in files]

