"""
Notes: Many of .dat files are written using Matlab. 
Hence, there are "-1" subtraction to Python 0-based indexing
"""

import math
import numpy as np
from config import _3DMM_DEFINITION_DIR


VERTEX_NUM = 53215
TRI_NUM = 105840

def load_3DMM_tri():
    # Triangle definition (i.e. from Basel model)

    print('Loading 3DMM tri ...')
   
    fd = open(_3DMM_DEFINITION_DIR + '3DMM_tri.dat')
    tri = np.fromfile(file=fd, dtype=np.int32)
    fd.close()
    #print tri

    tri = tri.reshape((3,-1)).astype(np.int32)
    tri = tri - 1
    tri = np.append(tri, [[ VERTEX_NUM], [VERTEX_NUM], [VERTEX_NUM]], axis = 1 )

    print('    DONE')
    return tri

def load_3DMM_vertex_tri():
    # Vertex to triangle mapping (list of all trianlge containing the cureent vertex)

    print('Loading 3DMM vertex tri ...')
   
    fd = open(_3DMM_DEFINITION_DIR + '3DMM_vertex_tri.dat')
    vertex_tri = np.fromfile(file=fd, dtype=np.int32)
    fd.close()

    vertex_tri = vertex_tri.reshape((8,-1)).astype(np.int32)
    #vertex_tri = np.append(vertex_tri, np.zeros([8,1]), 1)
    vertex_tri[vertex_tri == 0] = TRI_NUM + 1
    vertex_tri = vertex_tri - 1

    print('    DONE')
    return vertex_tri

def load_3DMM_vt2pixel():
    # Mapping in UV space

    fd = open(_3DMM_DEFINITION_DIR + 'vertices_2d_u.dat')
    vt2pixel_u = np.fromfile(file=fd, dtype=np.float32)
    vt2pixel_u = np.append(vt2pixel_u - 1, 0)
    fd.close()

    fd = open(_3DMM_DEFINITION_DIR + 'vertices_2d_v.dat')
    vt2pixel_v = np.fromfile(file=fd, dtype=np.float32)
    vt2pixel_v = np.append(vt2pixel_v - 1, 0)
    fd.close()

    return vt2pixel_u, vt2pixel_v

def load_3DMM_kpts():
    # 68 keypoints indices

    print('Loading 3DMM keypoints ...')
   
    fd = open(_3DMM_DEFINITION_DIR + '3DMM_keypoints.dat')
    kpts = np.fromfile(file=fd, dtype=np.int32)
    kpts = kpts.reshape((-1, 1))
    fd.close()

    return kpts - 1

def load_3DMM_tri_2d(with_mask = False):
    fd = open(_3DMM_DEFINITION_DIR + '3DMM_tri_2d.dat')
    tri_2d = np.fromfile(file=fd, dtype=np.int32)
    fd.close()

    tri_2d = tri_2d.reshape(192, 224)

    tri_mask = tri_2d != 0

    tri_2d[tri_2d == 0] = TRI_NUM+1 #VERTEX_NUM + 1
    tri_2d = tri_2d - 1

    if with_mask:
        return tri_2d, tri_mask

    return tri_2d
