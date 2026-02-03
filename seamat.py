#Plotting with seaborn and matplotlib
import seaborn as sns
import matplotlib.pyplot as plt
plt.plot([0,1],[10,11],label="line 1")
plt.plot([0,1],[11,10],label="line 2")
plt.scatter([0,1],[10.5,10.5],color='blue',marker='o',label="dots")
plt.xlabel("X axis")
plt.ylabel("Y axis")    
plt.title("Simple Plot with Lines and Dots")
plt.legend()    
plt.show()