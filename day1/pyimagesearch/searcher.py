# Code copied from Day 1 of PyImageSearch tutorials
import numpy as np

class Searcher:
  def __init__(self, index):
    # store the index of images
    self.index = index

  def search(self, queryFeatures):
    # initialize dictionary of results
    results = {}

    # loop over the index
    for (k, features) in self.index.items():
      # compute the chi-squared distance between the features
      # in our index and query features -- chi-squared typically
      # used for histograms
      d = self.chi2_distance(features, queryFeatures)

      # given the distance between both features
      # update reseults dictionary.  Key is image ID, 
      # values is distance
      results[k] = d

    # sort the results where the smallest distances are first
    results = sorted([(v,k) for (k,v) in results.items()])
    return results

  def chi2_distance(self, histA, histB, eps= 1e-10):
    # compute the chi-squared distance
    d = 0.5 * np.sum([((a - b) **2) / (a + b + eps)
      for (a,b) in zip(histA, histB)])
    return d
