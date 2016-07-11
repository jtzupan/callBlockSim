# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 14:04:19 2016

@author: tzupan
"""
import random

def randomBanker(incomingCall, callRoom):
    '''
    this function assigns the incoming call to any banker who is available
    and allowed to take the call
    '''
    #MEL_count will have to be kept outside of this function so it is not reset every time the function is called
    MEL = 0
    #availableBankers = callRoom.getBankers(incomingCall)
    try:
        availableBankers = callRoom.getAvailableBankers(incomingCall)
        bankerToTakeCall = random.choice(availableBankers)
        bankerToTakeCall.bankerTakesCall(incomingCall)
        #print 'call taken'
    except:
        MEL = 1
        return MEL
        
    return MEL
    
#def takeCall(incomingCall, callRoom):
#    '''
#    this function assigns the incoming call to any banker who is available
#    and allowed to take the call
#    '''
#    #MEL_count will have to be kept outside of this function so it is not reset every time the function is called
#    MEL = 0
#    #availableBankers = callRoom.getBankers(incomingCall)
#    try:
#        #minLicense = min([x.numLicenses() for x in availableBankers]) 
#        availableBankers = callRoom.getBankers(incomingCall)
#        print len(availableBankers)
#        bankerToTakeCall = random.choice(availableBankers)
#        bankerToTakeCall.bankerTakesCall(incomingCall)
#        #print 'call taken'
#    except: #Exception as e:
#        #print str(e)
#        MEL = 1
#        #print 'No available bankers.  Current MEL count: %d' %MEL
#        return MEL
#    #bankersToChooseFrom = [x for x in availableBankers if x.numLicenses() == minLicense]
#    #bankerToTakeCall = random.choice(availableBankers)
#    #bankerToTakeCall.bankerTakesCall(incomingCall)
#    #bankerToTakeCall.timeUnavailableLeft(incomingCall)
#    #return bankerTakesCall.getBankerName(), MEL
#    return MEL