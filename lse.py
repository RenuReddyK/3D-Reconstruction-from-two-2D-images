import numpy as np

def least_squares_estimation(X1, X2):
  """ YOUR CODE HERE
  """
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
      # print(a)
      A[i,:9] = a

  #print("A",A)
  #print(A.shape)

  # A=a
  # print(A)
  # a = np.matmul(A.T,A)
  # print("a",a)
  u, d, vt = np.linalg.svd(A)
  # print(vt)
  E_dash = vt[8,:]
  #print("E_dash",E_dash)
  #print("vt",vt)
  E_dash = E_dash.reshape((3,3))
  # print("E_dash",E_dash)
  # print(E_dash.shape)
  U, D, Vt = np.linalg.svd(E_dash.T)
  # print(U.shape)
  # print(Vt.shape)
  E = np.matmul(np.matmul(U,np.diag([1,1,0])),Vt)
  # print("E",E)
  # print(E.shape)
  # v=np.arange(9)
  # print(v)
  # A=v.reshape(3,3)
  # print(A)
  # print(A)

  """ END YOUR CODE
  """
  return E

if __name__ == '__main__':
    X1 = np.array([[1,2,3],[4,5,6]])
    print(X1.shape)
    X2 = np.array([[7,8,9],[10,11,12]])
    print(least_squares_estimation(X1, X2))
