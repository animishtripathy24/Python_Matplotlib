import matplotlib.pyplot as plt
import numpy as np
import random
x=np.arange(0,20)
y1=x**3
y2=x**10
random.shuffle(y1)
random.shuffle(y2)
plt.title("Scatter Plot")
#plt.grid(axis='both',ls='dashdot',lw=1,c='red')
plt.scatter(x,y1,marker="o",s=69)
plt.scatter(x,y2,marker='^',s=79)
plt.show()
