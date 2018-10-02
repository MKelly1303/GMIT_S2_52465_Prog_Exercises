import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.0, 10.0, 0.01)
y = 3.0 * x + 1.0

noise = np.random.normal(0.0, 10.0, len(x))


plt.plot(x , y+noise, 'r+')
plt.plot(x, y, 'b-')
# matplotlib remembers if you previously called the .plot command and adds in any subsequent .plot commands
plt.plot(x, y*3, 'y.')
plt.show()

# matplotlib will then reset once the original plot is closed and generate a new one...
plt.plot(x, y*3, 'm.')
plt.show()