# import numpy as np
# list1 = np.array([2,4])
# print(list1)
# # O/P - [2 4]
# x = np.mean(list1)
# print(x)
# # O/P -3.0

#creating a rank1 array
import numpy as np
arr = np.array([1,2,3,4,5])
print("Array with rank1: \n",arr
)

#O/P 
'''
Array with rank1: 
 [1 2 3 4 5]

'''

#creating a rank1 array
import numpy as np
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print("Array with ranK2: \n",arr)

#O/P 
'''
Array with ranK2: 
 [[ 1  2  3  4  5]
 [ 6  7  8  9 10]]

'''

#create an array from tuple
import numpy as np
arr = np.array((1,2,3))
print("\n array created using" 
      "passed tuple: \n",arr)
      
'''
 array created usingpassed tuple: 
 [1 2 3]

'''