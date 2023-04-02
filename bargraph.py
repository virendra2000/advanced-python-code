from matplotlib import pyplot as plt
x=[2,4,8,10]
y=[2,8,8,2]
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('Graph')
plt.bar(x,y,label="Graph",color='r',width=.5)
plt.show()
