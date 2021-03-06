import numpy as np
import pdb

# Write your code here for camera calibration (lab)
def camera_calibration(pt_3d, matches):
    """
    write your code to compute camera matrix
    """
    #pt_3d: points location in 3d, np array with size: k x 3. [x,y,z].
    #k is the 3d points number.
    #3: 3 dimension: [x,y,z]

    #matches: np array with size: (k,4). 
    #k is the match pairs number. 
    #4 is location in each match pair:[x_axis_img1, y_axis_img1, x_axis_img2, y_axis_img2]

    #return P: project matrix: np array (3,4)
    #return K: fundamental matrix, np array (3,3)
    #return R: rotation matrix, np array (3,3)
    #return c: camera center, np array (4,)

    f = []
    for n in range(matches.shape[0]):
        x, y, z, u, v = pt_3d[n,0], pt_3d[n,1], pt_3d[n,2], matches[n,0], matches[n,1]
        f.append([x,y,z,1,0,0,0,0, -u*x, -u*y, -u*z, -u])
        f.append([0, 0, 0, 0, x, y, z, 1, -v * x, -v * y, -v * z, -v])

    w, v = np.linalg.eig(np.dot(np.mat(f).T, np.mat(f)))
    P = np.reshape(v[:, np.argsort(w)[0]],(3,4))
    c = np.dot(np.linalg.inv(-P[:, 0:3]), P[:, 3])
    R, K = np.linalg.qr(P[:,:3])

    # <YOUR CODE>

    return P.A, K, R, c
