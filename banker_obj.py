# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 13:12:57 2016

@author: tzupan
"""

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
        self.busy = False
        #callsTaken and callsFromState are used for post hoc analysis
        #and do not affect the simulation        
        self.callsTaken = 0
        self.callsFromState = []

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

        if incomingCall.getState() in self.getLicenses() and self.specialty == incomingCall.getSpecialty() and self.callCount < maxCalls and self.busy == False:
            return True
        else:
            return False

    def bankerTakesCall(self, incomingCall):
        ''' 
        if banker takes call switches the banker to busy for the specified amount of time 
        '''
        if self.canReceiveCall(incomingCall):
            self.callCount += 1
            self.timeUnavailable = incomingCall.callDuration() 
            self.busy = True
            self.callCount += 1
            self.callsFromState.append(incomingCall.fromState)
        else:
            print self.name + 'could not take call, already has taken {} call.'.format(maxCalls)


    def reduceTimeUnavailable(self):
        '''
        reduces banker unavailability by one minute
        '''
        if self.timeUnavailable > 0:        
            self.timeUnavailable -= 1
        if self.timeUnavailable == 0:
            self.busy = False
