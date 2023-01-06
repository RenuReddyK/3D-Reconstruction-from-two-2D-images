from lse import least_squares_estimation
import numpy as np

def ransac_estimator(X1, X2, num_iterations=60000):
    sample_size = 8

    eps = 10**-4

    best_num_inliers = -1
    best_inliers = None
    best_E = None

    for i in range(num_iterations):
        # permuted_indices = np.random.permutation(np.arange(X1.shape[0]))
        permuted_indices = np.random.RandomState(seed=(i*10)).permutation(np.arange(X1.shape[0]))
        sample_indices = permuted_indices[:sample_size]
        test_indices = permuted_indices[sample_size:]

        """ YOUR CODE HERE
        """
        inliers = sample_indices
        print("inliers",inliers)
        # inliers= inliers.reshape((inliers.shape[0],1))
        print(inliers.shape)
        # print(sample_indices)
        # print(test_indices)
        newX1 = []
        newX2 = []
        T2  = []
        T1 = []
        for j in sample_indices:
            newX1.append(X1[j])
            newX2.append(X2[j])
        newX1 = np.array(newX1)
        newX2 = np.array(newX2)
        print(newX1.shape)
        # for p in test_indices:
        #     T1.append(X1[p])
        #     T2.append(X2[p])
        # T1 = np.array(T1)
        # T2 = np.array(T2)

        # T1 = X1[test_indices]
        # T2 = X2[test_indices]

        count = 0
        E = least_squares_estimation(newX1, newX2)
        print("E",E)
        e3 = np.array([0,0,1])
        #print(E3.shape)
        #e3 = np.matrix([[0,-1,0],[1,0,0],[0,0,0]])
        print(e3)
        print("X1",X1)
        print("T1",T1)
        for k in test_indices:
            x1= X1[k]
            x2 = X2[k]

            d1 = ((np.matmul(x2.T,np.matmul(E,x1)))**2)/((np.linalg.norm(np.cross(e3,np.matmul(E,x1))))**2)
            d2 = ((np.matmul(x1.T,np.matmul(E.T,x2)))**2)/((np.linalg.norm(np.cross(e3,np.matmul(E.T,x2))))**2)
            r = d1 + d2


            # print("r",r)
            if r < eps:
                # best_num_inliers = best_num_inliers + 1
                inliers = np.append(inliers,k)
                #inliers = np.append(inliers,x2)
        #print(inliers)

        """ END YOUR CODE
        """
        if inliers.shape[0] > best_num_inliers:
            best_num_inliers = inliers.shape[0]
            best_E = E
            best_inliers = inliers

    print("heyy",best_inliers.shape)
    print(best_E.shape)
    return best_E, best_inliers
# #
# if __name__ == '__main__':
#     X1 = np.array([[1,2,3],[4,5,6],[1,2,3],[4,5,6],[1,2,3],[4,5,6],[1,2,3],[4,5,6],[1,2,3],[4,5,6]])
#     print(X1.shape)
#     X2 = np.array([[7,8,9],[10,11,12],[7,8,9],[10,11,12],[1,2,3],[10,11,12],[7,8,9],[10,11,12],[7,8,9],[10,11,12]])
#     print(ransac_estimator(X1, X2, num_iterations=20))
