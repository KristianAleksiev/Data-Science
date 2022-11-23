"""
1. Data Modelling
- Understanding the processes that generate our data
- Function approximations as ML algorithms
- Computers learning with experience, without being explicitly programmed
- It's all about models

- Regression - model a function which returns a number(continuous variable) e.g. predict the temp tomorrow
- Classification -

Essence: Making a prediction about a function outputs, capturing patterns

2. Classification
Model a function which tries to differentiate between two or more predefined types of things(cat/dog).
Pre-defined Category.
3. Linear regression
- x, y, y(tilda) - modelling function
Goal: "Closest line" to the data - distance from point to line of each
- Orthogonal regression

N.B.!
- Local extrema -> sqrt(x**2), x**2, same line, =>( y(tilda) - y ) **2
- MEAN SQUARED ERROR => Sum(y(tilda) - y) ** 2, i e (0, n) / n
- TOTAL COST FUNCTION - best line => a, b: arguments that minimize the J(total cost function)
J depends on (x, y, a, b, n)=> x, y, n - fixed => J depends on (a, b) or J(a, b; x, y, n)

- FIRST DERIVATIVE  = 0

- Gradient, gradient descent
gradient - vector function

4. Logistic regression => Classification
- Sigmoid function, Generalized line model
"""