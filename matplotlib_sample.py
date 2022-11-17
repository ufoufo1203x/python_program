import numpy as np
import matplotlib.pyplot as plt

data = [10,20,30,40,50]
x = [0,1,2,3,4,5]
y = [0,1,2,3,4,5]


plt.plot(x, y, linestyle='--', color='blue', marker='o', label='test1')
plt.plot(data, linestyle=':', color='green', marker='*', label='test2')

plt.legend(); #Explanatory note

plt.title('Demo') #Title
plt.xlabel('X') #X label
plt.ylabel('Y') #Y label
plt.grid(True); #Show grid