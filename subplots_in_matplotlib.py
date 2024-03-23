import matplotlib.pyplot as plt
import numpy as np

x=[0,1,2,3,4]
y1=[30,40,30,20,10]
y2=[10,30,20,60,40]

plt.subplot(1,2,1)
plt.plot(x,y1)
plt.title("Power Finance Corporation")

plt.subplot(1,2,2)
plt.plot(x,y2)
plt.title("SJVN")
#plt.figure(figsize= 15,7)
plt.suptitle("Stock Market Statistics")
plt.show()
