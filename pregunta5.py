from matplotlib.pyplot import *
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
X = np.linspace(-1, 1, 100)
Y = np.linspace(-1, 1, 100)
X, Y=np.meshgrid(X, Y)
Z=0
for i in range(30):
    var = 2*i+1
    Z = Z + (np.sin(var*X)*np.sinh(var*Y))/(var*np.sinh(var))
fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(1,1,1, projection='3d')
ax.plot_wireframe(X, Y, Z, rstride=2, cstride=2)
title('Solución Ecuacón de Laplace-Cristhian Bernal')
ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")
ax.set_zlabel("Eje Z")
show()