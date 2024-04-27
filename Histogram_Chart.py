from matplotlib import pyplot as plt
marks=[8,90,50,25,40,60,55,44,72,75,78,30,10,34,84]
#grade_intervals=[0,35,70,100]
plt.hist(marks,bins=[0,10,20,30,40,50,60,70,80,90,100])
plt.title("Student Grade")
plt.show()
