def run():
    learning_rate=0.0000001   # chosen by trial and error
    num_iterations=100        # higher value for more accuracy
    m=gd(points,learning_rate,num_iterations)
    print(m)
