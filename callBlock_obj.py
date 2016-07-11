# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 13:19:11 2016

@author: tzupan
"""

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
        assert type(startTime) == int and startTime in range(0,13)
        self.startTime = startTime
        self.dayTime = dayTime
        #self.InCall = []

    def getBankersName(self, incomingCall):
        '''

        '''
        ableBankers = [x for x in self.bankersInRoom if x.canReceiveCall(incomingCall)]
        return [x.getBankerName() for x in ableBankers]

    def getAvailableBankers(self, incomingCall):
        '''
        returns a list of bankers who are currently ABLE to take calls
        '''
        return [x for x in self.bankersInRoom if x.canReceiveCall(incomingCall)]

    def getBusyBankers(self, incomingCall):
        '''
        returns a list of bankers who are currently UNABLE to take calls
        ''' 

        return [x for x in self.bankersInRoom if x.canReceiveCall(incomingCall) == False]