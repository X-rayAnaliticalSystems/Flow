import math as m
K=0.00000001
I=0.0002
g=9.82
x_max=600
def distance(u,p,h,v,Bd): # finess,quant, deep, velocity, front
    C=18.5*pow(I,-0.1) # coefficient
    N=((0.7*C+6)*C)/g # coeffitient
    S_in1=p*1000*(0.3*N*v*v)/h # initial turbidity 
    E=0.0002*m.exp(59*u)#coefficient of hydraulic fineness of particles
    #print(C,N,S_in1,E)
    x=0
    Xk=[]#distance
    while x<x_max:
        #print(0.01*S_in1*m.exp(-Bd*(u+K*E)*x/v))
        if (0.01*S_in1*m.exp(-Bd*(u+K*E)*x/v)<0.01):break
        Xk.append(x)
        x=x+0.1
    return Xk
def turbidity(u,p,h,v,Bd): # finess,quant, deep, velocity, front
    C=18.5*pow(I,-0.1) # coefficient
    N=((0.7*C+6)*C)/g # coeffitient
    S_in1=p*1000*(0.3*N*v*v)/h # initial turbidity 
    E=20*m.exp(u)#coefficient of hydraulic fineness of particles
    x=0
    Sk=[]#turbidity
    while x<x_max:# first
        if (0.01*S_in1*m.exp(-Bd*(u+K*E)*x/v)<0.01):break
        Sk.append(0.01*S_in1*m.exp(-Bd*(u+K*E)*x/v))
        x=x+0.1
    return Sk
def midle_distance(u1,u2,p1,p2,h,v,Bd):
    C=18.5*pow(I,-0.1) # coefficient
    N=((0.7*C+6)*C)/g # coeffitient
    S_in11=p1*1000*(0.3*N*v*v)/h # initial turbidity
    S_in12=p2*1000*(0.3*N*v*v)/h # initial turbidity 
    E1=20*m.exp(u1)#coefficient of hydraulic fineness of particles
    E2=20*m.exp(u2)#coefficient of hydraulic fineness of particles
    x=0
    Xk=[]#turbidity
    while x<x_max:
        A=0.01*S_in11*m.exp(-Bd*(u1+K*E1)*x/v)
        B=0.01*S_in12*m.exp(-Bd*(u2+K*E2)*x/v)
        #print(A,B)
        if ((A+B/2)<0.01):break
        Xk.append(x)
        x=x+0.1
    return Xk
def midle_turbidity(u1,u2,p1,p2,h,v,Bd):
    C=18.5*pow(I,-0.1) # coefficient
    N=((0.7*C+6)*C)/g # coeffitient
    S_in11=p1*1000*(0.3*N*v*v)/h # initial turbidity
    S_in12=p2*1000*(0.3*N*v*v)/h # initial turbidity 
    E1=20*m.exp(u1)#coefficient of hydraulic fineness of particles
    E2=20*m.exp(u2)#coefficient of hydraulic fineness of particles
    x=0
    Sk3=[]#turbidity
    while x<x_max:
        A=0.01*S_in11*m.exp(-Bd*(u1+K*E1)*x/v)
        B=0.01*S_in12*m.exp(-Bd*(u2+K*E2)*x/v)
        #print (A,B)
        if ((A+B/2)<0.01):break
        Sk3.append((A+B)/2)
        x=x+0.1
    return Sk3

def sort_turbidity(Sk,i):
    x=0
    for s in Sk:
        if s<i:return x
        x=x+0.1
        
def squere (distance,front):#distance, front
    import math
    K2=0.33#coeffitient
    K3=0.61#coeffitient
    return K2*(front*distance+K3*distance*distance*math.tan(math.radians(13)))

def density (squere,deep):  #
    return squere*deep

def time(distance,velocity,V,G):
    return distance*velocity+(V/G)*3600
