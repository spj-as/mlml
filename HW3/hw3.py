#%%
from statistics import variance
from tkinter import Variable
import numpy as np
import math
import matplotlib.pyplot as plt

def Guassian(variance, mean):
    U , V, S = 0, 0, 0 
    while True:
        U = np.random.uniform(-1,1)
        V = np.random.uniform(-1,1)
        S = U**2 + V**2
        if S < 1:
            break
    X = U * ((-2 * math.log(S))/S) ** (1/2)
    return X * (variance ** (1/2)) + mean  

def drawPlot(axs, title, W_GT, var, a, points):
    axs.set_title(title)
    axs.set_xlim(-2, 2)
    axs.set_ylim(-15, 20)
    Xs = np.linspace(-2, 2, 1000)
    Ys = Xs * 0
    for i in range(len(W_GT)):
        Ys += W_GT[i] * (Xs ** i)
    axs.plot(Xs, Ys, color='black')

    if len(points) == 0:
        Ys = Ys + a
        axs.plot(Xs, Ys, color='r')
        Ys = Ys - 2 * a
        axs.plot(Xs, Ys, color='r')
    # else:
    #     pointsArray = np.array(points).T
    #     axs.scatter(pointsArray[0], pointsArray[1], color='blue', s=10)

    #     Ys_upper = Xs * 0
    #     Ys_lower = Xs * 0
    #     for i in range(1000):
    #         X = np.zeros((1, len(W_GT)))
    #         for j in range(len(W_GT)):
    #             X[0][j] = Xs[i] ** j
    #         Ys_upper[i] = Ys[i] + a + X.dot(var).dot(X.T).item()
    #         Ys_lower[i] = Ys[i] - a - X.dot(var).dot(X.T).item()
    #     axs.plot(Xs, Ys_upper, color='r')
    #     axs.plot(Xs, Ys_lower, color='r')

    plt.draw()
def inverse(M,n):
        a =  [[0 for i in range(n*2)] for j in range(n)]
        for i in range(n):
            for j in range(n):
                if i==j:
                    a[i][j+n]=1
        # Reading matrix coefficients
        for i in range(n):
            for j in range(n):
                a[i][j] = float(M[i,j])

        # Applying Guass Jordan Elimination
        for i in range(n):
            if a[i][i] == 0.0:
                continue
            for j in range(n):
                if i != j:
                    ratio = a[j][i]/a[i][i]
                    for k in range(2*n):
                        a[j][k] = a[j][k] - ratio * a[i][k]

    # Row operation to make principal diagonal element to 1
        for i in range(n):
            div = a[i][i]
            for j in range(2*n):
                a[i][j] = a[i][j]/div
        ans =  Matrix(dim = (n, n), value = 0)  
        for i in range(n):
            for j in range(n):
                ans[i,j] = a[i][n+j]
        return ans    

if __name__ == "__main__":
    # mean_input = float(input("plz input mean: "))
    # variance_input = float(input("plz input variance: "))
    # mean = Guassian(mean_input, variance_input)
    # variance = 0
    # mean_error = 1
    # variance_error = 1
    # n = 1
    # while abs(mean_error) > 1e-4 or abs(variance_error) > 1e-4 :
    #     point = Guassian(mean_input, variance_input)
    #     n += 1
    #     mean_error = (point- mean)/ n
    #     variance_error = ((point-mean)** 2)/n - variance/(n-1)
    #     mean += mean_error
    #     variance += variance_error
    #     # print(f"Mean = {mean} Variance = {variance}")

    # print("num of point =", n)
    # print("mean_error =", mean_error)
    # print("variance_error", variance_error)
    b = float(input("b = "))
    n = int(input("n = "))
    a = float(input("a = "))
    W_GT = np.zeros((n, 1), dtype=float)
    for i in range(n):
        W_GT[i] = float(input(f"W[{i}] = "))

    points = []
    mean = np.zeros((n, 1), dtype=float)
    var = np.eye(n, dtype=float) * 1/b
    predic_mean = 0.
    predic_var = 0.
    err = 1
    c = 0

    f, axs = plt.subplots(2, 2, figsize=(10, 10))
    drawPlot(axs[0][0], "Ground truth", W_GT, var, a, points) 
    while abs(mean_error) > 1e-4:
        newpoint = Gaussian(0.0, a)
        x = np.random.uniform(-1.0, 1.0)
        for i in range(len(W)):
            newpoint += W[i] * (x ** i)
        point.append((x,newpoint))    
        c += 1
        X = np.zero
        



# %%
