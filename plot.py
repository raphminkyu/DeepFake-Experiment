import matplotlib.pyplot as plt
import plotly.graph_objects as go
import pandas as pd
import os


def plotIterMSE(csv):

    # plotting the MSE points  
    plt.plot(csv["Iterations"], csv["MSE"], label = "Mean Squared Error") 

    # naming the x axis 
    plt.xlabel('Number of Iterations') 

    # naming the y axis 
    plt.ylabel('MSE Values of the Models') 

    # giving a title to my graph 
    plt.title('Models Trained with Various Number of Iterations VS MSE of Each Model') 
    
    # function to show the plot 
    # plt.show() 
    plt.savefig(os.getcwd()+"/"+"mse.jpg")

def plotIterSSIM(csv):
    # plotting the SSIM points  
    plt.plot(csv["Iterations"], csv["SSIM"], label = "Structure Similarity") 

    # naming the x axis 
    plt.xlabel('Number of Iterations') 

    # naming the y axis 
    plt.ylabel('SSIM Values of the Models') 

    # giving a title to my graph 
    plt.title('Models Trained with Various Number of Iterations VS SSIM of Each Model') 
    
    # function to show the plot 
    # plt.show() 
    plt.savefig(os.getcwd()+"/"+"ssim.jpg")

def makeTable(csv):
    # set up the table from the values
    fig = go.Figure(data=[go.Table( 
        header=dict(values=['Iterations', 'MSE', 'SSIM']), 
        cells=dict(values=[csv["Iterations"], csv["MSE"], csv["SSIM"]])) 
    ]) 

    # show the table
    fig.write_image(os.getcwd()+"/"+"table.jpg") 

def saveStuff(csvFile):
    csv = pd.read_csv(os.getcwd()+"/"+csvFile)
    plotIterMSE(csv)
    # clear matplotlib plt
    plt.clf()
    plotIterSSIM(csv)
    makeTable(csv)
    
# plotBoth("metrics.csv")


