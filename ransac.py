from lse import least_squares_estimation
import numpy as np

def ransac_estimator(X1, X2, num_iterations=60000):
    sample_size = 8

    eps = 10**-4

    best_num_inliers = -1
    best_inliers = None
    best_E = None

    for i in range(num_iterations):
        permuted_indices = np.random.RandomState(seed=(i*10)).permutation(np.arange(X1.shape[0]))
        sample_indices = permuted_indices[:sample_size]
        test_indices = permuted_indices[sample_size:]

        inliers = sample_indices
        newX1 = []
        newX2 = []
        T2  = []
        T1 = []
        for j in sample_indices:
            newX1.append(X1[j])
            newX2.append(X2[j])
            
        newX1 = np.array(newX1)
        newX2 = np.array(newX2)
        count = 0
        E = least_squares_estimation(newX1, newX2)
        e3 = np.array([0,0,1])
        
        for k in test_indices:
            x1= X1[k]
            x2 = X2[k]

            d1 = ((np.matmul(x2.T,np.matmul(E,x1)))**2)/((np.linalg.norm(np.cross(e3,np.matmul(E,x1))))**2)
            d2 = ((np.matmul(x1.T,np.matmul(E.T,x2)))**2)/((np.linalg.norm(np.cross(e3,np.matmul(E.T,x2))))**2)
            r = d1 + d2

            if r < eps:
                inliers = np.append(inliers,k)

        if inliers.shape[0] > best_num_inliers:
            best_num_inliers = inliers.shape[0]
            best_E = E
            best_inliers = inliers

    return best_E, best_inliers

