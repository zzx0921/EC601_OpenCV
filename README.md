 EC601_OpenCV


Exercise 1

How does a program read the cvMat object, in particular, what is the order of the pixel structure?

In ColorImage.cpp, cvMat is a matrix which store the pixels of the image. It has three channels, red, green and blue. Matrix elements are stored row by row. Programs read cvMat object by using cvMatName.at(x,y). Program read the cvMat object in a similar way with the matrix object.


Exercise 2

2.Print out the values of the pixel at (20,25) in the RGB, YCbCr and HSV versions of the image. What are the ranges of pixel values in each channel of each of the above mentioned colorspaces?

For RGB, the values of the pixel at [20,25] are [106 122 225].

For HSV, the values of the pixel at [20,25] are [151 181 103].

For YCbCr, the values of the pixel at [20,25] are [  4 135 225].

The range should be [0,255].
