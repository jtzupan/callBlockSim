#this code will define a banker and a call

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
        self.busy = False

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

        if incomingCall.getState() in self.getLicenses() and self.specialty == incomingCall.getSpecialty() and self.busy == False:
            return True
        else:
            return False

    def bankerTakesCall(self, incomingCall):
        ''' 
        if banker takes call switches the banker to busy for the specified amount of time 
        '''
        if self.canReceiveCall(incomingCall):
            self.busy = True

    def timeUnavailableLeft(self, incomingCall):
        '''
        sets the banker as unavailable for duration of call
        '''
        self.timeUnavailable = incomingCall.callDuration() 

    def reduceCallLeft(self):
        '''
        reduces banker unavailability by one minute
        '''
        self.timeUnavailable -= 1
        if self.timeUnavailable == 0:
            self.busy = False



class incomingCall(object):
    '''
    representation of an incoming call
    '''

    def __init__(self, fromState, specialty, receivedTime, duration):
        '''
        initializes a incoming call; saves all parameters as attributes 
        of the instance.
        fromState: which state the call is coming from
        specialty: the specialty of the banker needed for the call
        receivedTime: time the call was received (EST)
        duration: how long the call lasted (must be a float longer than duration = 0)
        '''
        assert type(duration) == float and duration > 0
        self.fromState = fromState
        self.specialty = specialty
        self.receivedTime = receivedTime
        self.duration = duration

    def getState(self):

        return self.fromState

    def getSpecialty(self):
        return self.specialty

    def receivedTime(self):
        return self.receivedTime

    def callDuration(self):
        return self.duration
    
    def callReduces(self):
        self.duration -= 1


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
        '''
        self.bankersInRoom = bankersInRoom
        assert type(startTime) == float and startTime in range(0,13)
        self.startTime = startTime
        self.dayTime = dayTime

    def getBankersName(self, incomingCall):
       '''

       '''
       ableBankers = [x for x in self.bankersInRoom if x.canReceiveCall(incomingCall) and x.busy == False]
       return [x.getBankerName() for x in ableBankers]

    def getBankers(self, incomingCall):
       '''

       '''
       return [x for x in self.bankersInRoom if x.canReceiveCall(incomingCall) and x.busy == False]




def takeCall(incomingCall, callRoom):
    '''
    this function assigns the incoming call to any banker who is available
    and allowed to take the call
    '''
    availableBankers = callRoom.getBankers(incomingCall)
    minLicense = min([x.numLicenses for x in availableBankers])
    return minLicense
    






















