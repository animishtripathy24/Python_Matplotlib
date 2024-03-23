import matplotlib.pyplot as plt
import numpy as np

#passing label as a list of strings in the legend function
x=np.arange(0,5,1)
y1=x**2
y2=x**3
plt.plot(x,y1,x,y2)
plt.legend(['plot-1','plot-2'])
plt.show()

#using loc argument in legend and label argument in plot function
x3=[2,3,4,5,6]
y3=[9,1,4,7,2]
plt.plot(x3,y3,label="plot-3")
plt.legend(loc="lower center")
plt.show()

#framealpha attribute is used to define the opacity of the legend box
x4=[5,6,1,4,9,10]
y4=[1,9,2,8,3,6]
plt.plot(x4,y4,label='plot-4')
plt.legend(loc='upper left',framealpha=0)#here 0 means no outline will be displayed
plt.show()

#facecolor attribute is used to provide the color the box
#edgecolor attribute is used to provide edge color to the edge of the box
x5=[5,6,8,3,4]
y5=[8,9,5,1,3]
plt.plot(x5,y5,label="plot-5")
plt.legend(loc="lower center",framealpha=1,facecolor="yellow",edgecolor="black")
plt.show()

#fancybox takes argument either true or false used to provide fancyness to the box(slight roundedness)
#shadow argument also takes either true or false and is used to provide shadow to the box
x6=[9,5,1,7,4]
y6=[7,2,9,1,4]
plt.plot(x6,y6,label="plot-6")
plt.legend(loc="upper right",framealpha=1,facecolor="yellow",edgecolor="black",fancybox=True,shadow=True)
plt.show()



