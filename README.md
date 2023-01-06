# 3D-Reconstruction-from-two-2D-images

![0017_2](https://user-images.githubusercontent.com/68454938/210909831-8f450215-5aca-4390-bb2e-ebbb68efb398.png)

        Image 1 for 3d reconstruction

![0014_2](https://user-images.githubusercontent.com/68454938/210909822-422f94c2-6e71-44b2-b341-c07d8e9bcf69.png)

        Image 2 for 3d reconstruction

Reconstructed the scene from two images (shown above) using the SIFT matchings. The SIFT descriptors are simply computed and matched using OpenCV.

![s2](https://user-images.githubusercontent.com/68454938/210909184-438f49d9-9d2e-4cfe-aa52-6a8a015e75d9.png)
        
        SIFT features for image 1

![s1](https://user-images.githubusercontent.com/68454938/210909170-7c38ad96-f885-4b35-b089-8a960b67413e.png)

        SIFT features for image 2

RANSAC estimation: The estimation of E can be made much more robust by selecting sets of points that reach a common agreement (eliminating outliers or spurious matchings) and obtain a better estimate of E. The epipolar lines are drawn using the essential matrix E (for calibrated points).

![3](https://user-images.githubusercontent.com/68454938/210909229-ff161d88-76de-4382-b690-b6c1655b34f1.png)

        Keypoint matching between two images
    
To recover the transformation R, T between the two cameras, SVD decomposition of E is done. For a given estimate of E, there are two possible solutions for (T, R) due to the twisted pair ambiguity. So there are four possible solutions for (R, T), considering twisted pair ambiguity of E and -E.

![output](https://user-images.githubusercontent.com/68454938/210909494-aed6a23e-ab1b-4cd6-aa9a-786634463b00.png)
        
        RANSAC Inlier Matches


![5](https://user-images.githubusercontent.com/68454938/210909557-f101715c-3dc3-41c5-9ec5-5ff2eb33b217.png)

        Epipolar lines

Then triangulation is done to check whether a given candidate pair of (R, T) is the correct transformation (one out of the four candidates). This is one by  picking the candidate that has the highest number of reconstructed points in front of both the cameras. 

![6](https://user-images.githubusercontent.com/68454938/210909721-90e3b6b0-fbf1-46a3-8f2b-c5805d124b5a.png)


![7](https://user-images.githubusercontent.com/68454938/210909682-2eff7638-95ee-4ae4-b4c9-1eea2d5d0422.png)


