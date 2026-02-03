#violin plot
import seaborn as sns
import matplotlib.pyplot as plt
tips=sns.load_dataset("tips")
sns.violinplot(x="day", y="total_bill", data=tips, hue="sex", split=True)
plt.title("Violin plot of Total Bill by Day and Gender")
plt.show()