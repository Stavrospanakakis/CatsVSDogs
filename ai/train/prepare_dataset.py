import os
import cv2
import random
import numpy as np
from tqdm import tqdm
import tensorflow as tf

def Prepare_dataset():

    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
    
    directory = "./ai/images/train"
    
    categories = ["Dog", "Cat"]
    
    training_data = []
    
    image_size = 50
    
    # for dogs and cats
    for category in categories:  

        path = os.path.join(directory,category)  
        class_num = categories.index(category)  

        #for each image
        for img in tqdm(os.listdir(path)): 
            try:
                #convert image to grayscale and then to an array
                image_array = cv2.imread(os.path.join(path,img) ,cv2.IMREAD_GRAYSCALE) 
                
                # resize the image
                resized_array = cv2.resize(image_array, (image_size, image_size))  
                
                # add image and category to a a list
                training_data.append([resized_array, class_num]) 
            
            # just to keep the output clean
            except Exception as e:
                pass

    ##shuffle the data
    random.shuffle(training_data)

    #$ initialize the lists
    train_images = []
    train_labels = []    

    ##split the data as train images and train_labels 
    for features,label in training_data:
        train_images.append(features)
        train_labels.append(label)

    # reshape the arrays
    train_images = np.array(train_images).reshape(-1, image_size, image_size, 1)
    train_labels = np.array(train_labels)

    # normalize the data
    train_images = train_images/255.0

    return train_images, train_labels