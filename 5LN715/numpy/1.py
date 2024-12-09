import numpy as np
a = np.array([1, 2, 3, 4])
b = np.array([1, 2, 3, 4])
print(a * b) #claculates the element wise multiplication, [1*1, 2*2, 3*3, 4*4],resulting in [1, 4, 9, 16]
#the meaning is transforming the two arrays into a new array with the same shape, and the elements of the new array are the product of the corresponding elements of the two arrays
print(np.dot(a, b)) #claculates the dot product of the two arrays, 1*1 + 2*2 + 3*3 + 4*4, resulting in 30

c = np.array([[1,0,2], [1,2,0], [0,1,2]])
d = np.array([[1,2,3], [2,3,1], [3,1,2]])

print(c)
print(d)
print(c*d)#claculates the element wise multiplication, [[1*1, 0*2, 2*3], [1*2, 2*3, 0*1], [0*3, 1*1, 2*2]], resulting in [[1, 0, 6], [2, 6, 0], [0, 1, 4]]
print(np.dot(c, d))#claculates the dot product of the two arrays, [[1*1+0*2+2*3, 1*2+0*3+2*1, 1*3+0*1+2*2], [1*1+2*2+0*3, 1*2+2*3+0*1, 1*3+2*1+0*2], [0*1+1*2+2*3, 0*2+1*3+2*1, 0*3+1*1+2*2]], resulting in [[5, 4, 7], [5, 8, 5], [5, 5, 5]]

e = np.array([[1,2,3], [1,1,0], [1,1,1]])
f = np.array([[0,1,1], [1,2,1]])


#print(np.dot(e, f))

g = np.array([[1,2,3], [1,1,0], [1,1,1]])

h = g.reshape(len(g)*len(g))
#for example, if g is a 3*3 matrix, then len(g) is 3, so len(g)*len(g) is 9, so the reshape function will transform the 3*3 matrix into a 1*9 matrix
#for example, if g is a 2*3 matrix, then len(g) is 2, so len(g)*len(g) is 6, so the reshape function will transform the 2*3 matrix into a 1*6 matrix

print(h)