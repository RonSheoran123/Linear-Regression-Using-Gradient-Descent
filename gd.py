def gd(points,learning_rate,num_iterations):
    n=4  #Number of regressors
    m=np.zeros(n+1,dtype=float)
    for i in range(num_iterations):
        m=step_gradient(points,learning_rate,m)
        print(i,"cost:",cost(points,m))
    return m
