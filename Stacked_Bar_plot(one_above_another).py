from matplotlib import pyplot as plt
years=['2017','2018','2019','2020','2021']
cse=[67,34,89,29,96]
it=[56,78,23,45,69]
ece=[98,54,62,76,34]

ece_start=[cse[i]+it[i] for i in range(len(cse))]

plt.suptitle("Placement Statistics using Stacked Bar Plot")
#for vertical stacked bar plot we use bottom argument
plt.subplot(1,2,1)
plt.title("Placement comparison")
plt.bar(years,cse,width=0.4,color="black")
plt.bar(years,it,bottom=cse,width=0.4,color="green")
plt.bar(years,ece,bottom=ece_start,width=0.4,color="red")
plt.ylim(0,230)

#for horizontal stacked barplot we use left as an argument
plt.subplot(1,2,2)
plt.title("Placement comparison")
plt.barh(years,cse,height=0.4,color="black")
plt.barh(years,it,left=cse,height=0.4,color="green")
plt.barh(years,ece,left=ece_start,height=0.4,color="red")
plt.xlim(0,230)
plt.show()
