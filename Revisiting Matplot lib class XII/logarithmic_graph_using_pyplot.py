import matplotlib.pyplot as plt
import numpy

x = numpy.linspace(1,50,200)
y = numpy.log(x)

plt.plot(x,y,'c',linewidth = 2)

y = numpy.sin(x)
plt.plot(x,y, 'r', linewidth = 1, linestyle = 'dotted')
y = numpy.cos(x)
plt.plot(x,y,'g', linewidth=3, linestyle='dashed')
y = numpy.tan(x)
plt.plot(x,y, 'y', linewidth=2, linestyle = 'dashdot')
plt.show()