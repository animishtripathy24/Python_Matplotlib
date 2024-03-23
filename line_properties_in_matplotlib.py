import matplotlib.pyplot as plt
import numpy as np

x=np.arange(0,10,2)
y=x**2
print(x,y)
plt.plot(x,y,linestyle="dashdot",linewidth=1,marker='o',mec='c',mfc='y',c='k')
plt.show()
