from matplotlib.pyplot import *
from numpy import *
x=arange(0,10,0.001)
f=x**2-2*x
g=5*x-6
plot(x,g,x,f)
fill_between(x,f,g,where=(1<=x)&(x<=6))
from sympy import * 
x=symbols('x')
f=x**2-2*x
g=5*x-6
h=g-f
res=integrate(h,(x,1,6))
print(f"La respuesta es: {res}")
show()
