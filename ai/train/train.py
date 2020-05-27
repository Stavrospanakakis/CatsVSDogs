from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Activation, MaxPooling2D, Flatten, Dropout
import tensorflow as tf
from .prepare_dataset import Prepare_dataset
import os
import numpy as np

def Train():
    model_path = 'ai/models/model.h5'

    train_images, train_labels = Prepare_dataset()

    # train the model
    model = Sequential()

    model.add(Conv2D(64, (3, 3), input_shape=train_images.shape[1:]))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(64, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Flatten()) 
    model.add(Dense(64))
    model.add(Activation('relu'))

    model.add(Dense(1))
    model.add(Activation('sigmoid'))


    model.compile(
        loss='binary_crossentropy',
        optimizer='adam',
        metrics=['accuracy'],
    )

    model.fit(
        train_images,
        train_labels,
        batch_size=32,
        epochs=20,
        validation_split=0.3,
    )

    if (os.path.exists(model_path)):
        
        #replace the old model with the new one
        os.remove(model_path)
        model.save(model_path)
    else:
        model.save(model_path)
