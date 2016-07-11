# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 14:08:41 2016

@author: tzupan
"""
import random

import banker_obj as banker
import incomingCall_obj as call
import callBlock_obj as callBlock
import callAssignmentStrategies as callStrats

reload(banker)
reload(call)
reload(callBlock)
reload(callStrats)

#pseudocode
#iterate through every minute of an hour
#    check if any bankers become available during this minute
#        if yes:
#            set their busy status to False
#    find all calls that came in during this minute
#    iterate through these calls
#        FROM HERE TO END, callAssignmentStrategy.py WILL BE IN CHARGE OF LOGIC
#        attempt to assign call to banker using chosen assignment strategy
#        if assigned:
#            continue
#        if not assigned:
#            MELS +=1
#return MELS and other metadata that will be used in analysis

def runSimulation(listOfBankers, listOfCalls, callBlockStartTime, callBlockDayTime, callAssignmentStrategy):
    #later versions will read in csv files of bankers and calls
    #and use helper functions to read this files and produce
    #the respective lists
    
    callBlockInstance = callBlock.callRoom(listOfBankers, callBlockStartTime, callBlockDayTime)    
    
    mel_count = 0
    
    for i in range(60):
        [x.reduceTimeUnavailable() for x in callBlockInstance.bankersInRoom if x.busy == True]
        callsThisMinute = [c for c in listOfCalls if c.callStartTime == i]
        random.shuffle(callsThisMinute)
        while len(callsThisMinute) != 0:
#            mel_count += callStrats.randomBanker(callsThisMinute.pop(), callBlockInstance)
            mel_count += callAssignmentStrategy(callsThisMinute.pop(), callBlockInstance)
        print 'current Mel Count {}'.format(mel_count)
        print '{} busy bankers'.format(len([x for x in callBlockInstance.bankersInRoom if x.busy == True]))
            