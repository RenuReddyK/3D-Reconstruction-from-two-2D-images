import numpy as np
import matplotlib.pyplot as plt

def show_reprojections(image1, image2, uncalibrated_1, uncalibrated_2, P1, P2, K, T, R, plot=True):

  """ YOUR CODE HERE
  """
  P1proj =[]
  P2proj =[]
  T = T.reshape((3,1))
  print("t",T.shape)
  print("r",R.shape)
  print("k",K.shape)
  print("p1",P1.shape)
  print("UC1",uncalibrated_1.shape)
  for i in range(uncalibrated_1.shape[1]):
      p1 = P1[i,:3].reshape((3,1))
      print("p1",p1)
      p2 = (P2[i,:3]).reshape((3,1))
      P2proj_2 = np.matmul(K,np.matmul(np.linalg.inv(R),(p2-T)))
      P1proj_1 = np.matmul(K,np.matmul(R,p1) +  T)
      P1proj_1 = P1proj_1.reshape((1,3))
      P2proj_2 = P2proj_2.reshape((1,3))
      print("P1PROJ",P1proj_1)
      print("P2PROJ",P2proj_2)
      P1proj= np.append(P1proj,P1proj_1)
      P2proj = np.append(P2proj,P2proj_2)
      print("working till here")
  P1proj = np.array(P1proj).reshape(uncalibrated_1.shape[1],uncalibrated_1.shape[0])
  P2proj = np.array(P2proj).reshape(uncalibrated_2.shape[1],uncalibrated_2.shape[0])

  print("P1PROJ",P1proj.shape)
  print("P2PROJ",P2proj.shape)

  # P2proj = np.matmul(np.matmul(P1,R),uncalibrated_1) + T
  # P1proj = np.matmul(P2,uncalibrated_2) - T

 # print("p1",P1.shape) #shape = n x 3
  #print("p2",P2.shape)
  # P1proj = np.matmul(P1,R) + T
  # P2proj = np.matmul(P2,R) + T
  """ END YOUR CODE
  """

  if (plot):
    plt.figure(figsize=(6.4*3, 4.8*3))
    ax = plt.subplot(1, 2, 1)
    ax.set_xlim([0, image1.shape[1]])
    ax.set_ylim([image1.shape[0], 0])
    plt.imshow(image1[:, :, ::-1])
    plt.plot(P2proj[:, 0] / P2proj[:, 2],
           P2proj[:, 1] / P2proj[:, 2], 'bs')
    plt.plot(uncalibrated_1[0, :], uncalibrated_1[1, :], 'ro')

    ax = plt.subplot(1, 2, 2)
    ax.set_xlim([0, image1.shape[1]])
    ax.set_ylim([image1.shape[0], 0])
    plt.imshow(image2[:, :, ::-1])
    plt.plot(P1proj[:, 0] / P1proj[:, 2],
           P1proj[:, 1] / P1proj[:, 2], 'bs')
    plt.plot(uncalibrated_2[0, :], uncalibrated_2[1, :], 'ro')

  else:
    return P1proj, P2proj
