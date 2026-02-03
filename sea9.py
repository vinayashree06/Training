#Enhancing matplotlib with seaborn styles
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="darkgrid")
x=[1,2,3,4,5]
y=[10,12,15,18,22]
plt.plot(x,y,marker='o',linestyle='-',color='blue',label='Data Line')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('MatPlotlib  with Seaborn Darkgrid Style')
plt.legend()    
plt.show()