# -*- coding: utf-8 -*-
"""
Created on Wed May 27 19:33:16 2015

@author: TP
"""
import random

def readTOC(filename):
    raw = open(filename)
    raw = raw.read()
    lines=removeHeader(raw)
    lines=map(parseLine,lines)
    fullPreferences=[]
    for line in lines:  
        fullPreferences+=cardinalPreferences(line)
  #  print(fullPreferences)
    return fullPreferences
    
def removeHeader(raw):
    lines=raw.split("\n")
    headerSize=int(lines[0])+2
    n=len(lines)-1
    lines=lines[headerSize:n]    
    return lines

def parseLine(linestr):
    #linestr=linestr.replace(",{","")
    linestr=linestr.replace("{","")
    linestr=linestr.replace("}","")
    lines=linestr.split(",")
    return map(lambda x:int(x) ,lines)
    
def cardinalPreferences(ordinalPref):
    numVoters=ordinalPref.pop(0)
    size=len(ordinalPref)
    cardinalPrefs=[]
    for i in list(range(0,numVoters)):
        card=preference(ordinalPref,size)
        cardinalPrefs.append(card)
    return cardinalPrefs     

def preference(ordinalPref,size):
    cards = [0] * size
    rvector=randomVector(size) 
    for i,value in zip(ordinalPref,rvector):
        #print(i)
        #print(value)
        cards[i-1]=value
    return cards
        
def randomVector(n):
    v=[]
    for i in list(range(0,n)):
        v.append(random.random())
    z=sum(v)
    v=map(lambda x:x/z,v)
    v=list(reversed(sorted(v)))    
    return v
    


