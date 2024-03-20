import os
import numpy as np
import cv2
from glob import glob 
from tqdm import tqdm
import imageio
from albumentations import HorizontalFlip, VerticalFlip, ElasticTransform, GridDistortion, OpticalDistortion, CoarseDropout


def create_dir(path):
    if not os.path.exists(path):
        try:
            os.mkdirs(path)
        except:
            print("Error creating directory")
        
def load_data(path):
    """ X = Images and Y = masks """
    train_x = sorted(glob(os.path.join(path, "training", "images", "*.tif")))
    train_y = sorted(glob(os.path.join(path, "training", "1st_manual", "*.gif")))                               
    
    test_x = sorted(glob(os.path.join(path, "test", "images", "*.tif")))
    test_y = sorted(glob(os.path.join(path, "test", "1st_manual", "*.gif")))                               
    
    return (train_x, train_y), (test_x, test_y)

def augment_data(images, masks, save_path, augment=True):
    H = 512
    W = 512
    
    for idx, (x, y) in tqdm(enumerate(zip(images, masks)), total = len(images), desc="Progresing..."):
        """ Extracting names """
        #name = x.split()
        print(x, y)
        break

if __name__ == "__main__":
    """ Seeding"""
    np.random.seed(41)
    
    """ Load the Data """
    data_path = os.getcwd()
    (train_x, train_y), (test_x, test_y) = load_data(data_path)

    print(f"Train: {len(train_x)} - {len(train_y)}")
    print(f"Train: {len(test_x)} - {len(test_y)}")
  
    """ Create Directories """
    
    create_dir(os.path.join(os.getcwd(), "/new_data"))

    """
    create_dir(os.getcwd()+"new_data\train\mask")
    create_dir(os.getcwd()+"new_data\test\image")
    create_dir(os.getcwd()+"new_data\test\mask")
    """
   # augment_data(train_x, train_y, "new_data/train/", augment=True)