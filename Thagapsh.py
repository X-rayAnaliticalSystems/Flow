#Thagapsh

import flow as fl
import matplotlib.pyplot as plt
u1=0.005 #size1
u2=0.04#size2
h=0.2#deep
v=0.85#flow's velocity
Bd=15#Front
V=1.4+18.7
G=50

p1=1.00
p2=1.00

i020=0.20
i1000=1000
i1=1
i5=5
i10=10
i20=20
i50=50
i100=100
i500=500

Xk1=fl.distance(u1,p1,h,v,Bd)
Sk1=fl.turbidity(u1,p1,h,v,Bd)
Xk2=fl.distance(u2,p2,h,v,Bd)
Sk2=fl.turbidity(u2,p2,h,v,Bd)
Xk3=fl.midle_distance(u1,u2,p1,p2,h,v,Bd)
Sk3=fl.midle_turbidity(u1,u2,p1,p2,h,v,Bd)

print (len(Xk1),len(Xk2),len(Xk3))
print(len(Sk1),len(Sk2),len(Sk3))
X020=fl.sort_turbidity(Sk1,i020)
print('x020=',X020)
X1000=fl.sort_turbidity(Sk1,i1000)
print('x1000=',X1000)
X1=fl.sort_turbidity(Sk1,i1)
print('x1=',X1)
X5=fl.sort_turbidity(Sk1,i5)
print('x5=',X5)
X10=fl.sort_turbidity(Sk1,i10)
print('x10=',X10)
X50=fl.sort_turbidity(Sk1,i50)
print('x50=',X50)
X100=fl.sort_turbidity(Sk1,i100)
print('x100=',X100)
X500=fl.sort_turbidity(Sk1,i500)

print('x500=',X500)
P020=fl.squere(X020,Bd)
print('Sq020=',P020)
P1000=fl.squere(X1000,Bd)
print('Sq1000=',P1000)
P1=fl.squere(X1,Bd)
print('Sq1=',P1)
P5=fl.squere(X5,Bd)
print('Sq5=',P5)
P10=fl.squere(X10,Bd)
print('Sq10=',P10)
P50=fl.squere(X50,Bd)
print('Sq50=',P50)
P100=fl.squere(X100,Bd)
print('Sq100=',P100)
P500=fl.squere(X500,Bd)
print('Sq500=',P500)

T=fl.time(P020,v,V,G)
print('Time=',T)
destiny=fl.density(P020,h)
print('Destiny=',destiny)
plt.plot(Xk1,Sk1,'red',Xk2,Sk2,'blue',Xk3,Sk3,'green',linewidth=2)
plt.grid(True)
plt.show()
