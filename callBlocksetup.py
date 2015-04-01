#this code will define a banker and a call

class banker(object):
    '''
    representation of a banker
    '''

    def __init__(self, specialty):
        '''
        initializes a banker; saves all parameters as attributes
        of the instance.
        specialty: the banker's specialty, input as a string
        licenses: a blank list of the states in which the banker holds licenses
        busy: a banker can only recieve a call when not busy, initially set to false
        '''
        
        self.licenses = []
        self.specialty = specialty
        self.busy = False

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

    def canReceiveCall(self, incomingCall):
        '''
        Checks if banker can accept call.
        Banker can recieve call if they match on specialty and state
        and are not busy.
        Returns True if they can accept call and False otherwise
        '''

        if incomingCall.getState() in self.getLicenses() and self.specialty == incomingCall.getSpecialty() and self.busy = False:
            return True
        else:
            return False

    def bankerTakesCall(self, incomingCall):
        ''' '''
        if canRecieveCall(incomingCall):
            self.busy = True



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

    def getBankers(incomingCall):
       '''

       '''
       ableBankers = [x for x in bankersInRoom() if x.canReceiveCall(incomingCall)]
       return ableBankers



























