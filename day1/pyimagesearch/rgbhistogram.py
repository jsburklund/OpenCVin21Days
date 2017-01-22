#Code copied from Day 1 of PyImageSearch tutorials
import numpy as np
import cv2

class RGBHistogram:
  def __init__(self, bins):
    #store the number of bins the histogram will use
    self.bins = bins

  def describe(self, image):
    #compute a 3D histogram in RGB colorspace,
    #then normalize the histogram so that images
    #with the same content at different scales
    #will have approximately the same histogram
    hist = cv2.calcHist([image], [0,1,2],
      None, self.bins, [0,256, 0,256, 0,256])
    hist = cv2.normalize(hist)

    # return 3D histogram as a flattened feature vector
    return hist.flatten()
