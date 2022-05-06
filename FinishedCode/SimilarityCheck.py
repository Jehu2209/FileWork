# Copyright 2022, Jehu Morning, Alrights Reserved
"""
Using vectorization methods to judge the similarity of a file against another
"""
import math, string, os, json

class SimCheck:
    """
    Welcome to SimCheck
    """
    def __init__(self, fileList: list, checkQuery=None):
        # self.fileList is further transmuted while self.ListofFiles remains constant
        # if fileList has more than 1 item then the list can be sorted
        if len(fileList) > 2:
            self.fileList = fileList
            self.fileList.sort()
        else:
            self.fileList = fileList
        # Saving a copy of the fileList
        self.ListofFiles = tuple(self.fileList)
        # assigning checkQuery value and keeps a plan text copy of the file name
        if checkQuery is not None:
            if checkQuery not in self.fileList:
                self.checkQuery = checkQuery
                # Saving a copy of the checkQuery
                self.QueryofCheck = tuple(checkQuery)
            else:
                self.checkQuery = checkQuery
                self.fileList.remove(self.checkQuery)
                self.QueryofCheck = tuple(checkQuery)
        else:
            self.checkQuery = self.fileList[0]
            self.fileList = fileList[1:]
            # for quickSum
            self.QueryofCheck = self.ListofFiles[0]
    def dataRead(self) -> list:
        """
        Forge: data enters here,
        files are opened and read,
        then contents is transmuted into a single string with all punctuation removed
        =============================================================================
        File paths from __init__(): are opened, contents are read and lines
        :return:
        """
        try:
            self.fileList = [open(i, 'r') for i in self.fileList]
            data = [i.read() for i in self.fileList] +[open(self.checkQuery, 'r').read()]
            # darkSpace lives!
            dataRead = [''.join(i.translate(str.maketrans('', '', string.punctuation))).replace('\n', '').replace('\t', '') for i in data]
            self.fileList = dataRead[:-1]
            self.checkQuery = dataRead[-1]
            return self.fileList, self.checkQuery
        except IOError:
            raise BaseException('File not recognized')
    def countFreq(self, s: str) -> dict:
        """
        Beginning of vectorization,
        lists enter and turn into dictionaries with the count of each word
        ==================================================================
        :return: count of each word
        """
        countFreqD = {}
        for i in s.split(' '):
            if i in countFreqD:
                countFreqD[i] += 1
            else:
                countFreqD[i] = 1
        return countFreqD
    def scalProd(self, D1: dict, D2: dict) -> float:
        """
        Middle of vectorization,
        two dictionaries enter, the dictionary of the testCheck and queryCheck
        the sum like words is returned(as length of vectors)
        ======================================================================
        :param D1: checkQuery dictionary
        :param D2: checkTest dictionary
        :return: scalar product float value
        """
        Sum = 0.0
        for key in D1:
            if key in D2:
                Sum += (D1[key] * D2[key])
        return Sum

    def vectAng(self, v1, v2):
        """
        Final of vectorization,
        the length of the vectors is put through the vector angle formula,
        -----------------------------------------------------------------
        |multiplication of two vectors: θ = arccos((a · b)/(|a| × |b|))"|
        -----------------------------------------------------------------
        =================================================================
        :param v1: queryCheck
        :param v2: checkContent
        :return: θ as radian measurement of similarity, with identical x -> 0
        """
        return math.acos(SimCheck(fileList=[self.checkQuery] + self.fileList).scalProd(v1, v2) / math.sqrt(SimCheck(fileList=[self.checkQuery] + self.fileList).scalProd(v1, v1) * SimCheck(fileList=[self.checkQuery] + self.fileList).scalProd(v2, v2)))
    def docSim(self):
        """# Hot Mess!!"""
        # instance is created
        sim = SimCheck(fileList=[self.checkQuery] + self.fileList)
        # dataRead is called, contents are separated into checkContent and queryContent
        dataRead = sim.dataRead()
        # the testees and tester
        checkContent, queryContent = dataRead[0], dataRead[1]
        # both checkContent and queryContent are pushed through countFreq()
        checkContent, queryContent = [sim.countFreq(i) for i in checkContent], sim.countFreq(queryContent)
        # simScores is the list of similarity scores
        # cycling through checkContent and applies vectAng to the items in checkContent and queryContent
        simScores = [sim.vectAng(v1=queryContent, v2=i) for i in checkContent]
        # returns hotdog list
        return simScores
    def exportJSON(self):
        self.RadVals = SimCheck(fileList=[self.checkQuery] + self.fileList).docSim()
        self.preJSON = {
            "checkQuery": self.QueryofCheck,
            "fileList": self.ListofFiles,
            "Radian Values": {}
        }
        n = 0
        for i in self.ListofFiles:
            if i is not self.QueryofCheck:
                self.preJSON["Radian Values"][i] = self.RadVals[n]
                n += 1
        return self.preJSON
    def quickSum(self) -> str:
        """
        Gathers all pertinent information and prints a statement of information
        =======================================================================
        :return: str
        """
        print('Welcome too SimCheck!\n')
        print(f'\tChoosen files for comparision: {self.ListofFiles}')
        print(f'\tDesignated checkQuery: {self.QueryofCheck}')
        n = 0
        for i in self.ListofFiles:
            if i is not self.QueryofCheck:
                print(f'\tcheckQuery similarity to {i}: {SimCheck(fileList=[self.checkQuery] + self.fileList).docSim()[n]}')
                n += 1
            else:
                pass


# /Users/sadamhussein/PycharmProjects/FileWork_mac/ExOp/File2.txt
# /Users/sadamhussein/PycharmProjects/FileWork_mac/ExOp/File1.txt
# [f'/Users/sadamhussein/PycharmProjects/FileWork_mac/ExOp/{i}' for i in os.listdir('/Users/sadamhussein/PycharmProjects/FileWork_mac/ExOp')]

per = SimCheck(fileList=[f'/Users/sadamhussein/PycharmProjects/FileWork_mac/ExOp/{i}' for i in os.listdir('/Users/sadamhussein/PycharmProjects/FileWork_mac/ExOp')], checkQuery='/Users/sadamhussein/PycharmProjects/FileWork_mac/ExOp/File1.txt').docSim()
for i in per:
    print(i)
with open('simcheck.json', 'w') as outfile:
    outfile.write(json.dumps(SimCheck(fileList=[f'/Users/sadamhussein/PycharmProjects/FileWork_mac/ExOp/{i}' for i in os.listdir('/Users/sadamhussein/PycharmProjects/FileWork_mac/ExOp')]).exportJSON(), indent=4))
