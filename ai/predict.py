from tensorflow.keras.models import load_model
import cv2
import numpy as np

def Predict(filename):
    # load the existing trained model
    loaded_model = load_model("ai/models/model.h5")
  

    loaded_model.compile(
        loss='binary_crossentropy',
        optimizer='adam',
        metrics=['accuracy'],
    )
    test_path = filename
    test_data = []
    image_size = 50

    #convert image to grayscale and then to an array
    image_array = cv2.imread(test_path ,cv2.IMREAD_GRAYSCALE)  

    #resize the array
    resized_array = cv2.resize(image_array, (image_size, image_size)) 

    # add the data to a list
    test_data.append([resized_array]) 

    #reshape the array
    test_data = np.array(test_data).reshape(-1, image_size, image_size, 1)

    out = loaded_model.predict(test_data)
    
    if out == 0:
        return "Hmmm. I think this is this a Dog"
    else:
        return "Hmmm. I think this is this a Cat"
