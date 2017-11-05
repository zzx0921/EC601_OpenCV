#include "opencv2/core/core.hpp"
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include "iostream"

 // Author Rishab Shah

using namespace cv;
using namespace std;
 
int main(int argc, char** argv )
{
    Mat src;
    src = imread(argv[1], CV_LOAD_IMAGE_COLOR);           //load the image
    namedWindow( "Original image", CV_WINDOW_AUTOSIZE );  //open a window
    imshow( "Original image", src);                       //show images

	vector<Mat> input_planes(3);
	split(src,input_planes);                              //split into three channels
	Mat channel1_display, channel2_display, channel3_display;
        imshow("Red",   input_planes[2]);
        imshow("Green",   input_planes[1]);
        imshow("Blue",   input_planes[0]);


	Mat ycrcb_image;
	cvtColor(src, ycrcb_image, CV_BGR2YCrCb);            //convert BGR into YCrCb
	split(ycrcb_image,input_planes);                     //split into three channels
        imshow("Y",   input_planes[0]);
        imshow("Cb",   input_planes[1]);
        imshow("Cr",   input_planes[2]);


	Mat hsv_image;
	cvtColor(src, hsv_image, CV_BGR2HSV);               //convert BGR into HSV
	vector<Mat> hsv_planes(3);                          //split into three channels
	split(hsv_image,hsv_planes);
        imshow("Hue",   hsv_planes[0]);
        imshow("Saturation",   hsv_planes[1]);
        imshow("Value",   hsv_planes[2]);


	
    waitKey(0);                                       
    return 0;
} 
