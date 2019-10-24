import numpy as np
import matplotlib.pyplot as plt
import pyfits

def load(file):
   return pyfits.open(file)[0].data


def register_stack(stack, template):
   
    return None

def plot_many_signals(signals, spread=5):

    for i in range(signals.shape[0]):
        plt.plot(signals[i,:] + i*spread)