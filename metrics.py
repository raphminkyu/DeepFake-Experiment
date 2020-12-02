import cv2
import numpy as np
import math

def mse(img1, img2):
	'''
    Gets MSE of corresponding pixels in two images

    :param str img1: path to image1
    :param str img2: path to image2

    return: float value of mse
    '''
	i1 = cv2.imread(img1)
	i2 = cv2.imread(img2)
	
	#if img dimensions are different, reutrn error
	if i1.shape[0] != i2.shape[0] or i1.shape[1] != i2.shape[1] :
		raise Exception('image have different size')

	mse = np.square(np.subtract(i1,i2)).mean()
	return mse

def psnr(img1,img2):
	'''
    Gets PSNR of corresponding pixels in two images
		-computes MSE after denoising
		-slightly biased for smooth result
		-lower the error, higher the PSNR
		-https://www.mathworks.com/help/vision/ref/psnr.html#:~:text=The%20mean%2Dsquare%20error%20(MSE,MSE%2C%20the%20lower%20the%20error.

    :param str img1: path to image1
    :param str img2: path to image2

    return: float value of PSNR
    '''
	i1 = cv2.imread(img1)
	i2 = cv2.imread(img2)
	i1 = i1.astype(np.float64)
	i2 = i2.astype(np.float64)
	mseVal = mse(img1,img2)
	if  mseVal == 0:
		return float('inf')
	maxVal =255
	return 10 * math.log10(maxVal**2/ math.sqrt(mseVal))


def ssim(img1, img2):
	'''
    Gets SSIM of corresponding pixels in two images
		simplified from scikit-image 's strucutral similarity method:
		https://github.com/scikit-image/scikit-image/blob/v0.17.2/skimage/metrics/_structural_similarity.py#L12
		implements uniform filtering as compared to gaussian filter
		ranges from -1 to 1, 1 being identical and -1 being totes different

    :param str img1: path to image1
    :param str img2: path to image2

    return: float value ssim
	'''

	i1 = cv2.imread(img1)
	i2 = cv2.imread(img2)
	i1 = i1.astype(np.float64)
	i2 = i2.astype(np.float64)

	kernel = np.ones((5,5),np.float32)/25
	# kernel 
	# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_filtering/py_filtering.html
	muX = cv2.filter2D(i1,-1,kernel)
	mu2x = muX *muX

	muY = cv2.filter2D(i2,-1,kernel)
	mu2y = muY *muY
	# varX = E(X^2) - (E(X))^2
	varX = cv2.filter2D(i1*i1,-1,kernel) - mu2x
	varY = cv2.filter2D(i2*i2,-1,kernel) - mu2y
	# covXY = E(XY)-E(X)E(Y)
	covXY = cv2.filter2D(i1*i2,-1,kernel) - muX*muY
	# constant: https://en.wikipedia.org/wiki/Structural_similarity
	k1 = 0.01
	k2 = 0.03
	# L: dynamic range of pixel values, 2^(bits per pixel)-1. 
	# L = 256-1 in our case
	L = 255
	# c_1 = (k_1*L)^2
	c1 = (k1*L)**2
	c2 = (k2*L)**2
	ssimMatrix = ((2*muX*muY + c1)*(2*covXY+c2)) / ((mu2x+mu2y+c1)*(varX+varY+c2))
	return ssimMatrix.mean()

