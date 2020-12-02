# This is the main script that allows us to explore the differences 
# between deepfake models that have been trained with different number
# of iterations. We have used the model with 50000 iterations as the baseline
# to compare it to the ones with lesser iterations, specifically, 100, 200, 500, 1000, 2000, 5000,
# 1000,2000, 5000, 7500,10000 and 20000 iterations. We compare these videos using MSE and SSIM methods 
# and graph them using matplotlib and 
# generate a table using plotly

# authors: Zolboo Raph and Lan

# Importing libraries 
import cv2 
import os 
from split import split_into_frames
from loop import iterate 
from plot import saveStuff

def main():
    # this list will be used to plot the MSE values of comparisons
    msevals = []

    # SSIM values of comparisons. SSIM and MSE are both Y-axis values
    ssimvals = []

    # X-axis values: the number of iterations
    numiters = []

    # Generate All the Images
    # Generating images for the model with 100 iterations
    split_into_frames("100.mp4")

    # Generating images for the model with 200 iterations
    split_into_frames("200.mp4")

    # Generating images for the model with 500 iterations
    split_into_frames("500.mp4")

    # Generating images for the model with 1000 iterations
    split_into_frames("1000.mp4")

    # Generating images for the model with 2000 iterations
    split_into_frames("2000.mp4")

    # Generating images for the model with 5000 iterations
    split_into_frames("5000.mp4")

    # Generating images for the model with 10000 iterations
    split_into_frames("10000.mp4")

    # Generating images for the model with 20000 iterations
    split_into_frames("20000.mp4")

    # Generating images for the model with 50000 iterations
    split_into_frames("50000.mp4")

    def compare(video1, video2):

        print("Comparing"+ str(video1))

        # loops through each of the pictures in the provided folders and 
        # compare them using the metrics MSE, PSNR and SSIM
        # between the model with 50000 iterations and 100 iterations
        firstFolder = 'Generated_Images_Test_'+str(video1)+'_Iterations.mp4'
        secondFolder = 'Generated_Images_Test_'+str(video2)+'_Iterations.mp4'

        # getting the MSE and SSIM values of the comparisons
        mse, ssim = iterate(firstFolder, secondFolder)
        
        #print("MSE: "+str(mse))
        #print("SSIM: "+str(ssim))

        # updating the plot lists
        numiters.append(video1)
        msevals.append(mse)
        ssimvals.append(ssim)

    #comparing the rest of the models with the base line
    compare(100, 50000)
    compare(200, 50000)
    compare(500, 50000)
    compare(1000, 50000)
    compare(2000, 50000)
    compare(5000, 50000)
    compare(10000, 50000)
    # compare(20000, 50000)  


    # write csv of output
    csvName = "metrics.csv"
    # no need to close
    with open(csvName, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["Iterations", "MSE", "SSIM"])
        for i in len(numiters):
            csvwriter.writerow([numiters[i], msevals[i], ssimvals[i])

    saveStuff("metrics.csv")

main()
