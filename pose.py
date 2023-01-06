import numpy as np

def pose_candidates_from_E(E):
  transform_candidates = []
  ##Note: each candidate in the above list should be a dictionary with keys "T", "R"
  """ YOUR CODE HERE
  """
  U, D, Vt = np.linalg.svd(E)
  Rp = np.matrix([[0,-1,0],[1,0,0],[0,0,1]])
  Rn = np.matrix([[0,1,0],[-1,0,0],[0,0,1]])
  r1 = np.matmul(np.matmul(U,Rp.T),Vt)
  r2 = np.matmul(np.matmul(U,Rn.T),Vt)
  r3 = np.matmul(np.matmul(U,Rp.T),Vt)
  r4 = np.matmul(np.matmul(U,Rn.T),Vt)
  Tpz = [0,0,1]
  Tnz = [0,0,-1]
  # t1 = np.cross(U,Tpz)
  # t2 = np.cross(U,Tnz)
  # t3 = np.cross(-U,Tpz)
  # t4 = np.cross(-U,Tnz)
  t1 = U[:3,2]
  t2 = t1
  t3 = -U[:3,2]
  t4 = t3
  # t3 = np.cross(-U,Tpz)
  # t4 = np.cross(-U,Tnz)
  a1 = {"T": t1,"R": r1}
  a2 = {"T": t2,"R": r2}
  a3 = {"T": t3,"R": r3}
  a4 = {"T": t4,"R": r4}
  transform_candidates.append(a1)
  transform_candidates.append(a2)
  transform_candidates.append(a3)
  transform_candidates.append(a4)
  """ END YOUR CODE
  """
  return transform_candidates
