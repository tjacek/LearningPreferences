import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from matplotlib.collections import PatchCollection
#from matplotlib.patches import Rectangle

class Vote(object):
    def __init__(self,prefs,t=7):
        self.prefs=prefs
        self.t=t

    def show(self,ax):
        ax.add_patch(plt.Rectangle((0.5, self.t), 6, 2, 
        	ls="--", ec="c", fc="None",))
        for pref_i in self.prefs:
            pref_i.show(ax)

    def get_bounds(self):
        point=[[pref_i.x,pref_i.y] for pref_i in self.prefs]       
        point=np.array(point)
        return np.amax(point,axis=0)-np.amin(point,axis=0)

class Pref(object):
    def __init__(self,x=3,y=3,name="A"):
        self.x=x
        self.y=y
        self.name=name

    def show(self,ax):
        ax.text(self.x,self.y, self.name, fontsize=14,
            bbox={'facecolor':'#0099FF', 'alpha': 0.5, 'pad': 10})

def make_vote(x,y,names,t):
    prefs=[ Pref(x+1.5*i,y,name_i) 
             for i,name_i in enumerate( names)]	
    return Vote(prefs,t)

fig = plt.figure()
ax = fig.add_subplot()
fig.subplots_adjust(top=0.85)

ax.axis([0, 10, -1, 10])
plt.axis('off')

vote=make_vote(1,8,["A","B","C","D"],7)
vote.show(ax)
vote=make_vote(1,5.5,["A","B","C","D"],4.5)
vote.show(ax)
vote=make_vote(1,3,["A","B","C","D"],2)
vote.show(ax)
vote=make_vote(1,0.5,["A","B","C","D"],-0.5)
vote.show(ax)

plt.show()