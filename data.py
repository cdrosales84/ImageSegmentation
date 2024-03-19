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
    train_x = sorted(glob(os.path.join(path, "training", "images, "*.png")))
    train_y = sorted(glob(os.path.join(path, "training", "images, "*.png")))                               
    
    test_x = sorted(glob(os.path.join(path, "test", "images, "*.png")))
    test_y = sorted(glob(os.path.join(path, "test", "images, "*.png")))                               
    
    return (train_x, train_y), (test_x, test_y)

if __name__ == "__main__":
    """ Seeding"""
    np.random.seed(41)