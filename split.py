# authors: Zolboo Raph and Lan

# Importing libraries 
import cv2 
import os 

#this function takes the name of the video and splits the video
#into a group of images where each image is a frame in the video
#and saves it into 
def split_into_frames(vidname):

    # Read the video from specified path 
    cam = cv2.VideoCapture("./vids/"+vidname) 
    
    try: 
        
        # creating a folder named after the name of the video
        if not os.path.exists('Generated_Images_'+vidname): 
            make_directories(vidname) 
    
    # if not created then raise error 
    except OSError: 
        print ('Error: Creating directory of data') 
    
    # frame 
    currentframe = 0
    
    while(True): 
        
        # reading from frame 
        ret,frame = cam.read() 

        folder_name = './Generated_Images_'+vidname
    
        if ret: 
            # if video is still left continue creating images 
            name = folder_name + '/frame' + str(currentframe) + '.png'
            print ('Creating...' + name) 
    
            # writing the extracted images 
            cv2.imwrite(name, frame) 
    
            # increasing counter so that it will 
            # show how many frames are created 
            currentframe += 1
        else: 
            break
    
    # Release all space and windows once done 
    cam.release() 
    cv2.destroyAllWindows() 

# this function creates a directory with the specified name for the 
# images that are extracted from the videos
def make_directories(vid_name):

    # Directory
    directory = 'Generated_Images_'+vid_name

    # Parent Directory
    parent_dir = os.getcwd()

    # Path
    path = os.path.join(parent_dir, directory)

    # Create the directory in the project folder 
    os.mkdir(path) 
    #print("Directory '% s' created" % directory) 



