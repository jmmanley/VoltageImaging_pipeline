import numpy as np
import matplotlib.pyplot as plt

def naive_std_ROIs(data, THRESH, MIN_AREA):

   from skimage.measure import regionprops, label
   
   if len(data.shape) > 2:
      std_img = np.std(data,0)
   else:
      std_img = data
   
   props = regionprops(label(std_img>THRESH), intensity_image=std_img)
   props = [props[x] for x in np.argsort([1/p.area for p in props]) if props[x].area > MIN_AREA]

   return props


def plot_props(img, props):
   
   plt.matshow(img);

   for i in range(len(props)):
      box = props[i].bbox
      r = [box[0],box[2],box[2],box[0], box[0]]
      c = [box[3],box[3],box[1],box[1], box[3]]

      plt.plot(c, r, c='r');
