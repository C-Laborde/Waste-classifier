import os
from matplotlib import image
from matplotlib import pyplot
import numpy as np


def load_data(data_type):
    path = os.path.join("data", data_type)
    files = os.listdir(path)
    materials = ["cardboard", "glass", "metal", "paper", "plastic", "trash"]
    mat_to_nr = {"cardboard": 0, "glass": 1, "metal": 2, "paper": 3, "plastic": 4, "trash": 5}
    all_data = []
    labels = []
    if data_type is "test":
        for img in files:
            img_path = os.path.join(path, img)
            all_data.append(image.imread(img_path))
            ret = -1
            i = 0
            while ret == -1:
                ret = img.find(materials[i])
                i += 1
            labels.append(mat_to_nr[materials[i-1]])

    if data_type is "train" or data_type is "valid":
        for mat in materials:
            mat_path = os.path.join(path, mat)
            files = os.listdir(mat_path) 
            for img in files:
                img_path = os.path.join(mat_path, img)
                all_data.append(image.imread(img_path))
            labels = labels + [mat_to_nr[mat]] * len(files)
    return np.array(all_data), labels
        