import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi)
plt.plot(x, np.sin(x),label='sin')
plt.plot(x, np.cos(x),label='cos')
plt.plot(x, np.tan(x),label='tan')
plt.ylim([-3,3])
plt.show() # if add this line, the plot on the .plt
# #will be shown and the save command below will save empty .plt draw board
# plt.savefig('123.png')