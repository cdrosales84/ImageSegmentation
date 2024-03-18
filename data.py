import os
import numpy as np
import cv2
from glob import glob 
from tqdm import tqdm
import imageio
from albumentations import HorizontalFlip, VerticalFlip, ElasticTransform, GridDistortion, OpticalDistortion, CoarseDropout


def create_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)
        
def load_data(path):
    """ X = Images and Y = masks """
    train_x = glob(os.path.join(path, "training", "images, "*.png"))