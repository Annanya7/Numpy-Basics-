# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 11:00:59 2021

@author: hp
"""

#%%
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

#%%
#Use a tuple to create a NumPy array:
import numpy as np
arr = np.array((1, 2, 3, 4, 5))
print(arr)

#%%
#Create a 1-D array containing the values 1,2,3,4,5:
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)

#%%
#Check how many dimensions the arrays have:

import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

#%%
#Indexing
import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr[1])

#%%
#Access the 2nd element on 1st dim:

import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st dim: ', arr[0, 1])

#%%
#slicing
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[:4])

#%%
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5:2])

#%%
#Datatypes
import numpy as np
arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)

#%%
#import numpy as np

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')

print(newarr)
print(newarr.dtype)
#%%
#Copy
#Make a copy, change the original array, and display both arrays:

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)

#%%
#View
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)


#%%
#reshape
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)

#%%
#iteration
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
  for y in x:
    print(y)
    
#%%
#join
arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)

print(arr)

#%%
#Split
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 4)
print(newarr)

#%%
#search 
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 0)
print(x)

#%%
#Sort
#Sort the array alphabetically:
arr = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr))

#%%


















