import matplotlib.pyplot as plt 
import matplotlib.animation as animation

class Pref(object):
    def __init__(self,x=3,y=3,name="A"):
        self.x=x
        self.y=y
        self.name=name

    def show(self,ax):
        ax.text(self.x,self.y, self.name, fontsize=14,
            bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})

fig = plt.figure()
ax = fig.add_subplot()
fig.subplots_adjust(top=0.85)

ax.axis([0, 10, 0, 10])
pref=Pref()
pref.show(ax)

plt.show()