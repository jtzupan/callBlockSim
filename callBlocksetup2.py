#this code will define a banker and a call

import random
import csv
    

def callSim(roomST, roomDT, callFileIn, bankerFileIn):
    '''
    this function is used to test different call assignment strategies
    '''
    mel_count = 0
    bankerList, bankerList1 = createBankerList(bankerFileIn)
    room = callRoom(bankerList, roomST, roomDT)
    callList = createIncomingCalls(callFileIn)
    #for call in callList:
    for i in range(len(callList)):
        call = random.choice(callList)
        callList.remove(call)
        mel_count += takeCall(call, room)

#        for banker in room.getBusyBankers():
#            banker.reduceCallLeft()


    return 'these calls resulted in %d MELs' %mel_count


def createIncomingCalls(file_in):
    '''
    '''
    incomingCallList = []
    fi = open(file_in, 'rb')
    for row in csv.reader(fi, delimiter = ','):
        for i in range(int(row[2])):
            #str(j) = incomingCall(row[3], row[1])
            #incomingCallList.append(str(j))   
            incomingCallList.append(incomingCallList(row[3], row[1]))
    #return incomingCallList

def createBankerList(file_in):
    '''
    '''
    bankerList = []
    bankerNameList = []
    fi = open(file_in, 'rb')
    for row in csv.reader(fi, delimiter = ','):
        if row[0] in bankerNameList:
            #row[0].addLicense(row[3])
            [x.addLicense(row[3]) for x in bankerList if x.getBankerName() == row[0]]
        else:
            bankerNameList.append(row[0])            
            bankerList.append(banker(row[0], row[2]))
            [x.addLicense(row[3]) for x in bankerList if x.getBankerName() == row[0]]
            #row[0].addLicense(row[3])
    return bankerList, bankerNameList
            
            


#help code to initialize bankers and calls
#def main():
#    tyler = s.banker('tyler', 'refi')
#    tom = s.banker('tom', 'refi')
#    za = s.banker('za', 'purch')
#    hersh = s.banker('hersh', 'purch')
#
#    tyler.addLicense('mi')
#    tom.addLicense('mi')
#    za.addLicense('mi')
#    hersh.addLicense('mi')
#
#
#if __name__ == '__main__':
#    main()









