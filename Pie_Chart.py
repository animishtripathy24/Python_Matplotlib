from matplotlib import pyplot as plt
student_performance=["Excellent","Good","Average","Poor"]
student_values=[15,25,12,8]
plt.pie(student_values,labels=student_performance,colors=['orange','cyan','blue','yellow','pink'],autopct="%2.3f%%")
plt.show()

#by default the graph starts from the 0 deg angle
#but if we want to change the starting angle
#we can use startangle as an argument to the pie function
plt.pie(student_values,labels=student_performance,startangle=180,explode=[0.2,0.0,0.0,0.0])
plt.show()
