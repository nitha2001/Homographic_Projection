import numpy as np


def est_homography(X, Y):
    """
    Calculates the homography of two planes, from the plane defined by X
    to the plane defined by Y. In this assignment, X are the coordinates of the
    four corners of the soccer goal while Y are the four corners of the penn logo

    Input:
        X: 4x2 matrix of (x,y) coordinates of goal corners in video frame
        Y: 4x2 matrix of (x,y) coordinates of logo corners in penn logo
    Returns:
        H: 3x3 homogeneours transformation matrix s.t. Y ~ H*X

    """

    ##### STUDENT CODE START #####
    a=np.zeros((8,9),dtype=float)
    i=0
    for i in range(X.shape[0]):
        a[(2*i)] = [-X[i,0],-X[i,1],-1,0,0,0,X[i,0]*Y[i,0],X[i,1]*Y[i,0],Y[i,0]]
        a[(2*i)+1] = [0,0,0,-X[i,0],-X[i,1],-1,X[i,0]*Y[i,1],X[i,1]*Y[i,1],Y[i,1]]

    U,S,Vh = np.linalg.svd(a ,full_matrices=True)
    H=Vh[-1,:]
    H = np.reshape(H,[3,3])
    print(H)
    ##### STUDENT CODE END #####

    return H

