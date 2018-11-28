import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

x=[1,2,3,4,5]
y=[1,2,3,1,2]

fig=plt.figure()
#ax1=plt.subplot2grid((1,1),(0,0))


ax1=fig.add_subplot(111)
ax1.plot(x,y,label='Line Graph',linewidth=1,color='r')

#ax2=fig.add_subplot(212)
#ax2.plot(x,y,label='Line Graph',linewidth=1,color='r')



ax1.grid(True,color='g',linewidth=0.2,linestyle='-')
ax1.set_yticks([1,2,3,4,5])
thres=2

ax1.fill_between(x,y,2,alpha=0.1,Q='g')



plt.xlabel('x axis',color='r')
plt.ylabel('y axis',rotation='90',color='g')
plt.title('Tutorials')
plt.legend()
plt.show()