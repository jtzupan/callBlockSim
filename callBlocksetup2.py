#this code will define a banker and a call

import random
import csv
#import pylab

#declare this global variable to be the max number of calls a banker can take during one call block hour
global maxCalls
maxCalls = 1

class banker(object):
    '''
    representation of a banker
    '''

    def __init__(self, bankerName, specialty):
        '''
        initializes a banker; saves all parameters as attributes
        of the instance.
        bankerName: the name of the banker (first and last)
        specialty: the banker's specialty, input as a string
        licenses: a blank list of the states in which the banker holds licenses
        busy: a banker can only recieve a call when not busy, initially set to false
        '''
        
        self.bankerName = bankerName
        self.licenses = []
        self.specialty = specialty
        self.callCount = 0
        #self.busy = False

    def getBankerName(self):
        return self.bankerName

    def getSpecialty(self):
        '''returns the specialty of the banker''' 
        return self.specialty

    def getLicenses(self):
        '''returns a list of the states in which a banker holds licenses'''
        return self.licenses

    def addLicense(self, state):
        '''adds the state to the list of bankers states licenses''' 
        if state not in self.licenses:
            self.licenses.append(state)

    def numLicenses(self):
        '''returns the numbers of licenses a banker has'''
        return len(self.licenses)

    def canReceiveCall(self, incomingCall):
        '''
        Checks if banker can accept call.
        Banker can recieve call if they match on specialty and state
        and are not busy.
        Returns True if they can accept call and False otherwise
        '''

        #TODO adjust self.callCount for max number of calls a banker should be taking in a call block hour
        #set global variable at begninning of script
        if incomingCall.getState() in self.getLicenses() and self.specialty == incomingCall.getSpecialty() and self.callCount < maxCalls:
            return True
        else:
            return False

    def bankerTakesCall(self, incomingCall):
        ''' 
        if banker takes call switches the banker to busy for the specified amount of time 
        '''
        if self.canReceiveCall(incomingCall):
            self.callCount += 1
        else:
            print self.name + 'could not take call, already has taken %s call.' %maxCalls

    def timeUnavailableLeft(self, incomingCall):
        '''
        sets the banker as unavailable for duration of call
        '''
        #self.timeUnavailable = incomingCall.callDuration() 
        pass

    def reduceCallLeft(self):
        '''
        reduces banker unavailability by one minute
        '''
        #self.timeUnavailable -= 1
        #if self.timeUnavailable == 0:
        #    self.busy = False
        pass



class incomingCall(object):
    '''
    representation of an incoming call
    '''

    def __init__(self, fromState, specialty):
        '''
        initializes a incoming call; saves all parameters as attributes 
        of the instance.
        fromState: which state the call is coming from
        specialty: the specialty of the banker needed for the call
        receivedTime: time the call was received (EST)
        duration: how long the call lasted (must be a float longer than duration = 0)
        '''
        #assert type(duration) == float and duration > 0
        self.fromState = fromState
        self.specialty = specialty
        #self.receivedTime = receivedTime
        #self.duration = duration

    def getState(self):

        return self.fromState

    def getSpecialty(self):
        return self.specialty

    def receivedTime(self):
        #return self.receivedTime
        pass

    def callDuration(self):
        #return self.duration
        pass
    
    def callReduces(self):
        #self.duration -= 1
        pass


class callRoom(object):
    '''
    representation of the call block (called a room)
    '''

    def __init__(self, bankersInRoom, startTime, dayTime):
        '''
        initializes a call block; saves all parameters as attributes of the instance
        bankersInRoom: a list of bankers in the room for current hour
        startTime: the starting hour of the call block (must be an float between 0 and 13)
        dayTime: am or pm 
        inCall: an empty list of the bankers that are currently in a call
        '''
        self.bankersInRoom = bankersInRoom
        assert type(startTime) == float and startTime in range(0,13)
        self.startTime = startTime
        self.dayTime = dayTime
        #self.InCall = []

    def getBankersName(self, incomingCall):
        '''

        '''
        ableBankers = [x for x in self.bankersInRoom if x.canReceiveCall(incomingCall)]
        return [x.getBankerName() for x in ableBankers]

    def getBankers(self, incomingCall):
        '''
        returns a list of bankers who are currently able to take calls
        '''
        return [x for x in self.bankersInRoom if x.canReceiveCall(incomingCall)]

    def getBusyBankers(self):
        '''
        returns a list of bankers who are currently UNABLE to take calls
        ''' 

        return [x for x in self.bankersInRoom if x.callCount > maxCalls]



def takeCall(incomingCall, callRoom):
    '''
    this function assigns the incoming call to any banker who is available
    and allowed to take the call
    '''
    #MEL_count will have to be kept outside of this function so it is not reset every time the function is called
    MEL = 0
    #availableBankers = callRoom.getBankers(incomingCall)
    try:
        #minLicense = min([x.numLicenses() for x in availableBankers]) 
        availableBankers = callRoom.getBankers(incomingCall)
        print len(availableBankers)
        bankerToTakeCall = random.choice(availableBankers)
        bankerToTakeCall.bankerTakesCall(incomingCall)
        #print 'call taken'
    except: #Exception as e:
        #print str(e)
        MEL = 1
        #print 'No available bankers.  Current MEL count: %d' %MEL
        return MEL
    #bankersToChooseFrom = [x for x in availableBankers if x.numLicenses() == minLicense]
    #bankerToTakeCall = random.choice(availableBankers)
    #bankerToTakeCall.bankerTakesCall(incomingCall)
    #bankerToTakeCall.timeUnavailableLeft(incomingCall)
    #return bankerTakesCall.getBankerName(), MEL
    return MEL
    

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
def main():
    tyler = s.banker('tyler', 'refi')
    tom = s.banker('tom', 'refi')
    za = s.banker('za', 'purch')
    hersh = s.banker('hersh', 'purch')

    tyler.addLicense('mi')
    tom.addLicense('mi')
    za.addLicense('mi')
    hersh.addLicense('mi')


if __name__ == '__main__':
    main()









