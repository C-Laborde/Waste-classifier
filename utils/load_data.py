import os
from matplotlib import image
from matplotlib import pyplot
import numpy as np


def load_data(data_type):
    path = os.path.join("data", data_type)
    files = os.listdir(path)
    if data_type is "test":
        all_data = []
        labels = []
        materials = ["cardboard", "glass", "metal", "paper", "plastic", "trash"]
        for img in files:
            img_path = os.path.join(path, img)
            all_data.append(image.imread(img_path))

            
    
    if data_type is "train" or data_type is "valid":
        


    return (np.array(all_data), labels)
        