import numpy as np
import matplotlib.pyplot as plt

def naive_std_ROIs(data, THRESH, MIN_AREA):

   from skimage.measure import regionprops, label
   
   if len(data.shape) > 2:
      std_img = np.std(data,0)
   else:
      std_img = data
   
   rois = regionprops(label(std_img>THRESH), intensity_image=std_img)
   rois = [rois[x] for x in np.argsort([1/p.area for p in rois]) if rois[x].area > MIN_AREA]

   return rois


def plot_ROIs(img, props):
   
   plt.matshow(img);

   for i in range(len(props)):
      box = props[i].bbox
      r = [box[0],box[2],box[2],box[0], box[0]]
      c = [box[3],box[3],box[1],box[1], box[3]]

      plt.plot(c, r, c='r');


def extract_activity(rois, data):

   timeseries = np.zeros((len(rois), data.shape[0]))

   for i in range(len(rois)):
      curr = np.asarray([data[:,x,y] for (x,y) in rois[i].coords])

      timeseries[i,:] = np.mean(curr,0)

   return timeseries