


import csv
import sys
import callBlocksetup as cb

if len(sys.argv) == 3:
    file_in = sys.argv[1]
    bankerStates = sys.argv[2]

fi = open(file_in, 'rb')
bs = open(bankerStates, 'rb')
#fo = open(file_out, 'rb')
#fw = csv.writer(fo)

def createBanker():
    bankerList = []
    for line in csv.reader(fi, delimiter = ','):
        if line[0] != 'CommonID':
            bankerID, specialty = line[0], line[1]
            bankerList.append(cb.banker(bankerID, specialty))
    #list will not print
    #print bankerList
    return bankerList 



def addBankerLicenses(bankerList):
    for i in csv.reader(bs, delimiter = ','):
        for j in bankerList:
            if i[0] == j.getBankerName():
                j.addLicense(i[1]) 
    
    for i in bankerList:
        print i.getBankerName(), i.getLicenses()













if __name__ == '__main__':
    addBankerLicenses(createBanker())
