# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 13:17:42 2016

@author: tzupan
"""

class incomingCall(object):
    '''
    representation of an incoming call
    '''

    def __init__(self, fromState, specialty, duration, callStartTime):
        '''
        initializes a incoming call; saves all parameters as attributes 
        of the instance.
        fromState: which state the call is coming from
        specialty: the specialty of the banker needed for the call
        receivedTime: time the call was received (EST)
        duration: how long the call lasted (must be a int longer than duration = 0)
        '''
        assert type(duration) == int and duration > 0
        self.fromState = fromState
        self.specialty = specialty
        self.callStartTime = callStartTime
        self.duration = duration

    def getState(self):

        return self.fromState

    def getSpecialty(self):
        return self.specialty

    def callStartTime(self):
        return self.callStartTime

    def callDuration(self):
        return self.duration
    