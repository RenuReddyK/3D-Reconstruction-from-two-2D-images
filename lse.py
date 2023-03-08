import numpy as np

def least_squares_estimation(X1, X2):

  N = X1.shape[0]
  A = np.zeros((N,9))
  a =[]
  for i in range(N):
      px = X1[i][0]
      py = X1[i][1]
      pz = X1[i][2]
      ax = px * X2[i,:]
      ay = py * X2[i,:]
      az = pz * X2[i,:]
      a = np.hstack((ax,ay,az))
      A[i,:9] = a
  
  u, d, vt = np.linalg.svd(A)
  E_dash = vt[8,:]
  E_dash = E_dash.reshape((3,3))

  U, D, Vt = np.linalg.svd(E_dash.T)

  E = np.matmul(np.matmul(U,np.diag([1,1,0])),Vt)

  return E

if __name__ == '__main__':
    X1 = np.array([[1,2,3],[4,5,6]])
    print(X1.shape)
    X2 = np.array([[7,8,9],[10,11,12]])
    print(least_squares_estimation(X1, X2))
