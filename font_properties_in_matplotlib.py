import matplotlib.pyplot as plt
sub=['OS','DBMS','OOPS','DCCN','IR']
q1=[6,10,3,9,9]
q2=[9,10,7,9,8]
plt.plot(sub,q1,sub,q2)
f1={'family':'Arial','size':20,'color':'r'}
f2={'family':'Cambria','size':12,'color':'b'}
f3={'family':'Calibri','size':10,'color':'k'}
plt.title("Result Obtained",fontdict=f1)
plt.xlabel("Subjects",fontdict=f2)
plt.ylabel("Marks obtained",fontdict=f3)
plt.show()
