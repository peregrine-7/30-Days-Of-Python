import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

print('numpy:', np.__version__)

python_list = [1,2,3,4,5]
print('Type:', type(python_list))
print(python_list)
two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]
print(two_dimensional_list)
numpy_array_from_list = np.array(python_list)
print(type(numpy_array_from_list))
print(numpy_array_from_list)

numpy_bool_array = np.array([0,1,-1,0,0], dtype=bool)
print(numpy_bool_array)
numpy_two_dimensional_list = np.array(two_dimensional_list)
print(numpy_two_dimensional_list)
np_to_list = numpy_array_from_list.tolist()
print(np_to_list)


numpy_array_from_list = np.array([1,2,3,4,5])
print(numpy_array_from_list + 10)

print(np.array([-3,-2,0,1,2,3], dtype = 'bool'))
two_dimension_array = np.array([[1,2,3],[4,5,6],[7,8,9]])
two_dimension_array[1,1] = 55
two_dimension_array[1,2] = 44
print(two_dimension_array)
print(two_dimension_array[::-1,::-1])

np_list_one = np.array([1,2,3])
np_list_two = np.array([4,5,6])
print(np_list_one + np_list_two)
print(np.hstack((np_list_one, np_list_two)))

print(np.vstack((np_list_one, np_list_two)))

print(np.random.normal(0,1,5))
normal_array = np.random.normal(79,15,80)

sns.set()
plt.hist(normal_array, color = 'grey', bins=50)

four_by_four_matrix = np.matrix(np.ones((4,4),dtype=float))
print(four_by_four_matrix)
np.asarray(four_by_four_matrix)[2] = 2
print(four_by_four_matrix)

lst = range(0,11,2)
print(lst)
for l in lst:
    print(l)
print(np.linspace(1.0, 5.0, num=10))
print(np.linspace(1.0,5.0,num=5,endpoint=False))

print(np.logspace(2, 4.0, num=4))

x = np.array([1,2,3], dtype = np.complex128)
print(x)
print(x.itemsize)

np_normal_dis = np.random.normal(5, 0.5, 1000)

print(np.mean(np_normal_dis))
print(np.std(np_normal_dis))
plt.hist(np_normal_dis, color="grey", bins=21)
# plt.show()

f = np.array([1,2,3])
g = np.array([4,5,3])
print(np.dot(f,g))

h = [[1,2],[3,4]]
i = [[5,6],[7,8]]
print(np.matmul(h,i))
print(np.linalg.det(i))

Z = np.zeros((8,8))
Z[1::2,::2] = 1
Z[::2,1::2] = 1
print(Z)