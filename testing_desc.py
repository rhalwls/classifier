def deri1(theta1):
    return 2*theta1

def deri2(theta2):
    return 2*theta2


def func(theta1, theta2):
    return pow(theta1,2)+pow(theta2,2)

def deri(data_1feature, xat):
    #(y(x+delta x) - y(x))/delta x
    data_1feature[xat]


"""
theta1_old = 0
theta1_new = 6 # The algorithm starts at x=6

theta2_old = 0
theta2_new =8
eps = 0.01 # step size
precision = 0.00001


i=0
while abs(theta1_new - theta2_old) > precision or abs(theta2_new-theta2_old)>precision:
    i+=1
    theta1_old = theta1_new
    theta1_new = theta1_old - eps * deri1(theta1_old)
    theta2_old = theta2_new
    theta2_new = theta2_old - eps * deri2(theta2_old)
    print("iteration # ",i ,"  new theta1 :",theta1_new," new theta2 : ",theta2_new)
"""
import matplotlib.pyplot as plt
import numpy as np


y = [2, 3, 1] #x 의 순서에 따라 value
x = np.arange(len(y))
xlabel = ['가', '나', '다']
plt.title("Bar Chart")
plt.bar(x, y)
plt.xticks(x, xlabel)
plt.yticks(sorted(y))
plt.xlabel("가나다")
plt.ylabel("빈도 수")
plt.show()
plt.xlabel('x label')
plt.show()

plt.show()