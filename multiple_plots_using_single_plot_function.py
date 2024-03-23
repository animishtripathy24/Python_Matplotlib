import matplotlib.pyplot as plt
import numpy as np

x=np.arange(0,50,2)
y1=x**2
y2=x**3
y3=x**4
plt.plot(x,y1,x,y2,x,y3)
plt.title("Multiple plots using Single plot function")
plt.show()
