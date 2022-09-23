import readline
import sys
import re
from typing import List

# these values are hardcoded so this script will only work for this case
ETOT = 'Etot'
EKTOT = 'EKtot'
EPTOT = "EPtot"
FILEPATH = 'heat.out'

class Contents:
    def __init__(self, filePath, target):
        self.filePath = filePath
        self.target = target
        self.lines = self.cleanLines()
        self.contents = self.parseLines()
        self.writeToFile()
        
    def getLines(self, file_name: str) -> List[str]:
        try:
            file = open(file_name)
            lines = file.readlines()
            file.close()
            return lines
        
        except:
            print("ERROR: file not found")
            return []
            
    def cleanLines(self) -> List[str]:
        lines = self.getLines(self.filePath)
        res = []
        for line in lines:
            if self.target in line:
                res.append(line)
        
        return res
        
    def parseLines(self) -> List[str]:
        res = []
        for line in self.lines:
            temp = re.findall(self.target+"\s*[:=]{1}\s*[-]{0,1}\d{1,}.\d{1,}", line)[0]
            res += re.findall("[-]{0,1}\d{1,}.\d{1,}", temp)
        return res
        
    def writeToFile(self) -> None:
        file = open(self.target+'.txt', 'w')
        for c in self.contents:
            file.write(c+'\n')
        file.close()

# TODO: implement modularity for search file and search parameters
def main():
    Contents(FILEPATH, ETOT)
    Contents(FILEPATH, EKTOT)
    Contents(FILEPATH, EPTOT)

if __name__ == "__main__":
    main()