import numpy as np
from PIL import Image
from keras.models import Sequential
from keras.layers import Dense, Dropout

# Generate dummy data
# x_train = np.random.random((1000, 1))
# x_train = np.arange()

imagesFolderPath = "images"

animeTrainingImagesFolder = "anime+fairy+tail"
realTrainingImagesFolder = "avengers+movie"

animeValidationImagesFolder = "anime+fma+brotherhood"
realValidationImagesFolder = "lord+of+the+rings+scene"

animeTestImagesFolder = "rick+and+morty" # yes, I know rick and morty isn't really anime...
realTestImagesFolder = "sherlock+holmes+movie"





x_train = []


# y_train = np.random.randint(2, size=(1000, 1))
y_train = x_train % 2
# x_test = np.random.random((100, 1))
# x_test = np.random.randint(100, size=1000)
x_test = np.arange(100)
# y_test = np.random.randint(2, size=(100, 1))
y_test = x_test % 2

model = Sequential()
model.add(Dense(1, input_dim=1, activation='relu'))
# model.add(Dropout(0.5))
# model.add(Dense(64, activation='relu'))
# model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

model.fit(x_train, y_train,
          epochs=200,
          batch_size=10)
score = model.evaluate(x_test, y_test, batch_size=128)
