from pylab import *
xmax = 50.0
xmin = -50.0
NX = 20
NY = 20
ymax = 50.0
ymin = -50.0
x = linspace(xmin, xmax, NX)
y = linspace(ymin, ymax, NY)
X, Y = meshgrid(x,y)
Ax = (X)*(Y**2)        #f(X,Y)
Ay = -(Y)*(X**2)         #g(X,Y)
figure()
QP = quiver(X,Y,Ax,Ay)
quiverkey(QP, 0.85, 1.05, 1.0, '1 mT', labelpos='N')
dx = (xmax -xmin)/(NX -1)
dy = (ymax -ymin)/(NY -1)
axis([xmin-dx, xmax+dx, ymin-dy, ymax+dy])
title('Campos Vectoriales-Cristhian Bernal')
xlabel('x')
ylabel('y')
show()