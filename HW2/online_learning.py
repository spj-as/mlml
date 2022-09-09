#%%


def cal(p,N,m):
    R,r = 1,1
    for i in range(m+1,N+1):
        R *= i
    for i in range(1,N-m+1):
        r *= i
    return ( R / r ) * ( p ** m ) * ( (1-p)** (N-m) )

a = 0
b = 0
case = 1
with open("input.txt", "r") as f:

    for line in f:
        line = line.strip('\n')
        print("case ", case, ":", line)
        count=[0,0]
        for i in range(len(line)):
            count[int(line[i])] += 1
        p = count[1] / len(line)
        likelihood = cal(p , len(line) , count[1])
        print("Likelihood:", likelihood)
        print("Beta prior    : ","a =" ,a," b =", b)
        a += count[1]
        b += count[0]
        print("Beta posterior: ","a =" ,a," b =", b)
        case += 1
#%%
import matplotlib.pyplot as plt
import numpy as np

def cal(N , m , p):
    R,r = 1,1
    for i in range(m+1,N+1):
        R *= i
    for i in range(1,N-m+1):
        r *= i
    return ( R / r ) * ( p ** m ) * ( (1-p)** (N-m) )


def beta (p, a, b):
    A,B,C = 1,1,1
    for i in range(1,a+1):
        A *= i
    for i in range(1,b+1):
        B *= i
    for i in range(1,a+b+1):
        C *= i   
    return  (p ** (a-1)) * ((1-p) ** (b-1)) / (A * B)  * C
case = 1
x_ = np.linspace(0,1,100)



a = int(input("a = "))
b = int(input("b = "))
with open("input.txt", "r") as f:
    for line in f:
        line = line.strip('\n')
        print("case ", case, ":", line)
        count=[0,0]
        for i in range(len(line)):
            count[int(line[i])] += 1
        m = count[1] 
        N = count[0] + count[1] 
        
        if a != 0 and b != 0:
            f, axes = plt.subplots(1, 3, figsize = (9,4))
            axes[0].set_title("prior")
            axes[1].set_title("likelihood")
            axes[2].set_title("posterior")

            #prior
            y_prior = [0.0 for i in range (100)] 
            for i in range(len(x_)) :
                y_prior[i] = beta(x_[i], a, b)
            axes[0].plot(x_, y_prior, color="red") 


            #likelihood
            y_like = [0.0 for i in range (100)]
            for i in range (len(x_)) :
                y_like[i] = cal(N, m, x_[i])
            axes[1].plot(x_, y_like, color="blue") 

            #posterior
            y_post =  [0.0 for i in range (100)]
            for i in range(len(x_)) :
                y_post[i] = beta(x_[i], a + m, b + N - m) 
            axes[2].plot(x_, y_post, color="red") 
            plt.show()

        p = count[1] / len(line)
        likelihood = cal(len(line) , count[1] , p)
        print("Likelihood:", likelihood)
        print("Beta prior    : ","a =" ,a," b =", b)
        a += count[1]
        b += count[0]
        print("Beta posterior: ","a =" ,a," b =", b)
        case += 1
        print()

# %%
