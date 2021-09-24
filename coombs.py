import matplotlib.pyplot as plt 
import matplotlib.animation as animation
#from matplotlib.collections import PatchCollection
from rank import Election,make_vote

fig = plt.figure()

def reset_fig():
    fig.clear()
    ax = fig.add_subplot()
    fig.subplots_adjust(top=0.85)
    ax.axis([0, 10, -1, 10])
    plt.axis('off')
    return ax

votes=[make_vote(1,8,  ["D","C","B","A"],7),
       make_vote(1,5.5,["A","D","C","B"],4.5),
       make_vote(1,3,  ["A","B","D","C"],2),
       make_vote(1,0.5,["A","B","C","D"],-0.5)]

election=Election(votes)
def animate(cat_i):
    ax=reset_fig()	
    if(cat_i=="win"):
        ax.text(7, 6, r'Winner: D', fontsize=24)
    else:	
        election.set_category(cat_i)
    election.show(ax)

anim=animation.FuncAnimation(fig,animate,frames=["A","B","C","win"],
	                        interval=2000)
anim.save("test.gif",writer="imagemagick")

plt.show()