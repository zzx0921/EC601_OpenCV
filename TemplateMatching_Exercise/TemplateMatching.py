import numpy as np
import cv2

def TemplateMatching(src, temp, stepsize): # src: source image, temp: template image, stepsize: the step size for sliding the template
    mean_t = 0
    var_t = 0
    location = [0, 0]
    sum_t = 0
    sum_v1 = 0
# Calculate the mean and variance of template pixel values
# ------------------ Put your code below ------------------    
    for i in range(temp.shape[0]):
        for j in range(temp.shape[1]):
            sum_t = sum_t+temp[i,j]
    mean_t = sum_t/(temp.shape[0]*temp.shape[1])
    
    for i in range(temp.shape[0]):
        for j in range(temp.shape[1]):
            sum_v1 = sum_v1+((temp[i,j]-mean_t)**2)
            var_t = var_t+(sum_v1/(temp.shape[0]*temp.shape[1]))
                   
    max_corr = 0
    a = 0
    # Slide window in source image and find the maximum correlation
    for i in np.arange(0, src.shape[0] - temp.shape[0], stepsize):
        for j in np.arange(0, src.shape[1] - temp.shape[1], stepsize):
            mean_s = 0
            var_s = 0
            corr = 0
           
            # Calculate the mean and variance of source image pixel values inside window
            # ------------------ Put your code below ------------------ 
            for x in range(i,i+temp.shape[0]):
                for y in range(j,j+temp.shape[1]):
                    mean_s += src[x][y]
            mean_s = mean_s/(temp.shape[0]*temp.shape[1])
            
            for x in range(i,i+temp.shape[0]):
                for y in range(j,j+temp.shape[1]):
                    var_s += (src[x][y] - mean_s)**2
            var_s = var_s/(temp.shape[0]*temp.shape[1])
                    
            # Calculate normalized correlation coefficient (NCC) between source and template
            # ------------------ Put your code below ------------------ 
            a = 0
            for ii in range(temp.shape[0]):
                for jj in range(temp.shape[1]):
                    a += (temp[ii][jj] - mean_t)*(src[i+ii][j+jj] - mean_s)
                    
            corr = (1/(temp.shape[0]*temp.shape[1]))*a/(var_t*var_s)
            
            if corr > max_corr:
                max_corr = corr
                location = [i, j]
    return location

# load source and template images
source_img = cv2.imread('source_img.jpg',0) # read image in grayscale
temp = cv2.imread('template_img.jpg',0) # read image in grayscale
location = TemplateMatching(source_img, temp, 20);
print(location)
match_img = cv2.cvtColor(source_img, cv2.COLOR_GRAY2RGB)

# Draw a red rectangle on match_img to show the template matching result
# ------------------ Put your code below ------------------ 
cv2.rectangle

# Save the template matching result image (match_img)
# ------------------ Put your code below ------------------ 
cv2.imwrite("Template_Matching.jpg",match_img)

# Display the template image and the matching result
cv2.namedWindow('TemplateImage', cv2.WINDOW_NORMAL)
cv2.namedWindow('MyTemplateMatching', cv2.WINDOW_NORMAL)
cv2.imshow('TemplateImage', temp)
cv2.imshow('MyTemplateMatching', match_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
