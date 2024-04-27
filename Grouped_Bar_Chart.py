from matplotlib import pyplot as plt
import numpy as np

years=["2017","2018","2019","2020"]
cse=[74,82,89,79]
it=[58,72,76,61]
ece=[67,74,81,68]
eee=[53,45,57,41]
l=np.arange(len(years))
w=0.2
plt.figure(figsize=(10,5))
plt.bar(l,cse,width=w,label="CSE")
plt.bar(l+0.2,it,width=w,label="IT");
plt.bar(l+0.4,ece,width=w,label="ECE");
plt.bar(l+0.6,eee,width=w,label="EEE");
plt.title("PLACEMENT COMPARISON")
plt.xticks(l+0.3,years)
plt.legend(loc="upper right",shadow=True)
plt.ylim(0,100)
plt.show()
