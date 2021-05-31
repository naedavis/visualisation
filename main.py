import matplotlib.pyplot as plt
import numpy
# from scify import stats

x = [14.2,16.5,11.8,15.3,18.8,22.5,19.5]
y = [220,330,190.00,340,410,445,415]
my_mean = numpy.mean(x)
my_mean_y = numpy.mean(y)


plt.xlabel('Temperature (degrees celsius')
plt.ylabel('')
plt.title('Soup sales in relation to temperature')
plt.scatter(x, y)
plt.show()
