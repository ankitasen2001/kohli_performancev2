import numpy as np
import matplotlib.pyplot as plt

x= np.arange(0, 3*np.pi, 0.1)
y = np.sin(x)
print(y)

plt.plot(x,y)
plt.show()

print("i am here")


import numpy as np
import matplotlib.pyplot as plt

x= np.arange(0, 3*np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)


plt.plot(x,y_sin)
plt.plot(x, y_cos)
plt.xlabel('x axis lable')
plt.ylabel('y axis label')
plt.title('sine'and 'cosine')
plt.legend('sine', 'cosine')
plt.show()

print("i am here")

import numpy as np
import matplotlib.pyplot as plt

x= np.arange(0, 3*np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.subplot(2,1,1)
plt.plot(x,y_sin)

plt.subplot(2,1,2)
plt.plot(x, y_cos)

plt.xlabel('x axis lable')
plt.ylabel('y axis label')
plt.title('sine'and 'cosine')
plt.legend('sine', 'cosine')
plt.show()

print("i am here")



x=np.linspace(-20,20,1000)

def func(x):
    y=[]
    for elem in x:
        # result=x**2
        result=5*(elem**2)+4*elem
        y.append(result)
    return y
y=func(x)
plt.plot(x,y)
plt.show()

