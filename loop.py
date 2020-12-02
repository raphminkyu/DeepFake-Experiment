# authors: Zolboo Raph and Lan

import os
import metrics

def getImgList(dir, folder1, folder2):
    '''
    Gets 2 list of sorted images in each folder

    :param str folder1: path to folder1 with images to compare
    :param str folder2: path to folder2 with images to compare

    return: tuple (2) of list1 and list2
    
    raises ValueError: if folder1 and folder2 have different number of images
    raises ValueError: if folder1 or folder2 have 0 images
    '''

    # os.walk generatea filenames 
    # os.walk() returns all files
    # next() returns next item in iterator
    print("Getting list of filenames for {} and {}".format(folder1, folder2))
    fold1 = next(os.walk(dir+"/"+folder1))[2]
    fold2 = next(os.walk(dir+"/"+folder2))[2]
    
    if len(fold1) ==0 or len(fold2)==0:
        raise ValueError("0 images")
    # outputs generated via Google Colab have files with ._ prefix and must be exterminated
    if len(fold1)*2 == len(fold2):
        cleanUp(dir+"/"+folder2)
        print("Cleaned up {}".format(dir+"/"+folder2))
        fold2 = next(os.walk(dir+"/"+folder2))[2]
    if len(fold1)!= len(fold2):
        raise ValueError("Different number of images in each folder {} ({}) and {} ({})".format(folder1, len(fold1), folder2,len(fold2)))

    fold1.sort()
    fold2.sort()
    return(fold1, fold2)

def iterate(dir, folder1,folder2):
    '''
    Gets 2 list of sorted images in each folder

    :param str folder1: path to folder1 with images to compare
    :param str folder2: path to folder2 with images to compare

    return: tuple (3) of (MSE, PSNR, SSIM)
    '''

    list1, list2 = getImgList(dir, folder1,folder2)
    mse = 0
    ssim=0

    # calculates metric for each corresponding image
    # calculate how many iterations ran
    count = 0
    for i in range(0, len(list1), int(len(list1)/10)+1):
        count+=1
        path1 = "{}/{}/{}".format(dir,folder1,list1[i])
        path2 = "{}/{}/{}".format(dir,folder2,list2[i])
        # 3 decimal digit
        mse += metrics.mse(path1, path2)
        ssim += metrics.ssim(path1, path2)

    mse = float(f'{mse/count:.4g}')
    ssim = float(f'{ssim/count:.4g}')
        
    return (mse,ssim)

def cleanUp(dir):
    fold = next(os.walk(dir))[2]
    for name in fold:
        if name.startswith("._"):
            os.remove("{}/{}".format(dir,name))
