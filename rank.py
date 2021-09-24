import matplotlib.pyplot as plt 

class Election(object):
    def __init__(self,votes):
        self.votes=votes
        self.prefs=[]
        for vote_i in self.votes:
            self.prefs+=vote_i.prefs

    def set_all(self,value=False):
        for pref_i in self.prefs:
            pref_i.set_color(value)	

    def set_category(self,cat,value=False):
        for pref_i in self.prefs:
            if(pref_i.name==cat):
                pref_i.set_color(value)	    
    
    def set_column(self,i,value=True):
        for vote_i in self.votes:
            vote_i.prefs[i].set_color(value)

    def show_winer(self,cat_i):
        for pref_i in self.prefs:
            if(pref_i.color=='green'):
                pref_i.set_color(True)
            if(pref_i.is_active() and pref_i.name==cat_i):
                pref_i.set_color('green')

    def show(self,ax):
        for vote_i in self.votes:
            vote_i.show(ax)	

class Vote(object):
    def __init__(self,prefs,t=7):
        self.prefs=prefs
        self.t=t

    def show(self,ax):
        ax.add_patch(plt.Rectangle((0.5, self.t), 6, 2, 
        	ls="--", ec="c", fc="None",))
        for pref_i in self.prefs:
            pref_i.show(ax)

class Pref(object):
    def __init__(self,x=3,y=3,name="A"):
        self.x=x
        self.y=y
        self.name=name
        self.color='#0099FF'

    def show(self,ax):
        ax.text(self.x,self.y, self.name, fontsize=14,
            bbox={'facecolor':self.color, 'alpha': 0.5, 'pad': 10})

    def is_active(self):
        return (self.color=='#0099FF')

    def set_color(self,color):
        if(type(color)==str):
            self.color=color
            return
        if(color):
            self.color='#0099FF'
        else:
            self.color="red"

def make_vote(x,y,names,t):
    prefs=[ Pref(x+1.5*i,y,name_i) 
             for i,name_i in enumerate( names)] 
    return Vote(prefs,t)