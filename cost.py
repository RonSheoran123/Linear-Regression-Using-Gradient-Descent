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
