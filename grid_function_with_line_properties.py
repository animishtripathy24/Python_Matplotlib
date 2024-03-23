import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0,10,2)
y=[30,10,60,20,40]
#plt.grid(axis='x')
#plt.grid(axis='y')

# we can also mention linestyle, linewidth and color to style the grid lines accordingly
plt.grid(axis='both',ls='dashdot',lw=2,c='m')
plt.plot(x,y,marker='o',mec='k',mfc='yellow',ls='solid',lw=2,c='r')
plt.show()
