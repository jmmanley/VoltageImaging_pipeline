import numpy as np
import matplotlib.pyplot as plt
import pyfits

def load(file):
   return pyfits.open(file)[0].data
