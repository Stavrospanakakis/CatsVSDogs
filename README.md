# Cats vs Dogs

Cats vs Dogs is a simple app I created in order to start practicing with Machine Learinng. You upload an image 
and it recognises if it is a cat or a dog. Also you can train the model again if you want by clicking one button.
I didn't really focus on the UI/UX but on the algorithm of the neural network.

## Installation
I used the [Kaggle Cats and Dogs Dataset](https://www.microsoft.com/en-us/download/details.aspx?id=54765) to train it.

Download the dataset and add the images into the ai/images/train

#### Docker
You should have Docker and Docker Compose installed.
```
$ cd build
$ docker-compose up --build
```
#### Manually
You should have pip installed.
```
$ cd build
$ pip install -r requirements.txt
$ cd ..
$ python app.py
```
Then browse to http://localhost:8000

