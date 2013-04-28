import cv
from freenect import sync_get_depth as get_depth, sync_get_video as get_video
import numpy
from OpenGL.GL import *
from OpenGL.GLU import *
import os, sys
import random
from math import *

"""
Draw Function
Process OpenGL Matrix
The OpenGL matrix is passed to the Draw() function, along with the RGB colour image. Here, for each point a vertex generated and placed inside the display. Finally the RGB image is mapped to the point cloud giving it the extra detail.
"""

def Draw(xyz,gl_rgb_tex,rgb,indices):
    gl_rgb_tex
    print 'fuck1'
    glGenTextures(1);
    print 'fuck3'
    """
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glLoadIdentity();
    zoom = 1
    glPushMatrix();
    glScalef(zoom,zoom,1);
    glTranslatef(0,0,-3.5);
    glRotatef(0, 1,0,0);
    glRotatef(0, 0,1,0);
    glTranslatef(0,0,1.5);
    LoadVertexMatrix();

    print 'fuck2'
    #Set the projection from the XYZ to the texture image
    glMatrixMode(GL_TEXTURE);
    glLoadIdentity();
    glScalef(1/640.0,1/480.0,1);
    LoadRGBMatrix();
    LoadVertexMatrix();
    glMatrixMode(GL_MODELVIEW);

    glPointSize(1);

    glEnableClientState(GL_VERTEX_ARRAY);
    glVertexPointer(3, GL_SHORT, 0, xyz);
    glEnableClientState(GL_TEXTURE_COORD_ARRAY);
    glTexCoordPointer(3, GL_SHORT, 0, xyz);

    print 'fuck3'

    glEnable(GL_TEXTURE_2D);
    glBindTexture(GL_TEXTURE_2D, 1);
    glTexEnvf( GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE )
    glTexParameterf( GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR )
    gluBuild2DMipmaps( GL_TEXTURE_2D, 3, 640, 480, GL_RGB, GL_UNSIGNED_BYTE, rgb );

    glPointSize(2.0);
    glDrawElements(GL_POINTS, 640*480, GL_UNSIGNED_INT, indices);
    glPopMatrix();
    glDisable(GL_TEXTURE_2D);
    """

while True:
    """ (1)
    Setup OpenGL Matrices
    First a matrix is created that contains all of the x and y locations of the pixels. This will always be the same, so it can be initialised at the beginnning, and resued later. It is wise to offset the the x-axis, as the depth map and rgb image do not align properly. I'll leave you to experiment with that, it's just a minor adjustment. :-)
    """
    xyz=numpy.empty((480,640,3))
    indices=numpy.empty((480,640))
    for i in range(480):
        for j in range(640):
            xyz[i][j][0] = j
            xyz[i][j][1] = i
            indices[i][j] = i*640+j

    """
    Now, the depth value is added to this matrix. This must be done each time a new depth map is generated and recieved by the program.
    """
    (depth,_),(rgb,_)=get_depth(),get_video()
    depth=depth.flatten()
    for i in range(480):
        for j in range(640):
            xyz[i][j][2] = depth[i*640+j]

    Draw(xyz,"hello",rgb,[1,2,3])
