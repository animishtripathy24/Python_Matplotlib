from matplotlib import pyplot as plt
import numpy as np
x=np.arange(0,10,2)
y=x**2
print(x,y)
plt.plot(x,y,marker="o",markeredgecolor="b",markerfacecolor="c",ms=10,color="k")
plt.title("Marker Basics")
plt.show()
