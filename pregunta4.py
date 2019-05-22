from pylab import *
xmax = 5.0
xmin = -5.0
NX = 15
NY = 15
ymax = 5.0
ymin = -5.0
x = linspace(xmin, xmax, NX)
y = linspace(ymin, ymax, NY)
X, Y = meshgrid(x,y)
Ax = (-2*Y)/(1+X**2+Y**2)        #f(X,Y)
Ay = (2*X)/(1+X**2+Y**2)      #g(X,Y)
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