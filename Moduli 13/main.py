import numpy as np


arr_2d = np.array ([[0,1,2,3,4,5],[6,7,8,9,10,11]])
print(arr_2d)

element = arr_2d [1,4]
print(element)

dimensions = arr_2d.ndim
print(dimensions)

arr_size = arr_2d.size
print(arr_size)

total_sum = np.sum(arr_2d)
print(total_sum)

average = np.mean(arr_2d)
print(average)


sum_columns = np.sum(arr_2d ,axis=0)
print(sum_columns)

sum_rows = np.sum(arr_2d ,axis=1)
print(sum_rows)



reshaped_array = arr_2d.reshape((6,2))
print(reshaped_array)

sub_array = arr_2d[:2,:2]
print(sub_array)

sub_array_ = arr_2d[-3:,-3:]
print(sub_array_)

ret_tuple = arr_2d.shape
print(ret_tuple)

















