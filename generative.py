# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 20:40:06 2015

@author: TP
"""
import numpy as np
from parserTOC import readTOC
from sklearn.decomposition import FactorAnalysis as FA 
from scipy.stats import norm
import voting

def toOrdinal(x):
    z = sorted(np.copy(x))
    return map(lambda y: z.index(y),x)

class PreferenceGenerator(object):
    def __init__(self,components):
        self.components=components
        self.comp=len(components)
        self.candidates=len(components[0])
        self.norm=norm

    def generate(self):
        pref=[]
        for i in xrange(self.candidates):
            v=self.components[:,i]
            value=0.0
            for f in v:
                value+=f*self.norm.rvs()
            pref.append(value)
        return pref    

    def generateOrd(self):
        return toOrdinal(self.generate())

    def generateSeries(self,n):
        s=[]
        for i in xrange(n):
            s.append(self.generateOrd())
        return s
    
def learn(data):
    model=FA(n_components =2)
    model.fit(data)
    return PreferenceGenerator(model.components_)

def experiment(model,methods, n_votes=10000,n_series=100):
    size=len(methods)    
    confusion_matrix=np.zeros((size,size))
    for i in xrange(n_series):
        synthetic_data=model.generateSeries(n_series)
        result=[]
        for method in methods:
            result.append(method(synthetic_data))
        print(result)    
        for i in xrange(len(result)):
            for j in xrange(len(result)):
                a_i=result[i]
                a_j=result[j]
                if(a_i==a_j):
                    confusion_matrix[i][j]+=1.0
    confusion_matrix*= (1.0 / n_series)
    print(confusion_matrix)
 
def runExperiment(dataset="data.toc"):
    data=readTOC(dataset)
    model=learn(data)
    methods=[voting.antiplurality,voting.pluarity,voting.bordaMethod,
    voting.twoTurns,voting.InstantRunoff]
    experiment(model,methods)

runExperiment()