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
