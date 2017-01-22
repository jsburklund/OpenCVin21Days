# Copied from Day 1 of PyImageSearch tutorials

from pyimagesearch.searcher import Searcher
import numpy as np
import argparse
import cPickle
import cv2

# Construct argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
    help="Path to the directory that contains the images we just indexed")
ap.add_argument("-i", "--index", required=True,
    help="Path to where index database is stored")
args = vars(ap.parse_args())

# load the index and initialize the searcher
index = cPickle.loads(open(args["index"]).read())
searcher = Searcher(index)

# loop over images in the index -- use each as a query for tests
for (query, queryFeatures) in index.items():
  # perform the search using the current query
  results = searcher.search(queryFeatures)

  # load the query image and display it
  path = args["dataset"] + "/%s" % (query)
  queryImage = cv2.imread(path)
  cv2.imshow("Query", queryImage)
  print "query: %s" % (query)

  # initialize the two montages to display the results (show top 10)
  montageA = np.zeros((166*5,400,3), dtype="uint8")
  montageB = np.zeros((166*5,400,3), dtype="uint8")

  # loop over the top ten results
  for j in xrange(0,10):
    # grab the result (using row-major order) and load result image
    (score, imageName) = results[j]
    path = args["dataset"]+"/%s"%(imageName)
    result = cv2.imread(path)
    print "\t%d. %s : %.3f" % (j+1, imageName, score)
    
    # check to see if the first montage should be used
    if j<5:
      # Add the image to the A montage
      montageA[j*166:(j+1)*166, :] = result

    # check to see fithe second montage should be used
    else:
      montageB[(j-5)*166:((j-5)+1)*166, :] = result

  # show the results
  cv2.imshow("Results 1-5", montageA)
  cv2.imshow("Results 6-10", montageB)
  cv2.waitKey(0)
