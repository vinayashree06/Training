import numpy as np
a1=np.array([1,2,3])
a2=np.array([[1,2],[3,4]])
a3=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])

print(a1)
print(a2)
print(a3)

a0=np.zeros([3,4])
a1=np.ones([2,2])
ar=np.arange(0,10,2)

print(a0)
print(a1)
print(ar)

a1=np.array([10,20,30,40])
print(a1[2])
a2=np.array([[10,20,30],[40,50,60],[70,80,90]])
print(a2[1,2])

a=np.array([10,20,30,40,50,60])
idx=np.array([1,3,5])

print(a[idx])

cond=a>30
print(a[cond])

x=np.array([1,2,3])
y=np.array([4,5,6])
print(x+y)
print(x-y)
print(x*y)
print(x/y)

#unary operations
a=np.array([-1,2,-3,4])
print(np.abs(a))

#binary operations
a=np.array([1,2,3])
b=np.array([4,5,6])
print(np.add(a,b))

#create an array of sine values
a=np.array([0,np.pi/2,np.pi])
print(np.sin(a))

b=np.array([0,1,2,3])
print(np.exp(b))
print(np.sqrt(b))
print(np.sqrt(a))

#Sorting arrays
dtypes = [('name', 'S10'), ('age', int)]
values = [(b'John', 25), (b'Alice', 30), (b'Bob', 20)]
arr = np.array(values, dtype=dtypes)
print(np.sort(arr, order='age'))
print(np.sort(arr, order='name'))

#create numpy arrays using lists or tuples
my_list = [1, 2, 3, 4, 5]
my_tuple = (6, 7, 8, 9, 10)
array_from_list = np.array(my_list)
array_from_tuple = np.array(my_tuple)
print(array_from_list)
print(array_from_tuple)

#initialize python numpy array using special functions
zeros_array = np.zeros((3, 3))
ones_array = np.ones((2, 4))
range_array = np.arange(0, 20, 5)
linspace_array = np.linspace(0, 1, 5)
constant_array = np.full((2, 3), 7)
print(zeros_array)
print(ones_array)
print(constant_array)
print(range_array)
print(linspace_array)

#random number generation
random_array = np.random.rand(3, 3)
print(random_array)
random_integers = np.random.randint(1, 10, size=(2, 2))
print(random_integers)

#create python numpy arrays using matrix creation routines
identity_matrix = np.eye(3)
diagonal_matrix = np.diag([1, 2, 3, 4])
zeros_like_matrix = np.zeros_like(diagonal_matrix)
ones_like_matrix = np.ones_like(identity_matrix)
print(identity_matrix)
print(diagonal_matrix)
print(zeros_like_matrix)
print(ones_like_matrix)

#random sampling in numpy
sampled_array = np.random.choice([10, 20, 30, 40, 50], size=3, replace=False)
print(sampled_array)

arr=np.random.randint(1,10,size=(2,3))
print(arr)

#normal distribution in numpy
normal_dist=np.random.normal(loc=0.0, scale=1.0, size=(3,3))
print(normal_dist)

#visualizing the binomial distribution
import matplotlib.pyplot as plt
from scipy.stats import binom
n, p = 10, 0.5
size=1000
data=np.random.binomial(n, p, size)
plt.hist(data, bins=np.arange(-0.5, n+1.5, 1), density=True, edgecolor='black', alpha=0.7, label='Histogram')
x=np.arange(0, n+1)
pmf=binom.pmf(x, n, p)
plt.scatter(x, pmf, color='red', label='TheoreticalPMF')
plt.vlines(x, 0,pmf, colors='red', linestyles='dashed')
plt.title('Binomial Distribution (n=10, p=0.5)')
plt.xlabel('Number of Successes')
plt.ylabel('Probability')   
plt.legend()
plt.grid(True)
plt.show()