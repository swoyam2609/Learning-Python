import matplotlib.pyplot as plt
import numpy

x = numpy.linspace(1,100,20)
print(x)
for i in x:
    print(i)
y = numpy.log(x)
plt.plot(x,y, linecolor='b', linestyle='dashdot', linewidth = 3, marker='o', markerfacecolor='red', markersize=8)
plt.xlabel("Range")
plt.ylabel("Log Values")
plt.title("Logarithmic Values")
plt.draw()
plt.show()