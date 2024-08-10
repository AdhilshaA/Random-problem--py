import matplotlib.pyplot as plt

x = [i for i in range(9)]
y = [i ** 2 for i in range(9)]
z = [i ** 3 for i in range(9)]
plt.plot(x,y,'rs',x,x,'g^')
plt.axis([0,10,0,70])
plt.xticks([i for i in range(11)])
plt.title("MY graph")
plt.savefig('graph1',bbox_inches='tight')
