# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 18:10:18 2015

@author: TP
"""
import numpy as np
from sets import Set

def InstantRunoff(votes):
    numberOfCandidates=len(votes[0])
    candidates=zeros(numberOfCandidates)
    tabu= {}#Set([])    
    while(True):    
        for vote in votes:
            winner=-1
            for pref in vote:
                if(not ( pref in tabu.keys())):
                    print("Test")
                    winner=pref
                    break
            candidates[winner]+=1.0
        maxVotes=getMax(candidates)
        majority=float(len(votes)) / 2.0
        if(candidates[maxVotes]> majority):
            return maxVotes
        else:
            worst=candidates.index(min(candidates)) 
            tabu[worst]=True 

def twoTurns(votes):
    numberOfCandidates=len(votes[0])
    candidates=zeros(numberOfCandidates)
    for vote in votes:
        candidates[vote[0]]+=1.0
    c1=getMax(candidates)
    candidates[c1]=-1.0
    c2=getMax(candidates)
    candidates=zeros(2)
    for vote in votes:
        v1=vote.index(c1)
        v2=vote.index(c2)
        if(v1>v2):
            candidates[0]+=1
        else:
            candidates[1]+=1
    if(candidates[0] > candidates[1]):
        return c2
    else:
        return c1

def pluarity(votes):
    result=countVotes(votes,trivialCount)
    return result.index(max(result))

def antiplurality(votes):
    result=countVotes(votes,antipluarCount)
    return result.index(max(result))

def bordaMethod(votes):
    result=countVotes(votes,bordaCount)
    return  result.index(max(result))

def countVotes(votes,countingMethod):
    numberOfCandidates=len(votes[0])
    candidates=zeros(numberOfCandidates)
    for vote in votes:
        countingMethod(vote,candidates)
    return candidates

def getMax(result):
    return result.index(max(result))

def zeros(n):
    z=[]
    for i in xrange(n):
        z.append(0.0)
    return z
    
def bordaCount(vote,candidates):
    n=len(vote)    
    for pref in vote:
        candidates[pref]+=n
        n-=1
    return candidates
    
def trivialCount(vote,candidates):
    candidates[vote[0]]+=1.0
    return candidates

def antipluarCount(vote,candidates):
    last=vote[-1]
    for i in xrange(len(vote)):
        if i!=last:
            candidates[i]+=1.0
    return candidates