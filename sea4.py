import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="whitegrid")
iris=sns.load_dataset("iris")
sns.swarmplot(x="species", y="sepal_length", data=iris )
plt.title("Swarm plot of Sepal Length by Species")
plt.show()