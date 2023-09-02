# Linear-Regression-Using-Gradient-Descent

Gradient descent is an optimization algorithm used in Machine Learning and Deep Learning to minimize a cost function or loss function. The goal of gradient descent is to find the set of parameters (weights and biases) for a model that minimize the cost function and make the model perform better on the training data.
Here's how gradient descent works:

1)**Initialization**: Start with an initial set of parameters (weights and biases), often chosen randomly.

2)**Compute the Gradient**: Calculate the gradient of the cost function with respect to each parameter. The gradient represents the direction and magnitude of the steepest increase in the cost function. This is done using the chain rule of calculus, which computes how a small change in each parameter affects the cost function.

3)**Update Parameters**: Adjust the parameters in the opposite direction of the gradient to minimize the cost function. This is typically done using the following update rule:

               parameter = parameter - learning_rate * gradient

  Here, the learning rate is a hyperparameter that determines the step size of each iteration. It's crucial to choose an appropriate learning rate; too large a learning rate 
  can cause the algorithm to overshoot the minimum, and too small a learning rate can make convergence slow.

4)**Repeat**: Steps 2 and 3 are repeated iteratively for a fixed number of iterations or until a convergence criterion is met. The convergence criterion can be a small change in the cost function or a maximum number of iterations.

5)**Result**: The final set of parameters obtained after the iterations should be a local minimum of the cost function, meaning it's a point where the cost is relatively low compared to its immediate neighbors.

There are variations of gradient descent, including:

_Stochastic Gradient Descent (SGD)_: Updates the parameters using a single random training example at each iteration. This can lead to faster convergence but can also introduce more noise.

_Mini-Batch Gradient Descent_: Updates the parameters using a small random subset of the training data at each iteration. It strikes a balance between the efficiency of SGD and the stability of batch gradient descent.

_Batch Gradient Descent_: Computes the gradient using the entire training dataset at each iteration. It can be slow for large datasets but provides a more stable convergence.

_Adaptive Learning Rate Methods_: These methods adjust the learning rate during training, such as Adagrad, RMSprop, and Adam, to overcome some of the challenges of choosing a fixed learning rate.

**This code uses the Batch Gradient Descent method.**

Gradient descent is a fundamental optimization technique used in training a wide range of machine learning models, including linear regression, logistic regression, neural networks, and many others. Its effectiveness relies on the convexity and smoothness of the cost function, and its efficiency can be improved with various optimization techniques and variants.


<img width="208" alt="image" src="https://github.com/RonSheoran123/Linear-Regression-Using-Gradient-Descent/assets/106268100/0af5a270-e1fe-424e-9402-2ae274003be2">

<img width="193" alt="image" src="https://github.com/RonSheoran123/Linear-Regression-Using-Gradient-Descent/assets/106268100/c6f16210-d4fc-4b6f-8942-b8c6d901e2f2">

