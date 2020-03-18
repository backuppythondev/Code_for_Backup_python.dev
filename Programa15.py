from pylab import *
from mpl_toolkits.mplot3d import Axes3D
 
# autor: backup_python.dev

fig = figure()
ax = Axes3D(fig)
style.use('dark_background')
X = np.arange(-8, 30, 0.50)
Y = np.arange(-8, 20, 0.50)
X, Y = np.meshgrid(X, Y)
Z = np.cos(X)

ax.plot_surface(X,Y,Z, rstride=1, cstride=1)
show()