from PIL import Image

from os import listdir, remove
from os.path import isfile, join

imagesFolder = "images"
foldernames = [
        "anime+fairy+tail",
        "rick+and+morty",
        "anime+fma+brotherhood",
        "avengers+movie",
        "lord+of+the+rings+scene",
        "sherlock+holmes+movie"
    ]

folderpaths = []

for folder in foldernames:
    folderpaths.append(imagesFolder + "/" + folder)
for folder in folderpaths:
    onlyfiles = [f for f in listdir(folder) if isfile(join(folder, f))]

    for f in onlyfiles:
        try:
            im = Image.open(folder+"/"+f)
            im = im.resize((800, 600))
            print f
            im.save(folder+"/"+f)
            im.close()
        except Exception as e:
            remove(folder+"/"+f)

    # onlyfiles = [f for f in listdir(folder) if isfile(join(folder, f))]
    # for f in onlyfiles:
    #     im = Image.open(folder+"/"+f)
    #     print str(im.height) + " - " + str(im.width)
    #     im.close()