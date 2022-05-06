# Copyright 2022, Jehu Morning, Alrights Reserved
"""
Analytics of a designated folder
"""
import os

class FileCull:
    def __init__(self, _path):
        self._path = _path
        self._flist = sorted([i for i in os.listdir(self._path)])
        self.cull_list = []
    def full_Path_Creation(self) -> list:
        """
        :return: fullpath for files in _path directory
        """
        return sorted([f'{self._path}/{i}' for i in self._flist])
    def open_Files_Find_Empty(self, _pathlist: list) -> list:
        """
        :param _pathlist: list of file fullpaths
        :return: list of empty files
        """
        return [i for i in _pathlist if len(open(i).read()) == 0]
    def files_to_be_removed(self, files_to_add: list):
        """
        :param files_to_add:
        :return:
        """
        for i in files_to_add:
            self.cull_list.append(i)
        return self.cull_list
    def file_cull(self):
        """
        :return:
        """
        for i in self.cull_list:
            os.remove(i)