import numpy as np
import csv

with open('train.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

data=np.delete(data,(0), axis=0)
data=np.array(data,dtype=float)

points=np.ndarray((7176,6),dtype=float)
for i in range(7176):
    points[i][0]=1
    for j in range(5):
        points[i][j+1]=data[i][j]

def step_gradient(points,learning_rate,m):
    n=4        #Number of regressors 
    m_slope=np.zeros(n+1,dtype=float)
    new_m=np.zeros(n+1,dtype=float)
    M=len(points)
    for i in range(M):
        y=points[i,n+1]
        small_sum=0
        for j in range(n+1):
            small_sum+=m[j]*points[i,j]
        for j in range(n+1):
            m_slope[j]+=(-2/M)*(points[i,n+1]-small_sum)*(points[i,j])
        for j in range(n+1):
            new_m[j]=m[j]-learning_rate*m_slope[j]    
    return new_m   

def cost(points,m):
    total_cost=0
    n=4        #Number of regressors
    M=len(points)
    for i in range(M):
        small_cost=0
        y=points[i,n+1]
        for j in range(n):
            x=points[i,j]
            small_cost+=m[j]*x
        total_cost=(1/M)*((y-small_cost)**2)
    return total_cost

def gd(points,learning_rate,num_iterations):
    n=4        #Number of regressors
    m=np.zeros(n+1,dtype=float)
    for i in range(num_iterations):
        m=step_gradient(points,learning_rate,m)
        print(i,"cost:",cost(points,m))
    return m

def run():
    learning_rate=0.0000001   # by trial and error
    num_iterations=100        # higher value for more accuracy
    m=gd(points,learning_rate,num_iterations)
    print(m)

run()
