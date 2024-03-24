import matplotlib.pyplot as plt
x=['A','B','C','D']
y=[90,10,20,50]
plt.title("Bar Plot")
plt.subplot()
plt.bar(x,y,color="red",width=0.2)
plt.show()

#for horizontal barplot we use barh() function and height as parameter
plt.barh(x,y,color='cyan',height =0.5)
plt.show()

