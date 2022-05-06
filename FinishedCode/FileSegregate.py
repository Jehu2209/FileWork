# Copyright 2022, Jehu Morning, Alrights Reserved
"""
Gathers simple file data from a specific folder
"""
import os

class FileSegregation:
    def __init__(self, Folder):
        self.Folder = Folder
        self.Files = sorted([i for i in os.listdir(Folder)])
    def file_Path_Creation(self):
        """
        :return: List of file paths that have been determined readable
        """
        # gathering the available extensions within the folder
        extList = [i.split('.')[1] for i in self.Files]
        # selects which files are openable
        openableList = [i for i,x in enumerate(extList) if x == 'txt']
        # selects the files from self.Files
        fileList = [self.Files[i] for i in openableList]
        # creates a list of fullpaths for the files which are readable and returns
        return [f'{self.Folder}/{i}' for i in fileList]
    def true_segregation(self) -> dict:
        """
        dict architecture {"ext": [[file names],[position within self.Files]]}

        :return: dictionary with file extensions and files of those extensions
        """
        ext_dictionary = {}
        extList = [i.split('.')[1] for i in self.Files]
        for i in extList:
            if i not in ext_dictionary:
                ext_dictionary[i] = [[j.split('.')[0] for j in self.Files if j.split('.')[1] == i], [l for l,x in enumerate(extList) if x == i]]
            else:
                pass
        return ext_dictionary
    def dictBurner(self, _list: list):
        """
        :param _list: List of items
        :return: Dictionary of the items of the list, with each dictionary entry containing the list without the entries item
        """
        dictBurns = {}
        n = 0
        for i in _list:
            dictBurns[i] = _list[0:n] + _list[n + 1:]
            n += 1
        return dictBurns