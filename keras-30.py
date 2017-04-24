import numpy as np

from math import floor

from PIL import Image

from os import listdir, remove
from os.path import isfile, join

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

animeTestingImagesFolder = "rick+and+morty" # yes, I know rick and morty isn't really anime...
realTestingImagesFolder = "sherlock+holmes+movie"

animeTrainFolderPath = "/".join([imagesFolderPath, animeTrainingImagesFolder])
animeTrainingImageFilenames = [f for f in listdir(animeTrainFolderPath) if isfile(join(animeTrainFolderPath, f))]

realTrainFolderPath = "/".join([imagesFolderPath, realTrainingImagesFolder])
realTrainingImageFilenames = [f for f in listdir(realTrainFolderPath) if isfile(join(realTrainFolderPath, f))]

# ===================


x_train = np.zeros((600, 22500))

for idx, f in enumerate(animeTrainingImageFilenames):
    try:
        img = np.ravel(np.asarray(Image.open(animeTrainFolderPath+ "/" + f)))
        # print np.shape(img)
        # exit(0)
        # print np.sum(img)
        # print np.shape(img)
        x_train[idx] = img
        # print idx
    except Exception as e:
        print e
        print 'had to pass'

for idx, f in enumerate(realTrainingImageFilenames):
    try:
        img = np.ravel(np.asarray(Image.open(realTrainFolderPath+ "/" + f)))
        # print np.shape(img)
        # exit(0)
        # print np.sum(img)
        # print np.shape(img)
        x_train[91 + idx] = img
        # print idx
    except Exception as e:
        print e
        print 'had to pass'

# ===================== testing

animeTestFolderPath = "/".join([imagesFolderPath, animeTestingImagesFolder])
animeTestingImageFilenames = [f for f in listdir(animeTestFolderPath) if isfile(join(animeTestFolderPath, f))]

realTestFolderPath = "/".join([imagesFolderPath, realTestingImagesFolder])
realTestingImageFilenames = [f for f in listdir(realTestFolderPath) if isfile(join(realTestFolderPath, f))]

# ===================


x_test = np.zeros((600, 22500))

for idx, f in enumerate(animeTestingImageFilenames):
    try:
        img = np.ravel(np.asarray(Image.open(animeTestFolderPath+ "/" + f)))
        # print np.shape(img)
        # exit(0)
        # print np.sum(img)
        # print np.shape(img)
        x_test[idx] = img
        # print idx
    except Exception as e:
        print e
        print 'had to pass'

for idx, f in enumerate(realTestingImageFilenames):
    try:
        img = np.ravel(np.asarray(Image.open(realTestFolderPath+ "/" + f)))
        # print np.shape(img)
        # exit(0)
        # print np.sum(img)
        # print np.shape(img)
        x_test[91 + idx] = img
        # print idx
    except Exception as e:
        print e
        print 'had to pass'

train_img_count = 190

x_train = x_train[0:189]
y_train = np.zeros((189))
y_train[92:] += 1
# print y_train

x_test = x_test[0:196]
y_test = np.zeros((196))
y_test[98:] += 1
# print y_test


# # y_train = np.random.randint(2, size=(1000, 1))
# y_train = x_train % 2
# # x_test = np.random.random((100, 1))
# # x_test = np.random.randint(100, size=1000)
# x_test = np.arange(100)
# # y_test = np.random.randint(2, size=(100, 1))
# y_test = x_test % 2

model = Sequential()
model.add(Dense(2250, input_dim=22500, activation='relu'))
# model.add(Dropout(0.5))
model.add(Dense(225, activation='relu'))
# model.add(Dense(800, activation='relu'))
# model.add(Dense(500, activation='relu'))
# model.add(Dense(250, activation='relu'))
# model.add(Dense(50, activation='relu'))
# model.add(Dense(25, activation='relu'))
# model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy',
            #   optimizer='rmsprop',
              optimizer="adam",
              metrics=['accuracy'])

model.fit(x_train, y_train,
          epochs=3,
          batch_size=int(floor(len(x_train)/10)))
score = model.evaluate(x_test[:135], y_test[:135], batch_size=10)
print score