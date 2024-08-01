import numpy as np
from PIL import Image
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from google.colab.patches import cv2_imshow
import cv2
import glob

os.mkdir('/content/image resized')

original_folder = '/content/dataset_dogs_vs_cats/train/cats/'
resized_folder = '/content/image resized/'

for i in range(1000):
  file_name = os.listdir('/content/dataset_dogs_vs_cats/test/cats')[i]
  img = Image.open(original_folder + file_name)
  img = img.resize((224,224))
  img = img.convert('RGB')
  img.save(resized_folder + file_name)

original_folder = '/content/dataset_dogs_vs_cats/train/cats/'
resized_folder = '/content/image resized/'

for i in range(1000):
  file_name = os.listdir('/content/dataset_dogs_vs_cats/test/cats')[i]
  img = Image.open(original_folder + file_name)
  img = img.resize((224,224))
  img = img.convert('RGB')
  img.save(resized_folder + file_name)