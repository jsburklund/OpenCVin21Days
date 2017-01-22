# Copied from Day 1 of PyImageSearch tutorials

from pyimagesearch.rgbhistogram import RGBHistogram
import argparse
import cPickle
import glob
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
    help="Path to the direcory that contains the images to be indexed")
ap.add_argument("-i", "--index", required=True,
    help="Path to where the computed index will be stored")
args = vars(ap.parse_args())

# initialize the index dictionary to store our quantified images
# with the 'key' being the image filename, and the 'value'
# being the computed feature vector
index = {}

# initialize the image descriptor -- a 3D RGB histogram with 8 bins each
desc = RGBHistogram([8,8,8])

# use glob to grap the image paths and loop over them
for imagePath in glob.glob(args["dataset"]+"/*.png"):
  # extract the image filename
  k = imagePath[imagePath.rfind("/")+1:]

  # load the image, get the feature vector, and add it to the database
  image = cv2.imread(imagePath)
  features = desc.describe(image)
  index[k] = features

# Write image database to disk
f = open(args["index"], "w")
f.write(cPickle.dumps(index))
f.close()
